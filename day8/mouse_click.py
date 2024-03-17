from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By


service_obj=Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()

act_obj = ActionChains(driver)

#####################right click
# r_click_elem = driver.find_element(By.XPATH, "//span[text()='right click me']")
# options_elem = driver.find_element(By.XPATH, "//span[text()='Cut']")
#
# act_obj.context_click(r_click_elem).move_to_element(options_elem).click().perform()
#
# alt_obj = driver.switch_to.alert
# print(alt_obj.text)
# alt_obj.accept()


#####################double click
d_click_elem = driver.find_element(By.XPATH, "//button[text()='Double-Click Me To See Alert']")
act_obj.double_click(d_click_elem).perform()
sleep(5)
alt_obj = driver.switch_to.alert
print(alt_obj.text)
alt_obj.accept()