import logging

logger = ''


def get_class_name(self,name):
    global logger
    logger = logging.getLogger(name)

fh = logging.FileHandler("./logfiles/log_01.log")
fh.setLevel(level=logging.INFO)
fh.setLevel(level=logging.DEBUG)
fh.setLevel(level=logging.WARNING)
fh.setLevel(level=logging.CRITICAL)
# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to fh
fh.setFormatter(formatter)

logger.addHandler(fh)


def enter(log_message):
    logger.info(":::::::"+log_message+":::::::::::::")


def exit(log_message):
    logger.info(":::::::"+log_message+":::::::::::::")


def debug(log_message):
    logger.debug(":::::::"+log_message+":::::::::::::")


def warning(log_message):
    logger.warning(":::::::"+log_message+":::::::::::::")


def critical(log_message):
    logger.critical(":::::::"+log_message+":::::::::::::")