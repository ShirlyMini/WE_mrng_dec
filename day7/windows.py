from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By


service_obj=Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# driver.get("https://www.geeksforgeeks.org/")
# driver.maximize_window()
#
# driver.find_element(By.XPATH, " //span[contains(text(),'Explore Community')]").click()
# driver.find_element(By.XPATH, " //span[contains(text(),'Explore Community')]").click()
# driver.find_element(By.XPATH, " //span[contains(text(),'Explore Community')]").click()
# driver.find_element(By.XPATH, " //span[contains(text(),'Explore Community')]").click()
# driver.find_element(By.XPATH, " //span[contains(text(),'Explore Community')]").click()
# print(driver.current_window_handle)# id of current window
# win_id = driver.window_handles# list of id
#
# # driver.switch_to.window(win_id[1])
# sleep(10)
#
# for id in win_id[1:]:#[parent_id, tab1,tab2..]
#     driver.switch_to.window(id)
#     print(driver.find_element(By.XPATH, "//div[contains(text(),'Top Hashtag Trends')]").is_displayed())#True
#
# sleep(20)

#####################################################################
# windows

# driver.get("https://demoqa.com/browser-windows")
# driver.maximize_window()
#
# driver.find_element(By.ID, "windowButton").click()
# print(driver.window_handles)
#
# driver.switch_to.window(driver.window_handles[1])
# print(driver.find_element(By.ID, "sampleHeading").text)
#
# driver.close()# driver focused window
#
# sleep(10)