import os
from pydicom import dcmread
from pydicom.dataset import Dataset

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db import add_instance, search, InvalidIdentifier, Instance


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

# Implement the handler for evt.EVT_C_FIND


def handle_find(event, db_path, cli_config, logger):
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
    print('hello')
    logger.info(f"Received C-FIND request from {addr}:{port} at {timestamp}")

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
                logger.error("Invalid C-FIND Identifier received")
                logger.error(str(exc))
                yield 0xA900, None
                return
            except Exception as exc:
                session.rollback()
                logger.error("Exception occurred while querying database")
                logger.exception(exc)
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
                logger.error("Error creating response Identifier")
                logger.exception(exc)
                yield 0xC322, None

            yield 0xFF00, response
# def handle_find(event):
#     requestor = event.assoc.requestor
#     timestamp = event.timestamp.strftime("%Y-%m-%d %H:%M:%S")
#     addr, port = requestor.address, requestor.port
#     print(f"Received C-FIND request from {addr}:{port} at {timestamp}")
    
#     model = event.request.AffectedSOPClassUID
    
#     if model.keyword in (
#         "UnifiedProcedureStepPull",
#         "ModalityWorklistInformationModelFind",
#     ):
#         print('model: ', model.keyword)
#         print(event.identifier)
#         yield 0x0000, None
#     else:
#         try:
#             matches = search(model, event.identifier)
        
#         except InvalidIdentifier as exc:
#             print('Invalid C-FIND Identifier received')
#             print(str(exc))
            
#             yield 0x900, None
#             return
        
#         except Exception as exc:
#             print("Exception occurred while querying database")
#             # lexc)
#             print(exc)
#             yield 0xC320, None
            
#             return
        
#         for match in matches:
#             if event.is_cancelled:
#                 yield 0xFE00, None
#                 return
#             try:
#                 response = match.as_identifier(event.identifier, model)
#                 response.RetrieveAETitle = event.assoc.ae.ae_title
#             except Exception as exc:
#                 print("Error creating response Identifier")
#                 # logger.exception(exc)
#                 yield 0xC322, None

            
#             yield 0xFF00, response
#         # print('hello')
#         # print("request accepted")
        
#         yield 0xFF00, None
    
    
# def handle_find(event):
#    # Implement the handler for evt.EVT_C_FIND

# def handle_find(event):
#     """Handle a C-FIND request event."""
#     ds = event.identifier
    
#     print("Received C-FIND request")

#     # Import stored SOP Instances
#     # Import stored SOP Instances
#     instances = []
#     fdir = 'bwl/dataset/'
#     print(os.listdir(fdir))
#     for fpath in os.listdir(fdir):
#         instances.append(dcmread(os.path.join(fdir, fpath)))
#     # instances = []
#     # fdir = 'dataset/CT_small.dcm'
#     # instances.append(dcmread(fdir))
#     # # for fpath in os.listdir(fdir):
#     # #     instances.append(dcmread(os.path.join(fdir, fpath)))

#     if 'ScheduledProcedureStepSequence' not in ds:
#         print('failure')
#         # Failure
#         yield 0xC000, None
#         return

#     if 'ScheduledProcedureStepSequence' in ds:
#         if 'PatientName' in ds:
#             if ds.PatientName not in ['*', '', '?']:
#                 matching = [
#                     inst for inst in instances if inst.PatientName == ds.PatientName
#                 ]

#              # Skip the other possible values...

#          # Skip the other possible attributes...

#      # Skip the other QR levels...

#     for instance in matching:
#         # Check if C-CANCEL has been received
#         if event.is_cancelled:
#             yield (0xFE00, None)
#             print('cancelled')
#             return

#         identifier = Dataset()
#         identifier.PatientName = instance.PatientName
#         # identifier.QueryRetrieveLevel = ds.QueryRetrieveLevel

#         # Pending
#         yield (0xFF00, identifier)
