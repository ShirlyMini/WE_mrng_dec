# Locators
# Normal locators--->
# ID(fastest locator)(unique)
# Name()
# class
# tag

# linktext
# partial link text

#<input - tag
# type="text"
# class="inputtext _55r1 _6luy"
# name="email"
# id="email"
# data-testid="royal_email"
# placeholder="Email address or phone number"
# autofocus="1"
# aria-label="Email address or phone number">


#####################################################################
# id

# from time import sleep
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common import by
# from selenium.webdriver.common.by import By
#
# service_obj=Service("E:\selenium\drivers\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
#
# driver.get("https://www.facebook.com/")
# driver.find_element(By.ID,"email").send_keys("xyz.gmail.com")
# driver.find_element("id", "pass").send_keys("12345")
#
# sleep(15)
#
# driver.close()

###########################################3
# Name

#
# from time import sleep
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common import by
# from selenium.webdriver.common.by import By
#
# service_obj=Service("E:\selenium\drivers\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
#
# driver.get("https://www.facebook.com/")
# driver.find_element(By.NAME,"email").send_keys("xyz.gmail.com")
# driver.find_element("name", "pass").send_keys("12345")
#
# sleep(15)
#
# driver.close()


###################################################33
# class

# inputtext _55r1 _6luy

#
# from time import sleep
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# service_obj=Service("E:\selenium\drivers\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
#
# driver.get("https://demo.nopcommerce.com/")
# driver.find_element(By.CLASS_NAME,"search-box-text").send_keys("mobile")
#
# sleep(15)
#
# driver.close()


##############################################33
# tag

# from time import sleep
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# service_obj=Service("E:\selenium\drivers\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
#
# driver.get("https://www.facebook.com/")
# driver.find_element(By.TAG_NAME,"button").click()
# # driver.find_element(By.TAG_NAME,"input").send_keys("mobile")
#
# sleep(15)
#
# driver.close()


##############################################3
# # link text <a- anchor tag> <innertext>
# # partial link text


from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.facebook.com/")
# # driver.find_element(By.LINK_TEXT,"Forgotten password?").click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"Forgotten").click()

# driver.find_element(By.LINK_TEXT,"Create new account").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"account").click()

sleep(15)

driver.close()







