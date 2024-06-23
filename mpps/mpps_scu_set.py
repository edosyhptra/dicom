from pydicom.dataset import Dataset
from pydicom.uid import generate_uid

from pynetdicom import AE, debug_logger
from pynetdicom.sop_class import (
    ModalityPerformedProcedureStep,
    CTImageStorage
)
from pynetdicom.status import code_to_category

# Continuing on from the previous example...
# Modality performs the procedure, update the MPPS SCP
# In performing the procedure a series with ten CT Image Storage
# SOP Instances is generated
ct_series_uid = generate_uid()
ct_instance_uids = [generate_uid() for ii in range(10)]
ct_study_uid = generate_uid()
mpps_instance_uid = generate_uid()
# Our N-SET *Modification List*


def build_mod_list(series_instance, sop_instances):
    ds = Dataset()
    ds.PerformedSeriesSequence = [Dataset()]

    series_seq = ds.PerformedSeriesSequence
    series_seq[0].PerformingPhysicianName = None
    series_seq[0].ProtocolName = "Some protocol"
    # series_seq[0].OperatorName = None
    series_seq[0].SeriesInstanceUID = series_instance
    series_seq[0].SeriesDescription = "some description"
    series_seq[0].RetrieveAETitle = None
    series_seq[0].ReferencedImageSequence = []

    img_seq = series_seq[0].ReferencedImageSequence
    for uid in sop_instances:
        img_ds = Dataset()
        img_ds.ReferencedSOPClassUID = CTImageStorage
        img_ds.ReferencedSOPInstanceUID = uid
        img_seq.append(img_ds)

    series_seq[0].ReferencedNonImageCompositeSOPInstanceSequence = []

    return ds


# Our final N-SET *Modification List*
final_ds = Dataset()
final_ds.PerformedProcedureStepStatus = "COMPLETED"
final_ds.PerformedProcedureStepEndDate = "20000101"
final_ds.PerformedProcedureStepEndTime = "1300"


# Initialise the Application Entity
ae = AE()

# Add a requested presentation context
ae.add_requested_context(ModalityPerformedProcedureStep)

# Associate with peer again
assoc = ae.associate("127.0.0.1", 1234)

if assoc.is_established:
    # Use the N-SET service to update the SOP Instance
    status, attr_list = assoc.send_n_set(
        build_mod_list(ct_series_uid, ct_instance_uids),
        ModalityPerformedProcedureStep,
        mpps_instance_uid
    )

    if status:
        print('N-SET request status: 0x{0:04x}'.format(status.Status))
        category = code_to_category(status.Status)
        if category in ['Warning', 'Success']:
            # Send completion
            status, attr_list = assoc.send_n_set(
                final_ds,
                ModalityPerformedProcedureStep,
                mpps_instance_uid
            )
            if status:
                print(
                    'Final N-SET request status: 0x{0:04x}'.format(status.Status))
    else:
        print('Connection timed out, was aborted or received invalid response')

    assoc.release()
