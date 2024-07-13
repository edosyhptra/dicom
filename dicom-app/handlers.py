from pydicom.dataset import Dataset
import requests
import json
import os

from pynetdicom.sop_class import ModalityPerformedProcedureStep

managed_instances = {}
json_file_path = 'dummy-data/data1.json'

# Function to load instance to JSON
def dicom_to_json_ncreate(ds):
    json_data = {
        'SOPInstanceUID': ds.SOPInstanceUID,
        'PatientID': ds.PatientID,
        'PatientName': ds.PatientName.alphabetic,
        'PatientBirthDate': ds.PatientBirthDate,
        'PatientSex': ds.PatientSex,
        'StudyID': ds.StudyID,
        'PerformedProcedureStepID': ds.PerformedProcedureStepID,
        'PerformedStationAETitle': ds.PerformedStationAETitle,
        'PerformedStationName': ds.PerformedStationName,
        'PerformedLocation': ds.PerformedLocation,
        'PerformedProcedureStepStartDate': ds.PerformedProcedureStepStartDate,
        'PerformedProcedureStepStartTime': ds.PerformedProcedureStepStartTime,
        'PerformedProcedureStepStatus': ds.PerformedProcedureStepStatus,
        'PerformedProcedureStepDescription': ds.PerformedProcedureStepDescription,
        'PerformedProcedureTypeDescription': ds.PerformedProcedureTypeDescription,
        'PerformedProcedureCodeSequence': ds.PerformedProcedureCodeSequence,
        'PerformedProcedureStepEndDate': ds.PerformedProcedureStepEndDate,
        'PerformedProcedureStepEndTime': ds.PerformedProcedureStepEndTime
    }

    return json_data

# Function to load JSON data and convert it to a Dataset


def load_worklist_from_json(json_data):
    ds = Dataset()
    ds.PatientID = json_data.get('PatientID', '')
    ds.PatientName = json_data.get('PatientName', '')
    ds.PatientBirthDate = json_data.get('PatientBirthDate', '')
    ds.PatientSex = json_data.get('PatientSex', '')
    ds.PatientWeight = json_data.get('PatientWeight', '')
    ds.StudyID = json_data.get('StudyID', '')
    ds.StudyInstanceUID = json_data.get('StudyInstanceUID', '')
    ds.ScheduledProcedureStepID = json_data.get('ScheduledProcedureStepID', '')
    ds.AccessionNumber = json_data.get('AccessionNumber', '')
    ds.ReferringPhysicianName = json_data.get('ReferringPhysician', '')
    ds.StudyDescription = json_data.get('StudyDescription', '')
    
    # N-CREATE
    ds.SOPClassUID = json_data.get('SOPClassUID', '')
    ds.SOPInstanceUID = json_data.get('SOPInstanceUID', '')
    ds.PerformedProcedureStepStatus = json_data.get(
        'PerformedProcedureStepStatus', '')
    
    # N-SET
    ds.PerformedProcedureStepEndDate = json_data.get(
        'PerformedProcedureStepEndDate', '')
    ds.PerformedProcedureStepEndTime = json_data.get(
        'PerformedProcedureStepEndTime ', '')
    ds.PerformedProcedureStepStatus = json_data.get(
        'PerformedProcedureStepStatus', '')

    ds.ScheduledProcedureStepSequence = [Dataset()]
    scheduled_procedure_step = ds.ScheduledProcedureStepSequence[0]
    scheduled_procedure_step.ScheduledProcedureStepStartDate = json_data.get(
        'ScheduledProcedureStepStartDate', '')
    scheduled_procedure_step.Modality = json_data.get('Modality', '')
    scheduled_procedure_step.ScheduledStationAETitle = json_data.get('ScheduledStationAETitle', '')  # noqa: E501
    scheduled_procedure_step.ScheduledPerformingPhysicianName = json_data.get(
        'ScheduledPerformingPhysician', '')
    scheduled_procedure_step.ScheduledProcedureStepLocation = json_data.get(
        'ScheduledProcedureStepLocation', '')
    scheduled_procedure_step.PreMedication = json_data.get('PreMedication', '')

    ds.ScheduledProcedureStepSequence = [scheduled_procedure_step]
    ds.RequestedProcedureID = json_data.get('RequestedProcedureID', '')
    ds.RequestedProcedureDescription = json_data.get(
        'RequestedProcedureDescription', '')
    ds.SpecialNeeds = json_data.get('SpecialNeeds', '')

    return ds

def init_managed_instances(json_file_path):
    with open(json_file_path, 'r') as json_file:
        worklist_data = json.load(json_file)
    
    update_managed_instances(worklist_data)

def update_managed_instances(data):
    for i in range(len(data)):
        # Convert JSON data to Dataset
        ds = load_worklist_from_json(data[i])
        managed_instances[i] = ds
        # Assign the dataset to managed_instances[0]
        print('=====================')
        print(managed_instances[i])
        print('=====================')

