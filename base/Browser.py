import logging
from base.BrowserFactory import BrowserFactory

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


def open_browser(browser):
        logger.info("Opening browser:::{}".format(browser))

        driver = BrowserFactory(browser).open_browser()
        return driver

