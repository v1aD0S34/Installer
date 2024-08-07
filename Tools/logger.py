import logging


def log_to_file(message):
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', filename='../log.txt')
    logger = logging.getLogger()
    logger.handlers[0].setFormatter(logging.Formatter('%(asctime)s | %(message)s', datefmt='%d.%m.%Y %H:%M:%S'))
    logger.info(message)
