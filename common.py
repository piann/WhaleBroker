import logging


def getDataFromDB():
    pass

def putDataIntoDB():
    pass


def setupLogging(fileName):
    # setup log file and log depth 

    fileHandler = logging.FileHandler(fileName)
    fileHandler.setLevel(logging.DEBUG)
    fileHandler.setFormatter( logging.Formatter('%(asctime)s:%(levelname)s:[%(filename)s.%(funcName)s]%(message)s', '%m-%d %H:%M:%S'))

    streamHandler = logging.StreamHandler()
    streamHandler.setLevel(logging.DEBUG)
    streamHandler.setFormatter( logging.Formatter('%(asctime)s:%(levelname)s:[%(filename)s.%(funcName)s]%(message)s', '%m-%d %H:%M:%S'))

    logger = logging.getLogger('')

    logger.setLevel(logging.DEBUG)
    logger.addHandler(fileHandler)
    logger.addHandler(streamHandler)


class tryCatchWrapped:
    # this is for decorator class

    def __init__(self, f):
        self.func = f

    def __call__(self, *args, **kwargs):
        try:
            self.func(*args, **kwargs)
        except Exception as e:
            logging.error(str(e), exc_info=True)

