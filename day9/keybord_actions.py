from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



service_obj=Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# driver.get("https://jqueryui.com/autocomplete/#multiple")
# driver.maximize_window()
#
# driver.switch_to.frame(driver.find_element(By.CLASS_NAME,'demo-frame'))
# sleep(3)
# driver.find_element(By.ID, 'tags').send_keys("a")
# sleep(2)
#
# list_of_elem = driver.find_elements(By.XPATH, "//ul[@id='ui-id-1']/li/div")
# print(list_of_elem)
# for elem in list_of_elem:
#     print(elem.text)
#     if elem.text == "BASIC":
#         elem.click()
#
# print(driver.find_element(By.ID,"tags").get_attribute("value"))

# driver.get("https://jqueryui.com/autocomplete/")
# driver.maximize_window()
#
# driver.switch_to.frame(driver.find_element(By.CLASS_NAME,'demo-frame'))#id, titile,index
# driver.find_element(By.ID,"tags").send_keys("a")
#
# driver.find_element(By.ID,"tags").send_keys(Keys.ARROW_DOWN)
# for _ in range(15):
#     sleep(1)
#     if driver.find_element(By.ID,"tags").get_attribute("value") == "Java":
#         driver.find_element(By.ID, "tags").send_keys(Keys.ENTER)
#         break
#     else:
#         driver.find_element(By.ID, "tags").send_keys(Keys.ARROW_DOWN)
#
#
# sleep(10)

driver.get("https://www.geeksforgeeks.org/")
driver.maximize_window()

act_obj = ActionChains(driver)
driver.find_element(By.LINK_TEXT,'Sign In').click()
sleep(3)
driver.find_element(By.XPATH,"//label[contains(text(),'Sign Up')]").click()
driver.find_element(By.ID,"email").send_keys("abc@gmail.com")

# ctrl+a and ctrl+c

act_obj.key_down(Keys.CONTROL).send_keys("a").send_keys("c").key_up(Keys.CONTROL).perform()
# act_obj.key_down(Keys.CONTROL).key_down(Keys.SHIFT).send_keys("i").key_up(Keys.SHIFT).key_up(Keys.CONTROL).perform()
# tab
act_obj.send_keys(Keys.TAB).perform()
#ctrl+v
act_obj.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

# tab
act_obj.send_keys(Keys.TAB).perform()
#ctrl+v
act_obj.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

sleep(10)

