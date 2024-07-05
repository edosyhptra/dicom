import json
from pydicom.dataset import Dataset
from pydicom.uid import CTImageStorage


def build_mod_list(series_instance, sop_instances):
    ds = Dataset()
    ds.PerformedSeriesSequence = [Dataset()]

    series_seq = ds.PerformedSeriesSequence
    series_seq[0].PerformingPhysicianName = "Dr. Agung"
    series_seq[0].ProtocolName = "Some protocol"
    # series_seq[0].OperatorName = None
    series_seq[0].SeriesInstanceUID = series_instance
    series_seq[0].SeriesDescription = "some description"
    series_seq[0].RetrieveAETitle = "dicom1"
    series_seq[0].ReferencedImageSequence = []

    img_seq = series_seq[0].ReferencedImageSequence
    for uid in sop_instances:
        img_ds = Dataset()
        img_ds.ReferencedSOPClassUID = CTImageStorage
        img_ds.ReferencedSOPInstanceUID = uid
        img_seq.append(img_ds)

    series_seq[0].ReferencedNonImageCompositeSOPInstanceSequence = []

    return ds

def dicom_to_mod_list_json(ds):
    mod_list_json = {
        'series_instance': ds.PerformedSeriesSequence[0].SeriesInstanceUID,
        'sop_instances': []
    }

    for img_ds in ds.PerformedSeriesSequence[0].ReferencedImageSequence:
        mod_list_json['sop_instances'].append(img_ds.ReferencedSOPInstanceUID)

    return mod_list_json

# Example usage:
series_instance = '1.2.3.4.5'
sop_instances = ['1.2.3.4.5.1', '1.2.3.4.5.2', '1.2.3.4.5.3']

ds = build_mod_list(series_instance, sop_instances)
mod_list_json = dicom_to_mod_list_json(ds)
print(json.dumps(mod_list_json, indent=2))