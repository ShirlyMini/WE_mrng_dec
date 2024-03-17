# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from time import sleep
# from selenium.webdriver.common.by import By
#
# service_obj=Service("E:\selenium\drivers\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
#
# driver.get("https://www.facebook.com/signup")
# xpath matching single element
# driver.find_element(By.XPATH, "//input[@name='firstname']").send_keys("myname")

# we_list = driver.find_elements(By.XPATH, "//input[@name='firstname']")# return list of webelements
# print(we_list)
# for i in we_list:
#     i.send_keys("myname")


# xpath matching multiple element
# driver.find_element(By.XPATH, "//input[@type='text']").send_keys("myname")

# we_list = driver.find_elements(By.XPATH, "//input[@type='text']")# return list of webelements
# print(we_list)#6
# for i in we_list[0:3]:
#     i.send_keys("myname")

# invalid xpath
# driver.find_element(By.XPATH, "//input[@type='text123']").send_keys("myname")#NoSuchElementException
# we_list = driver.find_elements(By.XPATH, "//input[@type='text123']")# return list of webelements
# print(we_list)#[]
#
# sleep(10)
# driver.quit()


#################################################################3

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from time import sleep
# from selenium.webdriver.common.by import By
#
# service_obj=Service("E:\selenium\drivers\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
#
# driver.get("https://www.facebook.com/signup")
# # clear
# name_we = driver.find_element(By.XPATH, "//input[@name='firstname']")
# name_we.send_keys("myname")
# print(name_we.text)
# print(name_we.get_attribute("value"))
# print(name_we.get_attribute("id"))
# print(name_we.get_attribute("class"))
# name_we.clear()
#
# name_we.send_keys("name12345")
# print(name_we.get_attribute("value"))
#
# sleep(10)
# driver.quit()

#################################################33

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By

service_obj=Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.facebook.com/signup")
# clear
we_list = driver.find_elements(By.XPATH, "//div[@class='placeholder']")
for i in we_list:
    print(i.text)

sleep(10)
driver.quit()