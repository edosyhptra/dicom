from pydicom.dataset import Dataset
# import requests

from pynetdicom.sop_class import ModalityPerformedProcedureStep
from db import add_instance, search, InvalidIdentifier, Instance
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

managed_instances = {}

# Implement the handler for evt.EVT_C_FIND
def handle_find(event, db_path, cli_config):
    """Handler for evt.EVT_C_FIND.

    Parameters
    ----------
    event : pynetdicom.events.Event
        The C-FIND request :class:`~pynetdicom.events.Event`.
    db_path : str
        The database path to use with create_engine().
    cli_config : dict
        A :class:`dict` containing configuration settings passed via CLI.
    logger : logging.Logger
        The application's logger.

    Yields
    ------
    int or pydicom.dataset.Dataset, pydicom.dataset.Dataset or None
        The C-FIND response's *Status* and if the *Status* is pending then
        the dataset to be sent, otherwise ``None``.
    """
    requestor = event.assoc.requestor
    timestamp = event.timestamp.strftime("%Y-%m-%d %H:%M:%S")
    addr, port = requestor.address, requestor.port
    # logger.info(f"Received C-FIND request from {addr}:{port} at {timestamp}")
    print(f"Received C-FIND request from {addr}:{port} at {timestamp}")

    model = event.request.AffectedSOPClassUID
    print(model)

    if model.keyword in (
        "UnifiedProcedureStepPull",
        "ModalityWorklistInformationModelFind",
    ):
        yield 0x0000, None
    else:
        engine = create_engine(db_path)
        with engine.connect() as conn:  # noqa: F841
            Session = sessionmaker(bind=engine)
            session = Session()
            # Search database using Identifier as the query
            try:
                matches = search(model, event.identifier, session)

            except InvalidIdentifier as exc:
                session.rollback()
                # logger.error("Invalid C-FIND Identifier received")
                # logger.error(str(exc))
                print("Invalid C-FIND Identifier received")
                print(str(exc))
                yield 0xA900, None
                return
            except Exception as exc:
                session.rollback()
                # logger.error("Exception occurred while querying database")
                # logger.exception(exc)
                print("Exception occurred while querying database")
                print(exc)
                yield 0xC320, None
                return
            finally:
                session.close()

        # Yield results
        for match in matches:
            print('============')
            print(match)
            if event.is_cancelled:
                yield 0xFE00, None
                return

            try:
                response = match.as_identifier(event.identifier, model)
                response.RetrieveAETitle = event.assoc.ae.ae_title
            except Exception as exc:
                # logger.error("Error creating response Identifier")
                # logger.exception(exc)
                print("Error creating response Identifier")
                print(exc)
                yield 0xC322, None

            yield 0xFF00, response
         
# def handle_find2(event):
#     """Handle a C-FIND request event."""
#     requestor = event.assoc.requestor
#     req = event.request
#     model =event.request.AffectedSOPClassUID
#     timestamp = event.timestamp.strftime("%Y-%m-%d %H:%M:%S")
#     addr, port = requestor.address, requestor.port
#     # logger.info(f"Received C-FIND request from {addr}:{port} at {timestamp}")
#     print(f"Received C-FIND request from {addr}:{port} at {timestamp}")
    
#     ds = event.identifier
#     item = ds.ScheduledStepAttributesSequence
#     # print(item[0].ScheduledProcedureStepStartDate)
    
#     if 'ScheduledStepAttributesSequence' not in ds:
#         # Failure
#         yield 0xC000, None
#         return
    
#     for uid, instance in managed_instances.items():
#         ScheduleStep = instance.get('ScheduledStepAttributesSequence')
#         matching = [
#             inst for inst in ScheduleStep if inst.ScheduledProcedureStepStartDate == item[0].ScheduledProcedureStepStartDate
#         ]
    
#     for instance in matching:
#         # Check if C-CANCEL has been received
#         if event.is_cancelled:
#              yield (0xFE00, None)
#              return

#         identifier = Dataset()
#         identifier.ScheduledStepAttributesSequence = [Dataset()]
#         item = identifier.ScheduledStepAttributesSequence
#         # item.ScheduledStationAETitle = 'CTSCANNER'
#         item[0].ScheduledProcedureStepStartDate = instance.ScheduledProcedureStepStartDate

#         # Pending
#         yield (0xFF00, identifier)

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
