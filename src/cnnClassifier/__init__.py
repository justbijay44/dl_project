import os
import sys
import logging

# Setting how we see the message
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dirs = "logs"
log_filepath = os.path.join(log_dirs, "runnings_logs.log")
os.makedirs(log_dirs, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,

    handlers=[
        # write log to file
        logging.FileHandler(log_filepath),

        #print to console
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("cnnClassifierLogger")