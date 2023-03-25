import inspect
import logging

def customLogger(loglevel):
    loggerName = inspect.stack()[1][3] # gets name of the class/method from where method is called
    logger = logging.getLogger(loggerName)
    
    # by default log all messages
    logger.setLevel(logging.DEBUG)
    
    fileHandler = logging.FileHandler(filename="{0}.log".format(loggerName), mode="w")  # file name can be used direclty as well like "{0}.log".format(loggerName)
    fileHandler.setLevel(loglevel)
    
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    
    return logger