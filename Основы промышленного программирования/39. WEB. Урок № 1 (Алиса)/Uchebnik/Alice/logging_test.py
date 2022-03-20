import logging


logging.basicConfig(
    level=logging.WARNING
)


def log():
    logging.debug("Debug")
    logging.info("Info")
    logging.warning("Warning")
    logging.error("Error")
    logging.critical("Critical")


if __name__ == '__main__':
    log()