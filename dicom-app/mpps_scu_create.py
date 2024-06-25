import json
import sys
from pydicom.dataset import Dataset
from pydicom.uid import generate_uid

from pynetdicom import AE, debug_logger
from pynetdicom.sop_class import ModalityPerformedProcedureStep
from pynetdicom.status import code_to_category

# Function to read JSON file and return parsed data
def read_json_file(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    return data


ct_study_uid = generate_uid()
mpps_instance_uid = generate_uid()

# Our N-CREATE *Attribute List*
def build_attr_list(patient_data):
    ds = Dataset()
    # Performed Procedure Step Relationship
    ds.ScheduledStepAttributesSequence = [Dataset()]
    step_seq = ds.ScheduledStepAttributesSequence
    step_seq[0].StudyInstanceUID = ct_study_uid
    step_seq[0].ReferencedStudySequence = []
    step_seq[0].AccessionNumber = '1'
    step_seq[0].RequestedProcedureID = "1"
    step_seq[0].RequestedProcedureDescription = 'Some procedure'
    step_seq[0].ScheduledProcedureStepStartDate = '20181005'
    step_seq[0].ScheduledProcedureStepID = "1"
    step_seq[0].ScheduledProcedureStepDescription = 'Some procedure step'
    step_seq[0].ScheduledProcedureProtocolCodeSequence = []

    # Use the patient data from the JSON file
    ds.PatientName = 'Edo' #patient_data['PatientName']
    ds.PatientID = '1' #patient_data['PatientID']
    ds.PatientBirthDate =  '23101996'#patient_data['PatientBirthDate']
    ds.PatientSex = '0'#patient_data['PatientSex']

    ds.ReferencedPatientSequence = []
    # Performed Procedure Step Information
    ds.PerformedProcedureStepID = "1"
    ds.PerformedStationAETitle = 'admin-scp'
    ds.PerformedStationName = 'Some station'
    ds.PerformedLocation = 'Some location'
    ds.PerformedProcedureStepStartDate = '20000101'
    ds.PerformedProcedureStepStartTime = '1300'
    ds.PerformedProcedureStepStatus = 'IN PROGRESS'
    ds.PerformedProcedureStepDescription = 'Some description'
    ds.PerformedProcedureTypeDescription = 'Some type'
    ds.PerformedProcedureCodeSequence = []
    ds.PerformedProcedureStepEndDate = None
    ds.PerformedProcedureStepEndTime = None
    # Image Acquisition Results
    ds.Modality = 'CT'
    ds.StudyID = "1"
    ds.PerformedProtocolCodeSequence = []
    ds.PerformedSeriesSequence = []

    return ds

# Main function to run the script
def main(json_file_path):
    patient_data = read_json_file(json_file_path)

    # Initialise the Application Entity
    ae = AE()

    # Add a requested presentation context
    ae.add_requested_context(ModalityPerformedProcedureStep)

    # Associate with peer AE at IP 127.0.0.1 and port 1234
    assoc = ae.associate("127.0.0.1", 1234)

    if assoc.is_established:
        # Use the N-CREATE service to send a request to create a SOP Instance
        # should return the Instance itself
        status, attr_list = assoc.send_n_create(
            build_attr_list(patient_data),
            ModalityPerformedProcedureStep,
            mpps_instance_uid
        )

        # Check the status of the display system request
        if status:
            print('N-CREATE request status: 0x{0:04x}'.format(status.Status))

            # If the MPPS request succeeded the status category may
            # be either Success or Warning
            category = code_to_category(status.Status)
            if category in ['Warning', 'Success']:
                # `attr_list` is a pydicom Dataset containing attribute values
                print(attr_list)
        else:
            print('Connection timed out, was aborted or received invalid response')

        # Release the association
        assoc.release()
    else:
        print('Association rejected, aborted or never connected')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 mpps_scu_create.py <json_file_path>")
    else:
        main(sys.argv[1])
