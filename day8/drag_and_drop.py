from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By


service_obj=Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
# driver.maximize_window()
#
# act_obj = ActionChains(driver)
#
# s1=driver.find_element(By.ID, 'box1')
# s2=driver.find_element(By.ID, 'box2')
# s3=driver.find_element(By.ID, 'box3')
#
# d1=driver.find_element(By.ID, 'box106')
# d2=driver.find_element(By.ID, 'box107')
# d3=driver.find_element(By.ID, 'box101')
#
# act_obj.drag_and_drop(s1,d1).drag_and_drop(s2,d2).drag_and_drop(s3,d3).perform()
# sleep(5)


driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()

act_obj = ActionChains(driver)
elem1 = driver.find_element(By.XPATH, "//div[@id='slider-range']/span[1]")
elem2 = driver.find_element(By.XPATH, "//div[@id='slider-range']/span[2]")
print(elem1.location)#{'x': 59, 'y': 250}
print(elem2.location)#{'x': 59, 'y': 250}

act_obj.drag_and_drop_by_offset(elem1,100, 0).perform()
act_obj.drag_and_drop_by_offset(elem2,-100, 0).perform()

print(elem1.location)
print(elem2.location)