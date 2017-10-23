from selenium import webdriver
import logging
logging.basicConfig(level=logging.INFO)


class FireFoxBrowser(object):

    logger = logging.getLogger(__name__)

    def __init__(self):
        self.logger.info("....Firefox browser constructor........")

    def create_driver(self):
        self.logger.info("........Creating fire fox driver.....")
        driver = webdriver.Firefox()
        return driver
