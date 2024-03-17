from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



service_obj=Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# driver.get("https://books-pwakit.appspot.com/")
# driver.maximize_window()
#
# # driver.find_element(By.ID, "input").send_keys("Books")
# driver_shadow1= driver.find_element(By.CSS_SELECTOR,'book-app').shadow_root
# driver_shadow1.find_element(By.CSS_SELECTOR,"input#input").send_keys("Books")
#
# sleep(10)


driver.get("chrome://settings/downloads")
driver.maximize_window()

# driver.find_element(By.ID, "input").send_keys("Books")
driver_shadow1= driver.find_element(By.CSS_SELECTOR,'settings-ui').shadow_root
driver_shadow2= driver_shadow1.find_element(By.CSS_SELECTOR,'settings-main#main').shadow_root
driver_shadow3= driver_shadow2.find_element(By.CSS_SELECTOR,'settings-basic-page.cr-centered-card-container').shadow_root
driver_shadow4= driver_shadow3.find_element(By.CSS_SELECTOR,'settings-downloads-page').shadow_root
driver_shadow5= driver_shadow4.find_element(By.CSS_SELECTOR,'settings-toggle-button.hr').shadow_root


print(driver_shadow5.find_element(By.CSS_SELECTOR,"div#labelWrapper.flex").text)

sleep(10)