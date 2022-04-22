import time

from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class ScacCode(BasePage):

    """Element locators"""
    input_field = (By.ID, "code")
    submit_button = (By.ID, "sub")
    company_name = (By.XPATH, "//div[@class='paragraph']")

    """Constructor of the class"""
    def __init__(self, driver):
        super().__init__(driver)

    """Page actions"""
    def click_input(self, scac):
        try:
            self.do_click(self.input_field)
            self.do_send_keys(self.input_field, scac)
            self.do_click(self.submit_button)
            time.sleep(1)
            #print(self.get_element_text(self.company_name))
            strg = self.get_element_text(self.company_name)
            name = self.get_company_name(strg)
            return name
        except BaseException as be:
            return be.args
        #company_name = name.strip()








