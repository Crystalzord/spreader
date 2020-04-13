import logging


def setup_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    fh = logging.FileHandler('spreader-log.txt')
    fh.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)

    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s: %(message)s')

    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    logger.addHandler(ch)
    logger.addHandler(fh)
