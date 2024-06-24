from pydicom.dataset import Dataset

from pynetdicom import AE, debug_logger
from pynetdicom.sop_class import (
    PatientRootQueryRetrieveInformationModelFind, 
    ModalityWorklistInformationFind)

debug_logger()

ae = AE()
ae.add_requested_context(ModalityWorklistInformationFind)

# Create our Identifier (query) dataset
ds = Dataset()
ds.PatientName = '*'
ds.ScheduledStepAttributesSequence = [Dataset()]
item = ds.ScheduledStepAttributesSequence
# item.ScheduledStationAETitle = 'CTSCANNER'
item[0].ScheduledProcedureStepStartDate = '20181005'
item[0].Modality = 'CT'

# Associate with the peer AE at IP 127.0.0.1 and port 11112
assoc = ae.associate("127.0.0.1", 1234)
if assoc.is_established:
    # Send the C-FIND request
    responses = assoc.send_c_find(
        ds, ModalityWorklistInformationFind)
    for (status, identifier) in responses:
        if status:
            print('C-FIND query status: 0x{0:04X}'.format(status.Status))
        else:
            print('Connection timed out, was aborted or received invalid response')

    # Release the association
    assoc.release()
else:
    print('Association rejected, aborted or never connected')
