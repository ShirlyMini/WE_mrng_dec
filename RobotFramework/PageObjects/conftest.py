from datetime import datetime
from selenium import webdriver

def launch_browser(browser):
    if browser == "chrome":
        from selenium.webdriver.chrome.service import Service
        service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    elif browser == "edge":
        from selenium.webdriver.edge.service import Service
        service_obj = Service(r"E:\selenium\drivers\msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj)
    elif browser == "ff":
        # from selenium.webdriver.firefox.service import Service
        # service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
        driver = webdriver.Firefox()
    else:
        from selenium.webdriver.chrome.service import Service
        service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    driver.get("https://admin-demo.nopcommerce.com/")
    driver.maximize_window()
    driver.implicitly_wait(20)
    return driver

def quit_browser(driver):
    driver.quit()

