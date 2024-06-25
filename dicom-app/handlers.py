from pydicom.dataset import Dataset
# import requests
import json

from pynetdicom.sop_class import ModalityPerformedProcedureStep
from db import add_instance, search, InvalidIdentifier, Instance
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

managed_instances = {}

# Function to load JSON data and convert it to a Dataset
def load_worklist_from_json(json_data):
    ds = Dataset()
    ds.PatientName = json_data['PatientName']
    ds.PatientID = json_data['PatientID']
    ds.PatientBirthDate = json_data['PatientBirthDate']
    ds.PatientSex = json_data['PatientSex']
    ds.StudyID = json_data['StudyID']
    ds.AccessionNumber = json_data['AccessionNumber']
    ds.ReferringPhysicianName = json_data['ReferringPhysician']
    ds.StudyDescription = json_data['StudyDescription']

    ds.ScheduledProcedureStepSequence = [Dataset()]
    scheduled_procedure_step = ds.ScheduledProcedureStepSequence[0]
    scheduled_procedure_step.ScheduledProcedureStepStartDate = json_data[
        'ScheduledProcedureStepStartDate']
    scheduled_procedure_step.Modality = json_data['Modality']
    scheduled_procedure_step.ScheduledStationAETitle = json_data['ScheduledStationAETitle']
    scheduled_procedure_step.ScheduledPerformingPhysicianName = json_data[
        'ScheduledPerformingPhysician']
    scheduled_procedure_step.ScheduledProcedureStepLocation = json_data[
        'ScheduledProcedureStepLocation']
    scheduled_procedure_step.PreMedication = json_data['PreMedication']

    ds.ScheduledProcedureStepSequence = [scheduled_procedure_step]
    ds.RequestedProcedureID = json_data['RequestedProcedureID']
    ds.RequestedProcedureDescription = json_data['RequestedProcedureDescription']
    ds.SpecialNeeds = json_data['SpecialNeeds']

    return ds

def generate_dummy_data():
    # Load the dummy worklist JSON data
    with open('dummy_data/data.json', 'r') as file:
        worklist_data = json.load(file)

    # Convert JSON data to Dataset
    ds = load_worklist_from_json(worklist_data)

    # Assign the dataset to managed_instances[0]
    # Assuming managed_instances is a list with at least one element
    managed_instances[0] = ds

    # Print out the dataset to verify
    print(managed_instances[0])
    
def save_into_managed_instances(json_file_path):
    """Save the JSON file data into the managed_instances dictionary."""
    with open(json_file_path, 'r') as json_file:
        worklist_data = json.load(json_file)
        
    # Convert JSON data to Dataset
    ds = load_worklist_from_json(worklist_data)

    # Assign the dataset to managed_instances[0]
    # Assuming managed_instances is a list with at least one element
    managed_instances[0] = ds

    # Print out the dataset to verify
    print(managed_instances[0])
    
    

def handle_find(event):
    """Handle a C-FIND request event."""
    requestor = event.assoc.requestor
    req = event.request
    model =event.request.AffectedSOPClassUID
    ds = event.identifier
    timestamp = event.timestamp.strftime("%Y-%m-%d %H:%M:%S")
    addr, port = requestor.address, requestor.port
    # logger.info(f"Received C-FIND request from {addr}:{port} at {timestamp}")
    print(f"Received C-FIND request from {addr}:{port} at {timestamp}")
    
    if 'ScheduledProcedureStepSequence' not in ds:
        # Failure
        yield 0xC000, None
    
    # item = ds.ScheduledStepAttributesSequence
    item = ds.ScheduledProcedureStepSequence
    schedule = item[0].ScheduledProcedureStepStartDate
    ae_title = item[0].ScheduledStationAETitle

    for uid, instance in managed_instances.items():
        ScheduledProcedure = instance.get('ScheduledProcedureStepSequence')
        matching = [
            inst for inst in ScheduledProcedure if inst.ScheduledProcedureStepStartDate == schedule or inst.ScheduledAETitle == ae_title
        ]
    
    for instance in matching:
        # Check if C-CANCEL has been received
        if event.is_cancelled:
             yield (0xFE00, None)
             return
        
        # identifier = Dataset()
        # identifier.PatientName = ds.PatientName
        # identifier.ScheduledProcedureStepSequence = [Dataset()]
        # identifier.ScheduledStationAETitle = instance.ScheduledStationAETitle
        # identifier.ScheduledProcedureStepStartDate = instance.ScheduledProcedureStepStartDate
        # identifier.Modality = instance.Modality
        
        # Create the identifier dataset
        identifier = Dataset()
        identifier.PatientName = ds.PatientName
        # identifier.PatientID = ds.PatientID
        # identifier.PatientBirthDate = ds.PatientBirthDate
        # identifier.PatientSex = ds.PatientSex
        # identifier.StudyID = ds.StudyID
        # identifier.AccessionNumber = ds.AccessionNumber
        # identifier.ReferringPhysicianName = ds.ReferringPhysician
        # identifier.StudyDescription = ds.StudyDescription
        
        # Create the ScheduledProcedureStepSequence dataset
        identifier.ScheduledProcedureStepSequence = [Dataset()]
        scheduled_procedure_step = identifier.ScheduledProcedureStepSequence[0]
        scheduled_procedure_step.ScheduledProcedureStepStartDate = instance.ScheduledProcedureStepStartDate
        scheduled_procedure_step.Modality = instance.Modality
        scheduled_procedure_step.ScheduledStationAETitle = instance.ScheduledStationAETitle
        scheduled_procedure_step.ScheduledPerformingPhysicianName = instance.ScheduledPerformingPhysicianName
        scheduled_procedure_step.ScheduledProcedureStepLocation = instance.ScheduledProcedureStepLocation
        scheduled_procedure_step.PreMedication = instance.PreMedication
        
        # Add the ScheduledProcedureStepSequence to the identifier
        identifier.ScheduledProcedureStepSequence = [scheduled_procedure_step]

        # Continue adding the remaining fields directly to the identifier
        # identifier.RequestedProcedureID = instance.RequestedProcedureID
        # identifier.RequestedProcedureDescription = instance.RequestedProcedureDescription
        # identifier.SpecialNeeds = instance.SpecialNeeds
        
        # Pending
        yield (0xFF00, identifier)

