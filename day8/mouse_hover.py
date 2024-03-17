from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By


service_obj=Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# driver.get("https://www.geeksforgeeks.org/")
# driver.maximize_window()
#
# act_obj = ActionChains(driver)

#//span[text()='Courses']
#//span[text()='For Working Professionals']
#//a[text()='Data Science Training Program']
#
# course_elem = driver.find_element(By.XPATH, "//span[text()='Courses']")
# act_obj.move_to_element(course_elem).perform()
#
# course_cat_elem = driver.find_element(By.XPATH, "//span[text()='For Working Professionals']")
# act_obj.move_to_element(course_cat_elem).perform()
#
# data_sci_elem = driver.find_element(By.XPATH, "//a[text()='Data Science Training Program']")
# act_obj.move_to_element(data_sci_elem).click().perform()
#
# print(driver.title)


#######################tool tip

driver.get("https://demoqa.com/tool-tips")
driver.maximize_window()

act_obj = ActionChains(driver)

button_elem = driver.find_element(By.ID, "toolTipButton")
act_obj.move_to_element(button_elem).perform()
sleep(5)
print(driver.find_element(By.XPATH,'//*[text()="You hovered over the Button"]').is_displayed())