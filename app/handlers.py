import os
from pydicom import dcmread
from pydicom.dataset import Dataset
from pynetdicom.sop_class import ModalityPerformedProcedureStep

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from db import add_instance, search, InvalidIdentifier, Instance

managed_instances = {}

# debug_logger()
def handle_echo(event):
    """Handler for evt.EVT_C_ECHO.

    Parameters
    ----------
    event : events.Event
        The corresponding event.
    cli_config : dict
        A :class:`dict` containing configuration settings passed via CLI.
    logger : logging.Logger
        The application's logger.

    Returns
    -------
    int
        The status of the C-ECHO operation, always ``0x0000`` (Success).
    """
    requestor = event.assoc.requestor
    timestamp = event.timestamp.strftime("%Y-%m-%d %H:%M:%S")
    addr, port = requestor.address, requestor.port
    print(f"Received C-ECHO request from {addr}:{port} at {timestamp}")

    return 0x0000

# Implement the evt.EVT_N_CREATE handler


def handle_create(event):
    # MPPS' N-CREATE request must have an *Affected SOP Instance UID*
    req = event.request
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

    # Update with the requested attributes
    ds.update(attr_list)

    # Add the dataset to the managed SOP Instances
    managed_instances[ds.SOPInstanceUID] = ds

    # Return status, dataset
    return 0x0000, ds
    
# Implement the evt.EVT_N_SET handler
def handle_set(event):
    req = event.request
    if req.RequestedSOPInstanceUID not in managed_instances:
        # Failure - SOP Instance not recognised
        return 0x0112, None

    ds = managed_instances[req.RequestedSOPInstanceUID]

    # The N-SET request's *Modification List* dataset
    mod_list = event.attribute_list

    # Skip other tests...

    ds.update(mod_list)

    # Return status, dataset
    return 0x0000, ds

# def handle_create(event, db_path, cli_config):
#     # MPPS' N-CREATE request must have an *Affected SOP Instance UID*
#     requestor = event.assoc.requestor
#     timestamp = event.timestamp.strftime("%Y-%m-%d %H:%M:%S")
#     addr, port = requestor.address, requestor.port
#     # logger.info(f"Received N-CREATE request from {addr}:{port} at {timestamp}")
#     print(f"Received N-CREATE request from {addr}:{port} at {timestamp}")
    
#     req = event.request
#     print('what is AffectedSOPInstance: ', req.AffectedSOPInstanceUID)
#     if req.AffectedSOPInstanceUID is None:
#         # Failed - invalid attribute value
#         return 0x0106, None
#     else:
#         # engine = create_engine(db_path)
#         # with engine.connect() as conn:
#         #     Session = sessionmaker(bind=engine)
#         #     session = Session()
#         #     # Can't create a duplicate SOP Instance
#         #     try:
#         #         query = text(
#         #             'SELECT COUNT(*) FROM sop_instances WHERE sop_instance_uid = :uid')
#         #         existing_instance = session.execute(
#         #             query, {'uid': req.AffectedSOPInstanceUID}).scalar()
#         #     except Exception as exc:
#         #         session.rollback()
#         #         # logger.error("Exception occurred while querying database")
#         #         # logger.exception(exc)
#         #         print("Exception occurred while querying database")
#         #         print(exc)
#         #         yield 0xC320, None
#         #         return
#         #     finally:
#         #         session.close()
#         engine = create_engine(db_path)
#         with engine.connect() as conn:
#             Session = sessionmaker(bind=engine)
#             session = Session()
#         # # Yield results
#         # if existing_instance > 0:
#         #     # Failed - duplicate SOP Instance
#         #     yield 0x0111, None
#         #     return

#             attr_list = event.attribute_list
#             # Performed Procedure Step Status must be 'IN PROGRESS'
#             if "PerformedProcedureStepStatus" not in attr_list:
#                 # Failed - missing attribute
#                 yield 0x0120, None
#                 return
#             if attr_list.PerformedProcedureStepStatus.upper() != 'IN PROGRESS':
#                 yield 0x0106, None
#                 return

#             ds = Dataset()

#             # Add the SOP Common module elements (Annex C.12.1)
#             ds.SOPClassUID = ModalityPerformedProcedureStep
#             ds.SOPInstanceUID = req.AffectedSOPInstanceUID

#             # Update with the requested attributes
#             ds.update(attr_list)
#             print('=========================add instance...')
#             add_instance(ds, session)
#             print('=========================setelah add instance...')
#             session.commit()
        
#         return 0x0000, ds
            
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