# Implement the evt.EVT_N_CREATE handler
def handle_create(event):
    requestor = event.assoc.requestor
    timestamp = event.timestamp.strftime("%Y-%m-%d %H:%M:%S")
    addr, port = requestor.address, requestor.port
    # logger.info(f"Received C-FIND request from {addr}:{port} at {timestamp}")
    print(f"Received N-CREATE request from {addr}:{port} at {timestamp}")
    
    # model =event.request.AffectedSOPClassUID
    # print(model.keyword)
    
    # MPPS' N-CREATE request must have an *Affected SOP Instance UID*
    req = event.request
    print('Patient Name: ', event.attribute_list.PatientName)
    print('Performed Procedure Status: ',
          event.attribute_list.PerformedProcedureStepStatus)
    if req.AffectedSOPInstanceUID is None:
        # Failed - invalid attribute value
        return 0x0106, None

    # Can't create a duplicate SOP Instance
    if req.AffectedSOPInstanceUID in managed_instances:
        # Failed - duplicate SOP Instance
        return 0x0111, None

    # The N-CREATE request's *Attribute List* dataset
    attr_list = event.attribute_list

    # Performed Procedure Step Status must be 'IN PROGRESS'
    if "PerformedProcedureStepStatus" not in attr_list:
        # Failed - missing attribute
        return 0x0120, None
    if attr_list.PerformedProcedureStepStatus.upper() != 'IN PROGRESS':
        return 0x0106, None

    # Skip other tests...

    # Create a Modality Performed Procedure Step SOP Class Instance
    #   DICOM Standard, Part 3, Annex B.17
    ds = Dataset()

    # Add the SOP Common module elements (Annex C.12.1)
    ds.SOPClassUID = ModalityPerformedProcedureStep
    ds.SOPInstanceUID = req.AffectedSOPInstanceUID
    print('SOP Instance UID: ', ds.SOPInstanceUID)  

    # Update with the requested attributes
    ds.update(attr_list)

    # Add the dataset to the managed SOP Instances
    managed_instances[ds.SOPInstanceUID] = ds
    
    print('===============================================')
    print(managed_instances)
    print('===============================================')

    # Return status, dataset
    return 0x0000, ds

# Implement the evt.EVT_N_SET handler
def handle_set(event):
    req = event.request
    requestor = event.assoc.requestor
    timestamp = event.timestamp.strftime("%Y-%m-%d %H:%M:%S")
    addr, port = requestor.address, requestor.port
    # logger.info(f"Received C-FIND request from {addr}:{port} at {timestamp}")
    print(f"Received N-SET request from {addr}:{port} at {timestamp}")
    print('SOP Instance UID: ', req.RequestedSOPInstanceUID)

    
    if req.RequestedSOPInstanceUID not in managed_instances:
        print('SOP Instance not recognised')
        # Failure - SOP Instance not recognised
        return 0x0112, None

    ds = managed_instances[req.RequestedSOPInstanceUID]

    # The N-SET request's *Modification List* dataset
    mod_list = event.attribute_list

    # Skip other tests...

    ds.update(mod_list)
    print('Patient Name: ', event.attribute_list)
    
    # # Convert the dataset to JSON
    # json_payload = ds.to_json()

    # # Send the JSON payload to the server
    # url = "http://your-server-url.com/endpoint"  # Replace with your server URL
    # headers = {'Content-Type': 'application/json'}
    # response = requests.post(url, data=json_payload, headers=headers)
    # # Check response from the server
    # if response.status_code == 200:
    #     print('Successfully sent dataset to server.')
    # else:
    #     print(
    #         f'Failed to send dataset to server. Status code: {response.status_code}')

    # Return success status and updated dataset
    return 0x0000, ds

    # Return status, dataset
    return 0x0000, ds
