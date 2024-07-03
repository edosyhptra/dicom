from pydicom.dataset import Dataset
import requests
import json

from pynetdicom.sop_class import ModalityPerformedProcedureStep

managed_instances = {}

# Function to load JSON data and convert it to a Dataset
def load_worklist_from_json(json_data):
    ds = Dataset()
    ds.PatientID = json_data['PatientID']
    ds.PatientName = json_data['PatientName']
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
    scheduled_procedure_step.ScheduledStationAETitle = json_data['ScheduledStationAETitle']  # noqa: E501
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
    
def save_into_managed_instances(json_file_path, patient_data):
    """Save the JSON file data into the managed_instances dictionary."""
    with open(json_file_path, 'r') as json_file:
        worklist_data = json.load(json_file)
        
    # Convert JSON data to Dataset
    for i in range(len(worklist_data)):
        ds = load_worklist_from_json(worklist_data[i])
        managed_instances[i] = ds
        # Assign the dataset to managed_instances[0]
        # Assuming managed_instances is a list with at least one element
        print('=====================')
        print(managed_instances[i])
        print('=====================')

    # Print out the dataset to verify
    # print(managed_instances[0])

def handle_find(event):
    """Handle a C-FIND request event."""
    requestor = event.assoc.requestor
    ds = event.identifier
    timestamp = event.timestamp.strftime("%Y-%m-%d %H:%M:%S")
    addr, port = requestor.address, requestor.port
    # logger.info(f"Received C-FIND request from {addr}:{port} at {timestamp}")
    print(f"Received C-FIND request from {addr}:{port} at {timestamp}")
    
    if 'ScheduledProcedureStepSequence' not in ds:
        # Failure invalid request
        yield 0xC000, None
    
    item = ds.ScheduledProcedureStepSequence
    ae_title = item[0].ScheduledStationAETitle
    
    matching = []

    for uid, instance in managed_instances.items():
        ScheduledProcedure = instance.get('ScheduledProcedureStepSequence')
        
        found = [
            inst for inst in ScheduledProcedure if inst.ScheduledStationAETitle == ae_title  # noqa: E501
        ]
        
        if found:
            matching = found
            patientName = instance.PatientName
            
    
    for instance in matching:
        # Check if C-CANCEL has been received
        if event.is_cancelled:
             yield (0xFE00, None)
             return
        
        # Create the identifier dataset
        identifier = Dataset()
        identifier.PatientName = patientName
        
        # Create the ScheduledProcedureStepSequence dataset
        identifier.ScheduledProcedureStepSequence = [Dataset()]
        scheduled_procedure_step = identifier.ScheduledProcedureStepSequence[0]
        scheduled_procedure_step.ScheduledProcedureStepStartDate = instance.ScheduledProcedureStepStartDate  # noqa: E501
        scheduled_procedure_step.Modality = instance.Modality
        scheduled_procedure_step.ScheduledStationAETitle = instance.ScheduledStationAETitle  # noqa: E501
        scheduled_procedure_step.ScheduledPerformingPhysicianName = instance.ScheduledPerformingPhysicianName  # noqa: E501
        scheduled_procedure_step.ScheduledProcedureStepLocation = instance.ScheduledProcedureStepLocation  # noqa: E501
        scheduled_procedure_step.PreMedication = instance.PreMedication
        
        # Add the ScheduledProcedureStepSequence to the identifier
        identifier.ScheduledProcedureStepSequence = [scheduled_procedure_step]

        # Continue adding the remaining fields directly to the identifier
        # identifier.RequestedProcedureID = instance.RequestedProcedureID
        # identifier.RequestedProcedureDescription = instance.RequestedProcedureDescription  # noqa: E501
        # identifier.SpecialNeeds = instance.SpecialNeeds
        
        # Pending
        yield (0xFF00, identifier)

# Implement the evt.EVT_N_CREATE handler
def handle_create(event):
    requestor = event.assoc.requestor
    timestamp = event.timestamp.strftime("%Y-%m-%d %H:%M:%S")
    addr, port = requestor.address, requestor.port
    req = event.request
    # logger.info(f"Received C-FIND request from {addr}:{port} at {timestamp}")
    print(f"Received N-CREATE request from {addr}:{port} at {timestamp}")
    
    if req.AffectedSOPInstanceUID is None:
        # Failed - invalid attribute value
        return 0x0106, None
    
    # for i in range(len(managed_instances)):
    #     if req.AffectedSOPInstanceUID in managed_instances[i].SOPClassUID: 
    #         # Failed - duplicate SOP Instance
    #         print('Duplicate SOP Instance')
    #         return 0x0111, None
        
    if req.AffectedSOPInstanceUID in managed_instances:
        # Failed - duplicate SOP Instance
        return 0x0111, None
    
    attr_list = event.attribute_list
    
    found = []
    for index in range(len(managed_instances.items())):
        patientName = managed_instances[index].PatientName
        modality = managed_instances[0].ScheduledProcedureStepSequence._list[0].Modality    # noqa: E501
           
        if patientName == attr_list.PatientName and modality == attr_list.Modality:
            found.append(patientName)
        
        if found: 
            # Create a Modality Performed Procedure Step SOP Class Instance
            #   DICOM Standard, Part 3, Annex B.17
            ds = Dataset()

            # Add the SOP Common module elements (Annex C.12.1)
            ds.SOPClassUID = ModalityPerformedProcedureStep
            ds.SOPInstanceUID = req.AffectedSOPInstanceUID

            # Update with the requested attributes
            ds.update(attr_list)

            # Add the dataset to the managed SOP Instances
            managed_instances[index] = ds
            print('===============================================')
            print(managed_instances[index])
            print('===============================================')
            
            # # The URL of the HTTP endpoint you want to send the data to
            # url = "http://10.20.184.26:8000/api/status"
            
            # # json_string = json.dumps(managed_instances[index], indent=4)
            # # print(json_string)

            # # Sending the data as a JSON payload
            # response = requests.post(url, json=managed_instances[index])

            # # Checking the response status
            # if response.status_code == 200:
            #     print("Data sent successfully!")
            # else:
            #     print(f"Failed to send data. Status code: {response.status_code}")
                        
            break
    # print('===============================================')
    # print(managed_instances)
    # print('===============================================')

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

    # found = False 
    
    for i, (key, value) in enumerate(managed_instances.items()):
        print(managed_instances[i].SOPInstanceUID)
        if req.RequestedSOPInstanceUID == managed_instances[i].SOPInstanceUID:
            index = i
            found = True
            
            break
        
    if not found:
        print('SOP Instance not recognised')
        # Failure - SOP Instance not recognised
        return 0x0112, None
    
    # ds = managed_instances[req.RequestedSOPInstanceUID]
    ds = managed_instances[index]

    # The N-SET request's *Modification List* dataset
    mod_list = event.attribute_list

    # Skip other tests...

    ds.update(mod_list)
    # print('Patient Name: ', event.attribute_list)
    
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
