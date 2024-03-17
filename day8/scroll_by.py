from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.chrome.service import Service
from time import sleep

from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By


service_obj=Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

act_obj = ActionChains(driver)
flag_we=driver.find_element(By.XPATH,"//img[@alt='Flag of India']")
# print(flag_we.location)
# act_obj.scroll_to_element(flag_we).perform()

# act_obj.scroll_by_amount(flag_we.location['x'], flag_we.location['y']).perform()

obj=ScrollOrigin.from_element(flag_we)
act_obj.scroll_from_origin(obj,0,-1000).perform()
sleep(5)