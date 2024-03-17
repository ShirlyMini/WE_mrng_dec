# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from time import sleep
# from selenium.webdriver.common.by import By
#
# service_obj=Service("E:\selenium\drivers\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
# # application commands
# driver.get("https://www.facebook.com/signup")
# print(driver.title)
# print(driver.current_url)#
# if driver.current_url == "https://www.facebook.com/signup":
#     print("url matched")
# print(driver.page_source)

##################################################################

# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.chrome.service import Service
# from time import sleep
# from selenium.webdriver.common.by import By
#
# service_obj=Service("E:\selenium\drivers\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
# conditional commands
# driver.get("https://www.linkedin.com/learning-login")

# is_displayed

# print(driver.find_element(By.ID, "auth-id-button").is_displayed())#True
# print(driver.find_element(By.ID, "auth-id-button").is_enabled())#False
# driver.find_element(By.ID, "auth-id-input").send_keys("shirly")
# print(driver.find_element(By.ID, "auth-id-button").is_displayed())#True
# print(driver.find_element(By.ID, "auth-id-button").is_enabled())#True

# print(driver.find_element(By.ID, "auth-id-button123").is_displayed())#NoSuchElementException

# driver.get("https://www.facebook.com/signup")
# # is_dispalyed works only with hidden element
# print(driver.find_element(By.XPATH, "//input[@name='custom_gender']").is_displayed())#False
# driver.find_element(By.XPATH, "//input[@value='-1']").click()
# print(driver.find_element(By.XPATH, "//input[@name='custom_gender']").is_displayed())#True

# is_selected
#
# driver.get("https://demoqa.com/automation-practice-form")
# driver.maximize_window()
#
# elem = driver.find_element(By.ID, "hobbies-checkbox-1")
# driver.execute_script("arguments[0].scrollIntoView();",elem)


# checkbox
# print(driver.find_element(By.ID, "hobbies-checkbox-1").is_selected())
# driver.find_element(By.XPATH, "//*[@id='hobbiesWrapper']/div[2]/div[1]").click()
#
# print(driver.find_element(By.ID, "hobbies-checkbox-1").is_selected())
# print(driver.find_element(By.XPATH, "//*[@id='hobbiesWrapper']/div[2]/div[1]").is_selected())#False

# radio button
# print(driver.find_element(By.ID, "gender-radio-1").is_selected())# false
# driver.find_element(By.XPATH, "//*[@id='genterWrapper']/div[2]/div[1]").click()
# print(driver.find_element(By.ID, "gender-radio-1").is_selected())# true


#########################################################3

# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.chrome.service import Service
# from time import sleep
# from selenium.webdriver.common.by import By
#
# service_obj=Service("E:\selenium\drivers\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
# quit and close commands
# driver.get("https://www.geeksforgeeks.org/")
# driver.maximize_window()
# driver.find_element(By.XPATH, "//span[contains(text(),'Explore Community')]").click()
# driver.find_element(By.XPATH, "//span[contains(text(),'Explore Community')]").click()
#
# sleep(5)
# driver.close()# driver focuse it will close parent or current windpow
# sleep(10)
# driver.quit()# close all windows

# navigator command
# driver.get("https://www.geeksforgeeks.org/")
# driver.get("https://www.facebook.com/signup")
# driver.back()#geeks for geek
# sleep(3)
# driver.refresh()
# sleep(3)
# driver.forward()# facebook
# sleep(3)
# driver.quit()


##############################################################

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import *

service_obj=Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://money.rediff.com/gainers")
driver.maximize_window()
# driver.implicitly_wait(300)
driver.find_element(By.XPATH, "//a[contains(text(),'Siyaram Recycling In')]").click()

wait_obj=WebDriverWait(driver, 60, 2, ignored_exceptions=[NoSuchElementException, TimeoutException])

wait_obj.until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@id='for_BSE']/h1")))
# wait_obj.until(expected_conditions.alert_is_present())
wait_obj.until(expected_conditions.presence_of_all_elements_located((By.XPATH, "//span")))# works only with xpath matches multiple elem



print(driver.find_element(By.XPATH, "//*[@id='for_BSE']/h1").text)

sleep(10)