def save_data(json_file_path, patient_data):
    if os.path.exists(json_file_path):
        # Read the existing data from the file
        with open(json_file_path, 'r') as json_file:
            worklist_data = json.load(json_file)
            
        # Create a list of StudyIDs in the worklist_data
        worklist_study_ids = {entry['StudyID'] for entry in worklist_data}

        # Check for duplicate StudyID
        patient_data = [
            entry for entry in patient_data if entry['StudyID'] not in worklist_study_ids]
        
        if not patient_data:
            return 200
        else:
            # Update JSON file
            for i in range(len(patient_data)):
                worklist_data.append(patient_data[i])
            with open(json_file_path, 'w') as json_file:
                json.dump(worklist_data, json_file, indent=4)

            update_managed_instances(worklist_data)

        return 200

    else:
        # If the directory doesn't exist, create a new one
        os.makedirs(os.path.dirname(json_file_path), exist_ok=True)
        with open(json_file_path, 'w') as json_file:
            json.dump(patient_data, json_file)
            
        update_managed_instances(patient_data)
        
        return 200
    
def handle_echo(event):
    """Handle a ECHO request event."""
    requestor = event.assoc.requestorr
    timestamp = event.timestamp.strftime("%Y-%m-%d %H:%M:%S")
    addr, port = requestor.address, requestor.port
    # logger.info(f"Received C-FIND request from {addr}:{port} at {timestamp}")
    
    print(f"Received ECHO request from {addr}:{port} at {timestamp}")
    
    return 0x0000
    

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

    for uid, found in managed_instances.items():
        ScheduledProcedure = found.get('ScheduledProcedureStepSequence')
        # check = []
        check = [
            inst for inst in ScheduledProcedure if inst.ScheduledStationAETitle == ae_title  # noqa: E501
        ]
        
        if check:
            matching.append(found)
            
    
    for instance in matching:
        # Check if C-CANCEL has been received
        if event.is_cancelled:
             yield (0xFE00, None)
             return
        
        # Create the identifier dataset
        identifier = Dataset()
        # identifier.Modality = instance.Modality
        # identifier.RequestedContrastAgent = ''
        identifier.PatientName = instance.PatientName
        identifier.PatientID = instance.PatientID
        identifier.StudyID = instance.StudyID
        identifier.PatientBirthDate = instance.PatientBirthDate
        identifier.PatientSex = instance.PatientSex
        identifier.PatientWeight = instance.PatientWeight
        
        # is it from the dicom or the app?
        identifier.StudyInstanceUID = '987111' 
        
        # Create the ScheduledProcedureStepSequence dataset
        # scheduled_procedure_step = Dataset()
        # scheduled_procedure_step.ScheduledProcedureStepID = '112'
        # scheduled_procedure_step.ScheduledStationAETitle = instance.ScheduledStationAETitle
        # scheduled_procedure_step.ScheduledProcedureStepStartDate = instance.ScheduledProcedureStepStartDate
        # scheduled_procedure_step.ScheduledProcedureStepStartTime = '000000'
        # scheduled_procedure_step.ScheduledProcedureStepEndDate = ''
        # scheduled_procedure_step.ScheduledProcedureStepEndTime = ''
        # scheduled_procedure_step.ScheduledPerformingPhysicianName = instance.ScheduledPerformingPhysicianName
        # scheduled_procedure_step.ScheduledProcedureStepDescription = 'Test procedure'
        # scheduled_procedure_step = identifier.ScheduledProcedureCodeSequence[0]
        # scheduled_procedure_step.ScheduledStationName = 'Test Station'
        # scheduled_procedure_step.ScheduledProcedureStepLocation = instance.ScheduledProcedureStepLocation
        # scheduled_procedure_step.PreMedication = instance.PreMedication
        # scheduled_procedure_step.ScheduledProcedureStepStatus = ''
        # scheduled_procedure_step.CommentsOnTheScheduledProcedure = ''

        # Add the ScheduledProcedureStepSequence to the identifier
        # identifier.ScheduledProcedureStepSequence = [scheduled_procedure_step]
        
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
    
    for i in range(len(managed_instances)):
        if req.AffectedSOPInstanceUID == managed_instances[i].SOPInstanceUID:
            # Failed - duplicate SOP Instance
            return 0x0111, None
    
    reqID = event.attribute_list.ScheduledStepAttributesSequence._list[
        0].ScheduledProcedureStepID
    index = 0

    # Get corresponding ScheduledProcedureStepID
    for i in range(len(managed_instances.items())):
        if reqID == managed_instances[i].ScheduledProcedureStepID:
            index = i
            break
    
    attr_list = event.attribute_list
    ds = Dataset()
    
    # Add the SOP Common module elements (Annex C.12.1)
    ds.SOPClassUID = ModalityPerformedProcedureStep
    ds.SOPInstanceUID = req.AffectedSOPInstanceUID

    # Update with the requested attributes
    ds.update(attr_list)

    # Add the dataset to the managed SOP Instances
    managed_instances[index].SOPClassUID = ModalityPerformedProcedureStep
    managed_instances[index].SOPInstanceUID = req.AffectedSOPInstanceUID
    managed_instances[index].PerformedProcedureStepStatus = event._decoded.PerformedProcedureStepStatus
    
    # Updata database
    if os.path.exists(json_file_path):
        # Read the existing data from the file
        with open(json_file_path, 'r') as json_file:
            worklist_data = json.load(json_file)
            
        worklist_data[index]["SOPClassUID"] = ModalityPerformedProcedureStep
        worklist_data[index]["SOPInstanceUID"] = req.AffectedSOPInstanceUID
        worklist_data[index]["PerformedProcedureStepStatus"] = event._decoded.PerformedProcedureStepStatus
        
        with open(json_file_path, 'w') as json_file:
            json.dump(worklist_data, json_file, indent=4)
          
    # found = []
    # for index in range(len(managed_instances.items())):
    #     patientName = managed_instances[index].PatientName
    #     modality = managed_instances[0].ScheduledProcedureStepSequence._list[0].Modality    # noqa: E501
           
    #     if patientName == attr_list.PatientName and modality == attr_list.Modality:
    #         found.append(patientName)
        
    #     if found: 
    #         # Create a Modality Performed Procedure Step SOP Class Instance
    #         #   DICOM Standard, Part 3, Annex B.17
    #         ds = Dataset()

    #         # Add the SOP Common module elements (Annex C.12.1)
    #         ds.SOPClassUID = ModalityPerformedProcedureStep
    #         ds.SOPInstanceUID = req.AffectedSOPInstanceUID

    #         # Update with the requested attributes
    #         ds.update(attr_list)

    #         # Add the dataset to the managed SOP Instances
    #         managed_instances[index] = ds
    #         print('===============================================')
    #         # print(managed_instances[index])
    #         print(type(managed_instances[index]))
    #         print(managed_instances[index].to_json())
    #         json_file_path = 'dummy-data/data1.json'
    #         # update_managed_instances(json_file_path, managed_instances[index])
    #         print('===============================================')
            
    #         # The URL of the HTTP endpoint you want to send the data to
    #         url = "http://10.20.186.205:8000/api/status"
            
    #         # # json_string = json.dumps(managed_instances[index], indent=4)
    #         # # print(json_string)
    #         data = dicom_to_json_ncreate(managed_instances[index])
    #         # data = data.to_json_dict()
    #         # print(data['PatientName'])
            
    #         # # # Sending the data as a JSON payload
    #         response = requests.post(url, data=data)

    #         # Checking the response status
    #         if response.status_code == 200:
    #             print("Data sent successfully!")
    #         else:
    #             print(f"Failed to send data. Status code: {response.status_code}")
                        
    #         break
        
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
    index = 0
    
    for i in range(len(managed_instances)):
        if req.RequestedSOPInstanceUID == managed_instances[i].SOPInstanceUID:
            index = i
        else:
            # Failure - SOP Instance not recognised
            return 0x0112, None
    
    # ds = managed_instances[req.RequestedSOPInstanceUID]
    ds = managed_instances[index]

    # The N-SET request's *Modification List* dataset
    mod_list = event.attribute_list
    ds.update(mod_list)
    
    if 'PerformedProcedureStepStatus' in mod_list:
        # Update database
        if os.path.exists(json_file_path):
            # Read the existing data from the file
            with open(json_file_path, 'r') as json_file:
                worklist_data = json.load(json_file)

            worklist_data[index]["PerformedProcedureStepStatus"] = mod_list.PerformedProcedureStepStatus  # noqa: E501
            worklist_data[index]["PerformedProcedureStepEndDate"] = mod_list.PerformedProcedureStepEndDate  # noqa: E501
            worklist_data[index]["PerformedProcedureStepEndTime"] = mod_list.PerformedProcedureStepEndTime  # noqa: E501

            with open(json_file_path, 'w') as json_file:
                json.dump(worklist_data, json_file, indent=4)
                
        return 0x0000, ds
    
    # Skip other tests...
    
    # url = "http://10.20.186.205:8000/api/status"

    
    # data = dicom_to_json(ds)
    # data = data.to_json_dict()
    # print(type(data))

    # Sending the data as a JSON payload
    # response = requests.post(url, data=data)

    # Checking the response status
    # if response.status_code == 200:
    #     print("Data sent successfully!")
    # else:
    #     print(f"Failed to send data. Status code: {response.status_code}")

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