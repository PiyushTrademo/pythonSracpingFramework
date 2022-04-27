import time

from Config.Config import TestData
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

"""This is SCAC page specif file"""

class ScacCode(BasePage):

    """Element locators"""
    input_field = (By.ID, "code")
    submit_button = (By.ID, "sub")
    company_name = (By.XPATH, "//div[@class='paragraph']")

    """Constructor of the class
    Call the URL to open it in the browser"""
    def __init__(self, driver):
        super().__init__(driver)
        driver.get(TestData.Base_Url)

    """Page actions"""
    def click_input(self, scac):
        try:
            self.do_click(self.input_field)
            self.do_send_keys(self.input_field, scac)
            self.do_click(self.submit_button)
            time.sleep(1)
            strg = self.get_element_text(self.company_name)
            name = self.get_company_name(strg)
            return name
        except BaseException as be:
            return be.args









