from collections import OrderedDict
import sys

try:
    from sqlalchemy import create_engine, Column, ForeignKey, Integer, String
except ImportError:
    sys.exit("qrscp requires the sqlalchemy package")

from sqlalchemy.orm import declarative_base

from pydicom.dataset import Dataset

from pynetdicom import build_context
from pynetdicom.sop_class import (
    PatientRootQueryRetrieveInformationModelFind,
    PatientRootQueryRetrieveInformationModelMove,
    PatientRootQueryRetrieveInformationModelGet,
    StudyRootQueryRetrieveInformationModelFind,
    StudyRootQueryRetrieveInformationModelMove,
    StudyRootQueryRetrieveInformationModelGet,
)

class InvalidIdentifier(Exception):
    pass


# Translate from the element keyword to the db attribute
_TRANSLATION = {
    "PatientID": "patient_id",  # PATIENT | Unique | VM 1 | LO
    "PatientName": "patient_name",  # PATIENT | Required | VM 1 | PN
    "StudyInstanceUID": "study_instance_uid",  # STUDY | Unique | VM 1 | UI
    "StudyDate": "study_date",  # STUDY | Required | VM 1 | DA
    "StudyTime": "study_time",  # STUDY | Required | VM 1 | TM
    "AccessionNumber": "accession_number",  # STUDY | Required | VM 1 | SH
    "StudyID": "study_id",  # STUDY | Required | VM 1 | SH
    "SeriesInstanceUID": "series_instance_uid",  # SERIES | Unique | VM 1 | UI
    "Modality": "modality",  # SERIES | Required | VM 1 | CS
    "SeriesNumber": "series_number",  # SERIES | Required | VM 1 | IS
    "SOPInstanceUID": "sop_instance_uid",  # IMAGE | Unique | VM 1 | UI
    "InstanceNumber": "instance_number",  # IMAGE | Required | VM 1 | IS
}

# Unique and required keys and their level, VR and VM for Patient Root
# Study Root is the same but includes the PATIENT attributes
_ATTRIBUTES = {
    "PatientID": ("PATIENT", "U", "LO", 1),
    "PatientName": ("PATIENT", "R", "PN", 1),
    "StudyInstanceUID": ("STUDY", "U", "UI", 1),
    "StudyDate": ("STUDY", "R", "DA", 1),
    "StudyTime": ("STUDY", "R", "TM", 1),
    "AccessionNumber": ("STUDY", "R", "SH", 1),
    "StudyID": ("STUDY", "R", "SH", 1),
    "SeriesInstanceUID": ("SERIES", "U", "UI", 1),
    "Modality": ("SERIES", "R", "VS", 1),
    "SeriesNumber": ("SERIES", "R", "IS", 1),
    "SOPInstanceUID": ("IMAGE", "U", "UI", 1),
    "InstanceNumber": ("IMAGE", "R", "UI", 1),
}
_PATIENT_ROOT_ATTRIBUTES = OrderedDict(
    {
        "PATIENT": ["PatientID", "PatientName"],
        "STUDY": [
            "StudyInstanceUID",
            "StudyDate",
            "StudyTime",
            "AccessionNumber",
            "StudyID",
        ],
        "SERIES": ["SeriesInstanceUID", "Modality", "SeriesNumber"],
        "IMAGE": ["SOPInstanceUID", "InstanceNumber"],
    }
)
_STUDY_ROOT_ATTRIBUTES = OrderedDict(
    {
        "STUDY": [
            "StudyInstanceUID",
            "StudyDate",
            "StudyTime",
            "AccessionNumber",
            "StudyID",
            "PatientID",
            "PatientName",
        ],
        "SERIES": ["SeriesInstanceUID", "Modality", "SeriesNumber"],
        "IMAGE": ["SOPInstanceUID", "InstanceNumber"],
    }
)

# Supported Information Models
_C_FIND = [
    PatientRootQueryRetrieveInformationModelFind,
    StudyRootQueryRetrieveInformationModelFind,
]
_C_GET = [
    PatientRootQueryRetrieveInformationModelGet,
    StudyRootQueryRetrieveInformationModelGet,
]
_C_MOVE = [
    PatientRootQueryRetrieveInformationModelMove,
    StudyRootQueryRetrieveInformationModelMove,
]

_PATIENT_ROOT = {
    PatientRootQueryRetrieveInformationModelFind: _PATIENT_ROOT_ATTRIBUTES,
    PatientRootQueryRetrieveInformationModelGet: _PATIENT_ROOT_ATTRIBUTES,
    PatientRootQueryRetrieveInformationModelMove: _PATIENT_ROOT_ATTRIBUTES,
}
_STUDY_ROOT = {
    StudyRootQueryRetrieveInformationModelFind: _STUDY_ROOT_ATTRIBUTES,
    StudyRootQueryRetrieveInformationModelGet: _STUDY_ROOT_ATTRIBUTES,
    StudyRootQueryRetrieveInformationModelMove: _STUDY_ROOT_ATTRIBUTES,
}


