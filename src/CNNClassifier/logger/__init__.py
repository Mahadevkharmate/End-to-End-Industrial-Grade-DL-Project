import os
import sys
import logging

# Create a custom logger
logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s]" # log format
log_dir = "logs" # directory to save logs
os.makedirs(log_dir, exist_ok=True) # create the directory if it doesn't exist
log_filepath = os.path.join(log_dir, "running_logs.log") # log file path

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath), # file handler to write logs to a file 
        logging.StreamHandler(sys.stdout)  # stream handler to output logs to console
    ]
)  # configure logging to file and console

logger = logging.getLogger("CNNClassifier") # create a logger instance with the name "CNNClassifier"