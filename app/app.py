import argparse
import sys
import os
from configparser import ConfigParser

from pydicom.uid import (
    ExplicitVRBigEndian,
    ExplicitVRLittleEndian,
    ImplicitVRLittleEndian
)

from pynetdicom import (
    AE,
    evt,
    debug_logger
)

from handlers import handle_find

from pynetdicom.sop_class import ModalityWorklistInformationFind
# from pynetdicom._globals import ALL_TRANSFER_SYNTAXES, DEFAULT_MAX_LENGTH
# from pynetdicom.utils import set_ae

debug_logger()

__aetitle__ = "Dicom project"
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
        "-p", "--port", default=1234 , help="TCP/IP port number to listen on",
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
    
    ## Database
    db_opts = parser.add_argument_group("Database Options")
    db_opts.add_argument(
        "--database-location",
        metavar="[f]ile",
        help="override the location of the database using file f",
        type=str,
    )
    db_opts.add_argument(
        "--instance-location",
        metavar="[d]irectory",
        help=("override the configured instance storage location to directory d"),
        type=str,
        default="data/"  # Default value set to "data/"
    )
    
    return parser.parse_args()
    

def main(args=None):
    if args is not None:
        sys.argv = args
    
    args = _setup_argparser()

    # Print the arguments to verify the correct values are being used
    print(f"Listening on port: {args.port}")
    print(f"Network timeout: {args.network_timeout} seconds")
    print(f"Bind address: {args.bind_address}")
    print(f"Database location: {args.database_location}")
    print(f"Network timeout: {args.network_timeout}")

    # Use default or specified configuration file
    current_dir = os.path.abspath(os.path.dirname(__file__))
    instance_dir = os.path.join(current_dir, args.instance_location)
    # db_path = os.path.join(current_dir, app_config["database_location"])
    
    # Try to create the instance storage directory
    os.makedirs(instance_dir, exist_ok=True)
    
    ae = AE(args.ae_title)
    ae.network_timeout = args.network_timeout
    
    ae.add_supported_context(ModalityWorklistInformationFind)

    handlers = [(evt.EVT_C_FIND, handle_find)]
    
    ae.start_server(
        (args.bind_address, args.port), evt_handlers=handlers
    )


if __name__ == "__main__":
    main()
    