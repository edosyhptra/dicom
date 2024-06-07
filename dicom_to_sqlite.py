from pydicom import dcmread
from pydicom.dataset import Dataset

from app import db

from sqlalchemy import create_engine
from sqlalchemy.schema import MetaData
from sqlalchemy.exc import IntegrityError, SAWarning
from sqlalchemy.orm import sessionmaker
DATASETS = {
    "CTImageStorage.dcm": {
        "patient_id": "1CT1",
        "patient_name": "CompressedSamples^CT1",
        "study_instance_uid": "1.3.6.1.4.1.5962.1.2.1.20040119072730.12322",
        "study_date": "20040119",
        "study_time": "072730",
        "accession_number": None,
        "study_id": "1CT1",
        "series_instance_uid": "1.3.6.1.4.1.5962.1.3.1.1.20040119072730.12322",
        "modality": "CT",
        "series_number": "1",
        "sop_instance_uid": "1.3.6.1.4.1.5962.1.1.1.1.1.20040119072730.12322",
        "instance_number": "1",
        "transfer_syntax_uid": "1.2.840.10008.1.2.1",
        "sop_class_uid": "1.2.840.10008.5.1.4.1.1.2",
    }
}
# Connect database
engine = db.create(
    "sqlite:////Users/edosyahputra/Project/dicom/instances.sqlite")

# ds = Dataset()
# ds.PatientID = "1234"
# ds.StudyInstanceUID = "1.2"
# ds.SeriesInstanceUID = "1.2.3"
# ds.SOPInstanceUID = "1.2.3.4"
# minimal = ds

session = sessionmaker(bind=engine)()

# DATA_DIR = "app/data"
"""Test adding to the instance database."""
ds = dcmread("app/data/CTImageStorage.dcm")
# ds = dcmread("instances.sqlite")
db.add_instance(ds, session)

obj = session.query(db.Instance).all()

print(getattr(obj[0], "patient_name"))

session.commit()

# assert 1 == len(obj)
# for kk, vv in DATASETS["CTImageStorage.dcm"].items():
#     assert vv == getattr(obj[0], kk)
