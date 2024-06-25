from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import json
import subprocess
import tempfile
from pydicom.dataset import Dataset
from pydicom.uid import generate_uid
from pynetdicom import AE, evt
from pynetdicom.sop_class import (
    ModalityPerformedProcedureStep, 
    ModalityWorklistInformationFind,
    PatientRootQueryRetrieveInformationModelFind,
)

import handlers as hd
import argparse
import os
import db
from sqlalchemy.orm import sessionmaker
from pydicom import dcmread

import sys

__aetitle__ = "admin-scp"
__version__ = "0.6.0"

def _setup_argparser():
    parser = argparse.ArgumentParser(
        description=(
            "program for dicom. adapted from pynetdicom "
        ),
        usage="storescp [options] port",
    )

    # Parameters
    req_opts = parser.add_argument_group("Parameters")
    req_opts.add_argument(
        "-p", "--port", default=1234, help="TCP/IP port number to listen on",
        type=int)

    # Network Options
    net_opts = parser.add_argument_group("Network Options")
    net_opts.add_argument(
        "-aet",
        "--ae-title",
        metavar="[a]etitle",
        help="override the configured AE title",
        default=__aetitle__
    )
    net_opts.add_argument(
        "-tn",
        "--network-timeout",
        metavar="[s]econds",
        help="timeout for the network (default: 30 s)",
        type=float,
        default=30,
        required=False
    )
    net_opts.add_argument(
        "-ba",
        "--bind-address",
        metavar="[a]ddress",
        help=(
            "The address of the network interface to "
            "listen on. If unset, listen on all interfaces."
        ),
        default="localhost",
    )

    # Database
    db_opts = parser.add_argument_group("Database Options")
    db_opts.add_argument(
        "--database-location",
        metavar="[f]ile",
        help="override the location of the database using file f",
        type=str,
        default="data.sqlite"
    )
    db_opts.add_argument(
        "--instance-location",
        metavar="[d]irectory",
        help=("override the configured instance storage location to directory d"),
        type=str,
        default="app/data/CTImageStorage.dcm"  # Default value set to "data/"
    )

    return parser.parse_args()

# Handlers for HTTP requests
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        response = {
            "message": "HTTP server is running"
        }
        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        patient_data = json.loads(post_data)

        # Validate the received data
        required_fields = ['PatientName', 'PatientID',
                           'PatientBirthDate', 'PatientSex',
                           'StudyID', 'AccessionNumber',
                           'ReferringPhysician', 'StudyDescription',
                           'ScheduledProcedureStepStartDate',
                           'Modality', 'RequestedProcedureID',
                           'RequestedProcedureDescription',
                           'ScheduledStationAETitle',
                           'ScheduledPerformingPhysician',
                           'ScheduledProcedureStepLocation',
                           'PreMedication', 'SpecialNeeds']

        if all(field in patient_data for field in required_fields):
            # Respond that the data was received
            response = {
                "message": "Data received successfully",
                "data": patient_data
            }
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
            
           # Write the JSON data to the specified file
            json_file_path = 'dummy-data/data1.json'
            os.makedirs(os.path.dirname(json_file_path), exist_ok=True)
            with open(json_file_path, 'w') as json_file:
                json.dump(patient_data, json_file)

            # Save the JSON file data into managed_instances dict
            hd.save_into_managed_instances(json_file_path)
            
            # Execute the external script with the temporary file path
            # try:
            #     subprocess.run(["python3", "mpps_scu_create.py",
            #                    temp_file_path], check=True)
            # except subprocess.CalledProcessError as e:
            #     print(f"Error running external script: {e}")
        else:
            response = {
                "message": "Invalid data format",
                "data": patient_data
            }
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())

# Function to start the HTTP server
def start_http_server():
    server_address = ('localhost', 8080)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print("HTTP server running on port 8080")
    httpd.serve_forever()

# Function to start the DICOM AE server
def start_dicom_ae():
    
    ae = AE(ae_title=__aetitle__)

    # Add the supported presentation context
    ae.add_supported_context(ModalityPerformedProcedureStep)
    ae.add_supported_context(ModalityWorklistInformationFind)
    ae.add_supported_context(PatientRootQueryRetrieveInformationModelFind)

    handlers = [(evt.EVT_N_CREATE, hd.handle_create),
                (evt.EVT_N_SET, hd.handle_set),
                (evt.EVT_C_FIND, hd.handle_find)]
    
    # Generate dummy data
    # hd.generate_dummy_data()
    
    # Start listening for incoming association requests
    print("DICOM AE server running on port 1234")
    ae.start_server(("127.0.0.1", 1234), evt_handlers=handlers)
    
# Run both servers in parallel
if __name__ == "__main__":
    http_thread = threading.Thread(target=start_http_server)
    dicom_thread = threading.Thread(target=start_dicom_ae)

    http_thread.start()
    dicom_thread.start()

    http_thread.join()
    dicom_thread.join()
