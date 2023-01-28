import logging
import os


class LogGenerator:
    @staticmethod
    def logger():
        logging.basicConfig(filename=os.path.abspath(os.curdir)+"\\logs\\pytest.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger
