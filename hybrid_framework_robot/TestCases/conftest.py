from datetime import datetime

import pytest
from selenium import webdriver

from hybrid_framework_robot.Utilities.ReadProperty import ReadProperty



def launch_browser(b_name):
    if b_name == "chrome":
        from selenium.webdriver.chrome.service import Service
        service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    elif b_name == "edge":
        from selenium.webdriver.edge.service import Service
        service_obj = Service(r"E:\selenium\drivers\msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj)
    elif b_name == "ff":
        # from selenium.webdriver.firefox.service import Service
        # service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
        driver = webdriver.Firefox()
    else:
        from selenium.webdriver.chrome.service import Service
        service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    driver.get(ReadProperty.GetURL())
    driver.maximize_window()
    driver.implicitly_wait(20)
    return driver

def teardown(driver):
    driver.quit()