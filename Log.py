import logging

FORMAT = '[%(asctime)s] [%(process)d] [%(levelname)7s] [%(filename)s:%(lineno)s]: %(message)s'
DATE_FORMAT = '%Y-%m-%d %H:%M:%S %z'


def init_logger(name):
    # Formatters
    formatter = logging.Formatter(fmt=FORMAT, datefmt=DATE_FORMAT)

    # Handlers
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.DEBUG)


    # Loggers
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # root level
    logger.addHandler(console_handler)
    return logger
