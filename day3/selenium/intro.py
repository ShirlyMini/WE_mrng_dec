from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# webdriver.Chrome()# fetch from website
service_obj=Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.facebook.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
print(driver.page_source)
driver.minimize_window()
driver.refresh()
driver.get("https://money.rediff.com/gainers")
driver.back()
print("after clicking back",driver.current_url)
sleep(10)
driver.forward()
print("after clicking forward",driver.current_url)

driver.close()
driver.quit()


