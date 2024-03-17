##################################################
# Java script generated

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By


# service_obj=Service("E:\selenium\drivers\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)

# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# driver.maximize_window()
#
# driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
#
# alt_ref=driver.switch_to.alert
# print(alt_ref.text)# alert msg
# sleep(3)
# alt_ref.accept()# click ok
#
#
# driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
# print(alt_ref.text)
# sleep(3)
# alt_ref.accept()# click ok
#
# sleep(3)
#
# driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
# print(alt_ref.text)
# sleep(3)
# alt_ref.dismiss()# click cancel
#
#
# driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
# print(alt_ref.text)
# alt_ref.send_keys("welcome")
# sleep(3)
# alt_ref.accept()
# sleep(10)

########################################################################3
# authentication pop up

#http://username:password@url
# driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
# driver.get("https://the-internet.herokuapp.com/basic_auth")
# driver.maximize_window()
#
# print(driver.find_element(By.XPATH, "//div[@class='example']/p").text)
#
# sleep(10)

# using autoit

# import autoit
# driver.get("https://the-internet.herokuapp.com/basic_auth")
#
# autoit.win_wait_active("",30)
# autoit.send("admin{TAB}")
# autoit.send("admin{TAB}")
#
# # autoit.send("{Enter}{TAB}")# if you have checkbox
# autoit.send("{Enter}")
# print(driver.find_element(By.XPATH, "//div[@class='example']/p").text)
# sleep(10)

#https://www.autoitscript.com/autoit3/docs/
# https://github.com/jacexh/pyautoit/tree/master

##########################################################
# notification

service_obj=Service("E:\selenium\drivers\chromedriver.exe")
ops= webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
# ops.accept_insecure_certs()
# ops.add_argument("--allow-insecure-localhost")
# ops.add_argument("--headless")
ops.add_argument("--start-maximized")
driver = webdriver.Chrome(service=service_obj, options=ops)
driver.get("https://whatmylocation.com/")

sleep(60)