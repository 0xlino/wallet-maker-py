import logging

import logging

def custom_logger():
    """
    Create a custom logger.

    Returns:
        logging.Logger: The custom logger object.
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
    file_handler = logging.FileHandler('custom_logger.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger

def test_logger():
    """
    Test the logger

    This function tests the functionality of the logger by logging messages at different levels of severity.
    It creates a logger instance, logs debug, info, warning, error, and critical messages, and verifies that they are properly logged.

    """
    logger = custom_logger()
    logger.debug('A debug statement is executed')
    logger.info('Information statement')
    logger.warning('Something is in warning mode')
    logger.error('A Major error has happened')
    logger.critical('Critical issue')