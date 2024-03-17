from selenium import webdriver
from selenium.webdriver import ActionChains

# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service
from time import sleep
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
###############################Chrome
# location = r"C:\Users\user\PycharmProjects\pythonProject_WEMorning_dec\day8"
# service_obj=Service("E:\selenium\drivers\chromedriver.exe")
# chrome_ops = webdriver.ChromeOptions()
# chrome_ops.add_experimental_option("prefs", {"download.default_directory":location})
# driver = webdriver.Chrome(service=service_obj, options=chrome_ops)
#
# driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
# driver.maximize_window()
# driver.find_element(By.XPATH,"//tbody/tr[1]/td[5]/a").click()

location = r"C:\Users\user\PycharmProjects\pythonProject_WEMorning_dec\day8"
service_obj=Service("E:\selenium\drivers\msedgedriver.exe")
egde_ops = webdriver.EdgeOptions()

egde_ops.add_experimental_option("prefs", {"download.default_directory":location})
driver = webdriver.Edge(service=service_obj, options=egde_ops)

driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
driver.maximize_window()
driver.find_element(By.XPATH,"//tbody/tr[1]/td[5]/a").click()
sleep(10)
driver.switch_to.window(driver.window_handles[1])
sleep(2)
driver.find_element(By.XPATH, "//span[text()='Download']")

sleep(20)