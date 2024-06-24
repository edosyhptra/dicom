from pydicom.dataset import Dataset

from pynetdicom.sop_class import ModalityPerformedProcedureStep

managed_instances = {}

# Implement the handler for evt.EVT_C_FIND
def handle_find(event):
    """Handle a C-FIND request event."""
    requestor = event.assoc.requestor
    req = event.request
    model =event.request.AffectedSOPClassUID
    timestamp = event.timestamp.strftime("%Y-%m-%d %H:%M:%S")
    addr, port = requestor.address, requestor.port
    # logger.info(f"Received C-FIND request from {addr}:{port} at {timestamp}")
    print(f"Received C-FIND request from {addr}:{port} at {timestamp}")
    
    ds = event.identifier
    item = ds.ScheduledStepAttributesSequence
    # print(item[0].ScheduledProcedureStepStartDate)
    
    if 'ScheduledStepAttributesSequence' not in ds:
        # Failure
        yield 0xC000, None
        return
    
    for uid, instance in managed_instances.items():
        ScheduleStep = instance.get('ScheduledStepAttributesSequence')
        matching = [
            inst for inst in ScheduleStep if inst.ScheduledProcedureStepStartDate == item[0].ScheduledProcedureStepStartDate
        ]
    
    for instance in matching:
        # Check if C-CANCEL has been received
        if event.is_cancelled:
             yield (0xFE00, None)
             return

        identifier = Dataset()
        identifier.ScheduledStepAttributesSequence = [Dataset()]
        item = identifier.ScheduledStepAttributesSequence
        # item.ScheduledStationAETitle = 'CTSCANNER'
        item[0].ScheduledProcedureStepStartDate = instance.ScheduledProcedureStepStartDate

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

    # Return status, dataset
    return 0x0000, ds
