from pydicom.dataset import Dataset

from pynetdicom import AE, evt
from pynetdicom.sop_class import ModalityPerformedProcedureStep
import mpps_handlers


handlers = [(evt.EVT_N_CREATE, mpps_handlers.handle_create), 
            (evt.EVT_N_SET, mpps_handlers.handle_set)]

# Initialise the Application Entity and specify the listen port
ae = AE(
    ae_title='admin-scp'
)

# Add the supported presentation context
ae.add_supported_context(ModalityPerformedProcedureStep)

# Start listening for incoming association requests
ae.start_server(("127.0.0.1", 1234), evt_handlers=handlers)
