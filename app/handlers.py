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

