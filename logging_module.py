import os
import logging

logging.basicConfig(filename=os.path.join(os.path.dirname(__file__), 'app.log'), level=logging.DEBUG)

def log(level, message):
    if level == 'info':
        logging.info(message)
    elif level == 'warning':
        logging.warning(message)
    elif level == 'error':
        logging.error(message)
    else:
        logging.debug(message)
