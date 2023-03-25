"""
Logger Demo
"""

import logging

class LoggerConsole():
    
    def testLog(self):
        # create logger and set level
        logger = logging.getLogger(LoggerConsole.__name__)
        logger.setLevel(logging.DEBUG)
        
        # create console handler and set log level
        chandler = logging.StreamHandler()
        chandler.setLevel(logging.DEBUG)

        # create formatter
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        
        # add formatter to console handler -> ch
        chandler.setFormatter(formatter)

        # add console handler to logger
        logger.addHandler(chandler)
        
        # logging messages
        logger.debug("debug message")
        logger.warning("warning message")
        logger.info("info message")
        logger.error("error message")
        logger.critical("critical message")

demo = LoggerConsole()
demo.testLog()