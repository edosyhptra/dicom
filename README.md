# DICOM Application

This application facilitates DICOM operations including SCP, MPPS, and Modality Worklist for SYNGO MR XA50A.

## Prerequisites

To run this application, your PC should have the following installed:
- Python > 3.7
- Git
- Python virtualenv --> you may use venv or conda

## Setup

1. **Clone the repository**
    ```bash
    git clone https://github.com/edosyhptra/dicom.git
    ```

2. **Create a virtual environment**
    ```bash
    python -m virtualenv [env_name]
    ```

3. **Activate the virtual environment**
    ```bash
    source /path/to/[env_name]/bin/activate
    ```

4. **Install Dependencies using pip**
    ```bash
    pip install -r requirements.txt
    ```

5. **Config**
    By default, the program will run as a localhost. To modify the address you change the code inside the script scp_mpps_modalityworklist.py
    
    Also, you have to change the peer Dicom address inside the same script as well. 

6. **Run the main script**
    ```bash
    python dicom_app/scp_mpps_modalityworklist.py
    ```
