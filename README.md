# Pynetdicom CLI App

This README provides instructions on how to set up and run the CLI application for Pynetdicom. The application allows you to perform DICOM operations such as C-ECHO and Basic Worklist Management Service (BWL).

## Installation

1. **Clone the Repository**
   ```sh
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Install Dependencies**
   Make sure you have Python 3 installed. Install the required packages using pip:
   ```sh
   pip install -r requirements.txt
   ```

## Running the Application

### Start the Application

To start the application, run the following command. By default, it binds to `localhost` on port `1234`:
```sh
python3 app/app.py
```

### Performing a C-ECHO

To perform a C-ECHO operation, use the `pynetdicom` module as follows:
```sh
python3 -m pynetdicom echoscu localhost 1234
```

### Performing a Basic Worklist Management Service (BWL)

To perform a BWL operation, run the `scu` from `bwl_scu.py`. This script uses a dummy dataset to check for a patient named 'edo':
```sh
python3 bwl_scu.py
```
By default, `bwl_scu.py` will connect to `localhost` on port `1234`.

## Use Cases

### 1. C-ECHO

To perform a C-ECHO, use the command provided above to verify connectivity and DICOM communication with the server.

### 2. Basic Worklist Management (BWL)

For BWL, the application checks for patient information using a dummy dataset. Run the `bwl_scu.py` script to perform this operation.

## Files and Directories

- `app/app.py`: The main application script that starts the DICOM server.
- `bwl_scu.py`: Script to perform Basic Worklist Management Service operations.
- `requirements.txt`: File containing the list of dependencies required by the application.

## Additional Information

For more information on `pynetdicom` and its capabilities, refer to the [pynetdicom documentation](https://pydicom.github.io/pynetdicom/stable/).

## Contact

For any issues or questions, please contact [your contact information].

---

Feel free to customize this README with your repository URL, contact information, and any other relevant details.