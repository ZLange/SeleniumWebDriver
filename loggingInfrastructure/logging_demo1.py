"""
Logging demo 1
Logging levels
DEBUG
INFO
WARNINGS
ERROR
CRITICAL
"""

import logging  # built in lib


logging.basicConfig(filename="test.log", level = logging.DEBUG)   # basic configuration for logs -> write logs in file
logging.warning("warning message")
logging.info("info message")
logging.error("error message")
