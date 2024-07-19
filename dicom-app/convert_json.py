import json
import pydicom
from pydicom.data import get_testdata_file
from pydicom.dataset import Dataset

ds = Dataset()
ds.PatientName = '*'
ds.ScheduledProcedureStepSequence = [Dataset()]
item = ds.ScheduledProcedureStepSequence[0]
item.ScheduledStationAETitle = 'CTSCANNER'
item.ScheduledProcedureStepStartDate = '20181005'
item.Modality = 'CT'

# Convert Dataset to JSON string
ds_json = ds.to_json()

# Parse JSON string to Python dictionary
ds_dict = json.loads(ds_json)

# Pretty print the dictionary
print(json.dumps(ds_dict, indent=4))
