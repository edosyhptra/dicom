from pydicom.dataset import Dataset

from pynetdicom import AE, evt
from pynetdicom.sop_class import ModalityPerformedProcedureStep, ModalityWorklistInformationFind
import handlers


handlers = [(evt.EVT_N_CREATE, handlers.handle_create), 
            (evt.EVT_N_SET, handlers.handle_set),
            (evt.EVT_C_FIND, handlers.handle_find)]

# Initialise the Application Entity and specify the listen port
ae = AE(
    ae_title='admin-scp'
)

# Add the supported presentation context
ae.add_supported_context(ModalityPerformedProcedureStep)
ae.add_supported_context(ModalityWorklistInformationFind)

# Start listening for incoming association requests
ae.start_server(("127.0.0.1", 1234), evt_handlers=handlers)
