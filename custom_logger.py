import logging

def custom_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
    file_handler = logging.FileHandler('custom_logger.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger

def test_logger():
    logger = custom_logger()
    logger.debug('A debug statement is executed')
    logger.info('Information statement')
    logger.warning('Something is in warning mode')
    logger.error('A Major error has happened')
    logger.critical('Critical issue')