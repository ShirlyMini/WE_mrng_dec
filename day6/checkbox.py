from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By


service_obj=Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# driver.get("https://demoqa.com/automation-practice-form")
# driver.maximize_window()
#
# elem = driver.find_element(By.ID, "hobbies-checkbox-1")
# driver.execute_script("arguments[0].scrollIntoView();",elem)


# checkbox
# print(driver.find_element(By.ID, "hobbies-checkbox-1").is_selected())
# # driver.find_element(By.XPATH, "//*[@id='hobbiesWrapper']/div[2]/div[1]").click()
#
#
#
# print(driver.find_element(By.ID, "hobbies-checkbox-1").is_selected())
# print(driver.find_element(By.XPATH, "//*[@id='hobbiesWrapper']/div[2]/div[1]").is_selected())#False
# check bo to select multiple options
# elm_list = driver.find_elements(By.XPATH, "//*[@id='hobbiesWrapper']/div[2]/div")
# print(elm_list)#---list of webelem
# for i in range(1,len(elm_list)+1):# len 3= 0,1,2
#     if driver.find_element(By.XPATH, f"//*[@id='hobbiesWrapper']/div[2]/div[{i}]/label").text in ["Sports", "Music"]:
#         driver.find_element(By.XPATH, f"//*[@id='hobbiesWrapper']/div[2]/div[{i}]").click()
#         print(driver.find_element(By.XPATH, f"//*[@id='hobbiesWrapper']/div[2]/div[{i}]/input").is_selected())# input tags
#     else:
#         print(driver.find_element(By.XPATH, f"//*[@id='hobbiesWrapper']/div[2]/div[{i}]/input").is_selected())
#
# sleep(10)


# radio button
# print(driver.find_element(By.ID, "gender-radio-1").is_selected())# false
# driver.find_element(By.XPATH, "//*[@id='genterWrapper']/div[2]/div[1]").click()
# print(driver.find_element(By.ID, "gender-radio-1").is_selected())# true

###################################################################3
# dropdown

# with select tag
# from selenium.webdriver.support.select import Select
#
# driver.get("https://www.facebook.com/signup")
# driver.maximize_window()
#
# drp_down_obj = Select(driver.find_element(By.ID, "day"))
# drp_down_obj.select_by_value("1")
# sleep(5)
# drp_down_obj.select_by_visible_text("27")
# sleep(5)
# drp_down_obj.select_by_index(0)# starts from 0 to n-1
# sleep(5)
# print(drp_down_obj.all_selected_options[0].text)


# without tag
# from selenium.webdriver import ActionChains
# driver.get("https://www.geeksforgeeks.org/")
# driver.maximize_window()
#
# act_obj  = ActionChains(driver)
# act_obj.move_to_element(driver.find_element(By.XPATH, "//span[contains(text(),'Tutorials')]")).\
#  move_to_element(driver.find_element(By.XPATH, "//span[contains(text(),'Tutorials')]/following-sibling::ul[@class='mega-dropdown']/li[1]/span")).\
#  click(driver.find_element(By.XPATH, "//span[contains(text(),'Tutorials')]/following-sibling::ul[@class='mega-dropdown']/li[1]/ul/li[1]")).\
#  perform()
#
# sleep(10)

###########################################################################3
# autocomplete

# driver.get("https://www.geeksforgeeks.org/")
# driver.maximize_window()
#
# driver.find_element(By.XPATH, "//input[@class='ant-input ant-input-lg']").send_keys("pyt")
# sleep(5)
# ele_list=driver.find_elements(By.XPATH, "//div[@class='gfg_home_page_search_suggestion_box_collection_item ']/span")
# for i in ele_list:
#     print(i.text)
#
#
# sleep(10)

##########################################################33

# links
# import requests
#
# driver.get("http://www.deadlinkcity.com/")
# driver.maximize_window()
#
# elem_list = driver.find_elements(By.XPATH, "//a")
# for link in elem_list:
#     try:
#
#         url = link.get_attribute("href")
#         status = requests.get(url)
#         # print(status)#<Response [450]>
#         print(url, status.status_code)
#         if status.status_code >=400:
#             print("invalid url")
#         else:
#             print("valid url")
#     except Exception as msg:
#         print(f"{msg}")

##################################################
# upload

# driver.get("https://www.foundit.in/")
# driver.maximize_window()
#
# driver.find_element(By.XPATH, "//div[contains(text(),'Upload Resume')]").click()
# driver.find_element(By.ID, "file-upload").send_keys(r"C:\Users\user\Downloads\pdfcatalog.pdf")
#
# sleep(10)

import autoit

driver.get("https://www.foundit.in/")
driver.maximize_window()

driver.find_element(By.XPATH, "//div[contains(text(),'Upload Resume')]").click()
sleep(10)
driver.find_element(By.ID, "file-upload").click()

autoit.win_wait_active("",30)
autoit.send(r"C:\Users\user\Downloads\pdfcatalog.pdf")
autoit.send("{Enter}")

sleep(10)