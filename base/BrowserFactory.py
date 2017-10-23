import logging
from browsers.ChromeBrower import ChromeBrowser
from browsers.FireFoxBrowser import FireFoxBrowser
from browsers.IEBrowser import IEBrowser
from base.Factory import Factory

logging.basicConfig(level=logging.INFO)


class BrowserFactory(Factory):
    logger = logging.getLogger(__name__)

    def __init__(self,browser):
        self.logger.info("...........Browser Factory constructor....")
        self.browser = browser

    def crate_driver(self):
        self.logger.info("......Creating driver object for browser.....")
        driver = ''
        if self.browser.strip() == 'chrome':
            driver = ChromeBrowser().create_driver()
        elif self.browser.strip() == 'ff':
            driver = FireFoxBrowser.create_driver()
        elif self.browser.strip() == 'ie':
            driver = IEBrowser.create_driver()
        return driver

    def open_browser(self):
        self.logger.info("...Opening browser.....")
        driver = self.crate_driver()
        return driver

