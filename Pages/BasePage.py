from logging import exception

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

"""This will all the utility functions
All the reusable methods will be defined in this File """


class BasePage:
    """Constructor of the class"""

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(by_locator)).text
            #ele_text = element.text
            return element
        except BaseException as es:
            return es.args


    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(by_locator))
        return bool(element)

    def get_company_name(self,strg):
        try:
            split_strg = strg.split(': ', 4)
            return split_strg[2]

        except BaseException as es:
            return es.args
