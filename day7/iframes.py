#iframe [previous frames]

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By


service_obj=Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://ui.vision/demo/webtest/frames/")
driver.maximize_window()

frame1_elem = driver.find_element(By.XPATH,"//frameset/frame[1]")

driver.switch_to.frame(frame1_elem)# id /# name/ title /index(trial and error)/ webelemant
driver.find_element(By.XPATH, "//input[@name='mytext1']").send_keys("welcome")

driver.switch_to.default_content()# casc

frame3_elem = driver.find_element(By.XPATH,"//frameset/frame[2]")
driver.switch_to.frame(frame3_elem)
driver.find_element(By.XPATH, "//input[@name='mytext3']").send_keys("welcome")

inner_frame3_elem = driver.find_element(By.XPATH,"//iframe")
driver.switch_to.frame(inner_frame3_elem)
#Form Filling Demo Page
print(driver.find_element(By.XPATH, "//div[text()='Form Filling Demo Page']").is_displayed())

driver.switch_to.parent_frame()# tranfer control to blue frame
driver.find_element(By.XPATH, "//input[@name='mytext3']").send_keys("123456")


driver.switch_to.default_content()
frame1_elem = driver.find_element(By.XPATH,"//frameset/frame[1]")
driver.switch_to.frame(frame1_elem)# id /# name/ title /index(trial and error)/ webelemant
driver.find_element(By.XPATH, "//input[@name='mytext1']").send_keys("123456")
driver.save_screenshot(r".\ss.png")
sleep(10)