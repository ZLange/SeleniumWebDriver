import logging
# import sys
# import os
# logpath = "../logging_infrastructure"
# sys.path.append(os.path.abspath(logpath))
# import logging_infrastructure.custom_logger as cl
from logging_infrastructure import custom_logger as cl  # should work, for now got only error ModuleNotFoundError

class CustLoggingDemo():
    
    log = cl.customLogger(logging.DEBUG)
    
    def method1(self):
        self.log.debug("debug message")
        self.log.warning("warning message")
        self.log.info("info message")
        self.log.error("error message")
        self.log.critical("critical message")
        
    def method2(self):
        m2log = cl.customLogger(logging.INFO)
        m2log.debug("debug message")
        m2log.log.warning("warning message")
        m2log.log.info("info message")
        m2log.log.error("error message")
        m2log.log.critical("critical message")
        
    def method3(self):
        m3log = cl.customLogger(logging.INFO)
        m3log.log.debug("debug message")
        m3log.log.warning("warning message")
        m3log.log.info("info message")
        m3log.log.error("error message")
        m3log.log.critical("critical message")
        
        
demo = CustLoggingDemo()
demo.method1()
demo.method2()
demo.method3()