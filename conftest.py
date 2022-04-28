import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options

from Config.Config import TestData


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    opt = Options()
    opt.add_experimental_option("excludeSwitches", ["enable-automation"])
    opt.add_experimental_option('useAutomationExtension', False)
    opt.add_argument("--disable-blink-features=AutomationControlled")
    opt.add_argument("--disable-extensions")
    opt.add_argument("--proxy-server='direct://'")
    opt.add_argument("--proxy-bypass-list=*")
    # opt.add_argument("--start-maximized")
    opt.add_argument('--headless')
    opt.add_argument('--disable-gpu')
    opt.add_argument('--disable-dev-shm-usage')
    opt.add_argument('--no-sandbox')
    opt.add_argument("--enable-javascript")
    opt.add_argument('--ignore-certificate-errors')
    opt.add_argument("--incognito")
    if request.param == "chrome":
        web_driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)

    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    request.cls.driver = web_driver
    web_driver.implicitly_wait(10)
    yield
    web_driver.quit()
