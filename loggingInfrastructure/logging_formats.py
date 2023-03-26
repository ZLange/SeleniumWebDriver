"""
Logging formats
https://docs.python.org/3/library/logging.html
https://docs.python.org/3/library/time.html
"""

import logging 
# import time

# define the logging formt
logging.basicConfig(format="%(asctime)s: %(levelname)s: %(message)s",
                    datefmt="%m/%d/%Y %I:%M:%S %p", level = logging.DEBUG)   # I for 12 format, H for 24 format
# test messages
logging.warning("warning message")
logging.info("info message")
logging.error("error message")