def create(db_location, echo=False):
    """Create a new database at `db_location` if one doesn't already exist.

    Parameters
    ----------
    db_location : str
        The location of the database.
    echo : bool, optional
        Turn the sqlalchemy logging on (default ``False``).
    """
    engine = create_engine(db_location, echo=echo)

    # Create the tables (won't recreate tables already present)
    Base.metadata.create_all(engine)

    return engine


# Database table setup stuff
Base = declarative_base()


class Image(Base):
    __tablename__ = "image"
    # (0008,0018) SOP Instance UID | VR UI, VM 1, U
    sop_instance_uid = Column(String(64), primary_key=True)
    # (0020,0013) Instance Number | VR IS, VM 1, R
    instance_number = Column(Integer)


class Instance(Base):
    __tablename__ = "instance"

    # Absolute path to the stored SOP Instance
    filename = Column(String)
    # Transfer Syntax UID of the SOP Instance
    transfer_syntax_uid = Column(String(64))
    sop_class_uid = Column(String(64))

    patient_id = Column(String, ForeignKey("patient.patient_id"))
    patient_name = Column(String, ForeignKey("patient.patient_name"))

    study_instance_uid = Column(String, ForeignKey("study.study_instance_uid"))
    study_date = Column(String, ForeignKey("study.study_date"))
    study_time = Column(String, ForeignKey("study.study_time"))
    accession_number = Column(String, ForeignKey("study.accession_number"))
    study_id = Column(String, ForeignKey("study.study_id"))

    series_instance_uid = Column(
        String, ForeignKey("series.series_instance_uid"))
    modality = Column(String, ForeignKey("series.modality"))
    series_number = Column(String, ForeignKey("series.series_number"))

    sop_instance_uid = Column(
        String,
        ForeignKey("image.sop_instance_uid"),
        primary_key=True,
    )
    instance_number = Column(String, ForeignKey("image.instance_number"))

    def as_identifier(self, identifier, model):
        """Return an Identifier dataset matching the elements from a query.

        Parameters
        ----------
        identifier : pydicom.dataset.Dataset
            The C-FIND, C-GET or C-MOVE request's *Identifier* dataset.
        model : pydicom.uid.UID
            The Query/Retrieve Information Model.

        Returns
        -------
        pydicom.dataset.Dataset
            The response *Identifier*.
        """
        ds = Dataset()
        ds.QueryRetrieveLevel = identifier.QueryRetrieveLevel

        if model in _PATIENT_ROOT:
            attr = _PATIENT_ROOT[model]
        else:
            attr = _STUDY_ROOT[model]

        all_keywords = []
        for level, keywords in attr.items():
            all_keywords.extend(keywords)
            if level == identifier.QueryRetrieveLevel:
                break

        for kw in [kw for kw in all_keywords if kw in identifier]:
            try:
                attribute = _TRANSLATION[kw]
            except KeyError:
                continue

            setattr(ds, kw, getattr(self, attribute, None))

        return ds

    @property
    def context(self):
        """Return a presentation context for the Instance.

        Returns
        -------
        pynetdicom.presentation.PresentationContext

        Raises
        ------
        ValueError
            If either of the *SOP Class UID* or *Transfer Syntax UID* is not
            available for the Instance.
        """
        if None in [self.sop_class_uid, self.transfer_syntax_uid]:
            raise ValueError(
                "Cannot determine which presentation context is required for "
                "for the SOP Instance"
            )

        return build_context(self.sop_class_uid, self.transfer_syntax_uid)


class Patient(Base):
    __tablename__ = "patient"
    # (0010,0020) Patient ID | VR LO, VM 1, U
    patient_id = Column(String(64), primary_key=True)
    # (0010,0010) Patient's Name | VR PN, VM 1, R
    patient_name = Column(String(400))


class Series(Base):
    __tablename__ = "series"
    # (0020,000E) Series Instance UID | VR UI, VM 1, U
    series_instance_uid = Column(String(64), primary_key=True)
    # (0008,0060) Modality | VR CS, VM 1, R
    modality = Column(String(16))
    # (0020,0011) Series Number | VR IS, VM 1, R
    series_number = Column(Integer)


class Study(Base):
    __tablename__ = "study"
    # (0020,000D) Study Instance UID | VR UI, VM 1, U
    study_instance_uid = Column(String(64), primary_key=True)
    # (0008,0020) Study Date | VR DA, VM 1, R
    study_date = Column(String(8))
    # (0008,0030) Study Time | VR TM, VM 1, R
    study_time = Column(String(14))
    # (0008,0050) Accession Number | VR SH, VM 1, R
    accession_number = Column(String(16))
    # (0020,0010) Study ID | VR SH, VM 1, R
    study_id = Column(String(16))
