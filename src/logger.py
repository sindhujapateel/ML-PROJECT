'''It imports logging, os, and datetime to handle logging, folders, and timestamps.
It creates a unique log filename using the current date and time.
It builds a logs directory inside your project and creates it if it doesn't exist.
It combines the logs folder path and filename to form the full path of the log file.
It configures Python's logging system to:
write log messages into that file,
include timestamp, line number, logger name, level, and message in each log entry,
log messages at INFO level and above.'''


import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)

if __name__=="main__":
    logging.info("Logging has started ")
