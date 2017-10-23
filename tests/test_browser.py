import unittest
from base import Browser

from log import MyLogger


class BrowserTest(unittest.TestCase):
    MyLogger.get_class_name(__name__)

    def test_open_browser(self):
        driver = Browser.open_browser("chrome")
        driver.maximize_window()
        driver.get("https://www.amazon.com")


