Sure! Here's a draft for your `README.md`:

---

# DICOM Application

This application facilitates DICOM operations including SCP, MPPS, and Modality Worklist.

## Prerequisites

To run this application, your PC should have the following installed:
- Python
- Git
- Python virtualenv

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

4. **Run the main script**
    ```bash
    python dicom_app/scp_mpps_modalityworklist.py
    ```

## Usage

After running the main script, the program will wait for a C-FIND request by the DICOM.

To demo the C-FIND request to the SCP, you can run `dicom_scu.py`:
```bash
python dicom_scu.py
```

You may edit the request header in `dicom_scu.py` to suit your needs.
