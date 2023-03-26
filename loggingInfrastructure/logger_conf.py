import logging
import logging.config
from os import path

class LoggerDemoConf():
    
    def testLog(self):
        # create logger
        conf_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf') # need to add path otherwise won't read config file from current dir
        logging.config.fileConfig(conf_file_path)
        logger = logging.getLogger(LoggerDemoConf.__name__)

        # logging messages
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warn message')
        logger.error('error message')
        logger.critical('critical message')

demo = LoggerDemoConf()
demo.testLog()