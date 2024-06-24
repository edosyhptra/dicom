from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import json
import subprocess
import tempfile
from pydicom.dataset import Dataset
from pydicom.uid import generate_uid
from pynetdicom import AE, evt
from pynetdicom.sop_class import ModalityPerformedProcedureStep, ModalityWorklistInformationFind
import handlers as hd

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
                           'PatientBirthDate', 'PatientSex']
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

            # Write the JSON data to a temporary file
            with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.json') as temp_file:
                json.dump(patient_data, temp_file)
                temp_file_path = temp_file.name

            # Execute the external script with the temporary file path
            try:
                subprocess.run(["python3", "mpps_scu_create.py",
                               temp_file_path], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error running external script: {e}")
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
    server_address = ('127.0.0.1', 8080)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print("HTTP server running on port 8080")
    httpd.serve_forever()

# Function to start the DICOM AE server


def start_dicom_ae():
    ae = AE(ae_title='admin-scp')

    # Add the supported presentation context
    ae.add_supported_context(ModalityPerformedProcedureStep)
    ae.add_supported_context(ModalityWorklistInformationFind)

    handlers = [(evt.EVT_N_CREATE, hd.handle_create),
                (evt.EVT_N_SET, hd.handle_set),
                (evt.EVT_C_FIND, hd.handle_find)]

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
