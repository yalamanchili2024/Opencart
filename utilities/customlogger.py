import logging
import  os

# logs configuration file

class loggen:
    @staticmethod
    def loggen():
        path = os.path.join(r"C:\Users\yalam\PycharmProjects\opecartv1\Opencart\logs","automation.log")
        logging.basicConfig(filename=path,format='%(asctime)s: %(levelname)s : %(message)s',
                            datefmt='%m/%d/%y %I:%M:%S %p')

        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger

