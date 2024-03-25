from poium import Elements
from selenium import webdriver

browser_type = [
    'Chrome',
    'Firefox',
    'Edge',
    'IE'
]


class Browser(object):

    def __init__(self, browser: str):
        my_browser = browser.title()
        if my_browser in browser_type:
            if my_browser == 'Chrome':
                self.driver = webdriver.Chrome()
            elif my_browser == 'Firefox':
                self.driver = webdriver.Firefox()
            else:
                raise Exception("No driver has been installed for this browser！")
        else:
            raise Exception("The browser name is not written correctly！")

    def get_driver(self):
        return self.driver


class MyElements(Elements):
    def __getitem__(self, item):
        return 0


driver = Browser('chrome').get_driver()
