import log
from selenium import webdriver

log.basicConfig(level=log.INFO)


class ChromeBrowser(object):

    logger = log.getLogger(__name__)

    def __init__(self):
        self.logger.info(".....Chrome Browser constructor....")

    def create_driver(self):
        self.logger.info(".....Creating Chrome browser....")
        driver = webdriver.Chrome()
        return driver