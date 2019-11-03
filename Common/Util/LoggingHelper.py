import logging


logging.basicConfig(level=logging.DEBUG, datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)-15s - [%(levelname)s] %(module)s: %(message)s',)


def log_info_message(message):
    logging.info(message)

def log_warning_message(message):
    logging.warning(message)