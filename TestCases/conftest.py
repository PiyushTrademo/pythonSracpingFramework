import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from Config.Config import TestData


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
        web_driver.get(TestData.Base_Url)
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        web_driver.get(TestData.Base_Url)
    request.cls.driver = web_driver
    web_driver.implicitly_wait(10)
    yield
    web_driver.quit()
