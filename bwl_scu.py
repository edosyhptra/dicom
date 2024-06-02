from pydicom.dataset import Dataset

from pynetdicom import AE, debug_logger
from pynetdicom.sop_class import ModalityWorklistInformationFind, PatientRootQueryRetrieveInformationModelFind

debug_logger()

# Initialise the Application Entity
ae = AE()

# Add a requested presentation context
# ae.add_requested_context(ModalityWorklistInformationFind)
ae.add_requested_context(PatientRootQueryRetrieveInformationModelFind)

# Create our Identifier (query) dataset
ds = Dataset()
ds.PatientName = 'CITIZEN^Jan'
ds.QueryRetrieveLevel = 'PATIENT'
# # Create our Identifier (query) dataset
# ds = Dataset()
# ds.PatientName = 'Edo'
# ds.QueryRetrieveLevel = 'PATIENT'
# ds.ScheduledProcedureStepSequence = [Dataset()]
# item = ds.ScheduledProcedureStepSequence[0]
# item.ScheduledStationAETitle = 'CTSCANNER'
# item.ScheduledProcedureStepStartDate = '20040119'
# item.Modality = 'CT'

# Associate with peer AE at IP 127.0.0.1 and port 11112
assoc = ae.associate("localhost", 1234)
# assoc = ae.associate("127.0.0.1", 11112)

if assoc.is_established:
    # Use the C-FIND service to send the identifier
    responses = assoc.send_c_find(ds, ModalityWorklistInformationFind)
    for (status, identifier) in responses:
        if status:
            print('C-FIND query status: 0x{0:04x}'.format(status.Status))
        else:
            print('Connection timed out, was aborted or received invalid response')

    # Release the association
    assoc.release()
else:
    print('Association rejected, aborted or never connected')
