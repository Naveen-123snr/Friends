import pytest
from selenium import webdriver
from Library.config import Configuration
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

#path = r"C:\Users\C NAVEEN\Desktop\New Folder\geckodriver.exe"


@pytest.fixture(params=["firefox","chrome"])
def init_driver(request):  # request is a library

    browser = request.param

    if browser.lower() == "chrome":
        option = webdriver.ChromeOptions()
        option.add_argument("--diable-notification")
        option.add_argument("--disable-infobars")
        option.add_argument("start-maximized")
        option.add_argument("--disable-extensions")
        option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications":2})
        option.add_argument("use-fake-ui-for-media-stream")
        driver = webdriver.Chrome(executable_path=Configuration.CHROME_PATH,options= option)

    elif browser.lower() == "firefox":
        option = Options()
        option.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
        #driver = webdriver.Firefox(executable_path=r"C:\Users\C NAVEEN\Downloads\geckodriver-v0.32.0-win32.zip\geckodriver.exe",options=option)
        driver = webdriver.Firefox(executable_path=r"C:\Users\C NAVEEN\Desktop\New Folder\geckodriver.exe",options=option)




        # provide a full path of the driver
        # path = r"F:\scraping\selenium\geckodriver.exe"

        # pass the driver path as a service

        # driver = webdriver.Firefox("C:\\selenium\\mozilla")
        driver.set_page_load_timeout(30)

    elif browser.lower() == "edge":
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())


    driver.get(Configuration.URL)
    driver.maximize_window()
    driver.implicitly_wait(30)
    yield driver

