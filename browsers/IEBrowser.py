import logging
from selenium import webdriver

logging.basicConfig(level=logging.INFO)


class IEBrowser(object):
    logger = logging.getLogger(__name__)

    def __init__(self):
        self.logger.info("...IEBrowser Constructor......")

    def create_driver(self):
        self.logger.info(".........Creating IE Driver.........")
        driver = webdriver.Ie()
        return driver
