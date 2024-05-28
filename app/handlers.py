import os
from pydicom import dcmread
from pydicom.dataset import Dataset

from pynetdicom import debug_logger

# debug_logger()

# Implement the handler for evt.EVT_C_FIND
def handle_find(event):
    """Handle a C-FIND request event."""
    ds = event.identifier

    print("Received C-FIND request")

    # Import stored SOP Instances
    # Import stored SOP Instances
    instances = []
    fdir = 'bwl/dataset/'
    print(os.listdir(fdir))
    for fpath in os.listdir(fdir):
        instances.append(dcmread(os.path.join(fdir, fpath)))
    # instances = []
    # fdir = 'dataset/CT_small.dcm'
    # instances.append(dcmread(fdir))
    # # for fpath in os.listdir(fdir):
    # #     instances.append(dcmread(os.path.join(fdir, fpath)))

    if 'ScheduledProcedureStepSequence' not in ds:
        print('failure')
        # Failure
        yield 0xC000, None
        return

    if 'ScheduledProcedureStepSequence' in ds:
        if 'PatientName' in ds:
            if ds.PatientName not in ['*', '', '?']:
                matching = [
                    inst for inst in instances if inst.PatientName == ds.PatientName
                ]

             # Skip the other possible values...

         # Skip the other possible attributes...

     # Skip the other QR levels...

    for instance in matching:
        # Check if C-CANCEL has been received
        if event.is_cancelled:
            yield (0xFE00, None)
            print('cancelled')
            return

        identifier = Dataset()
        identifier.PatientName = instance.PatientName
        # identifier.QueryRetrieveLevel = ds.QueryRetrieveLevel

        # Pending
        yield (0xFF00, identifier)
