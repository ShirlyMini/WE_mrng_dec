import datetime
#year month date time min sec millisec
# dt_now = datetime.datetime.now()
dt_des_time = datetime.datetime(2025,10,3,12,3,4)
# 01/01/2010 mm/dd/yyyy
print(dt_des_time.strftime("%m/%d/%Y"))

from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



service_obj=Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.automationtesting.in/Datepicker.html")
driver.maximize_window()

# driver.find_element(By.ID, "datepicker2").send_keys(dt_des_time.strftime("%m/%d/%Y"))
driver.find_element(By.ID, "datepicker1").click()

# prev_elem = driver.find_element(By.XPATH,"//a[@title='Prev']/span")
# next_elem = driver.find_element(By.XPATH,"//a[@title='Next']/span")

#//div[@class='ui-datepicker-title']/span[2]
#//div[@class='ui-datepicker-title']/span[1]
year=dt_des_time.strftime("%Y")# 2023
month = dt_des_time.strftime("%B")# oct
date = dt_des_time.strftime("%d")# oct

for _ in range(20):
    year_from_ui = driver.find_element(By.XPATH,"//div[@class='ui-datepicker-title']/span[2]").text
    print(year_from_ui)#2024
    if year_from_ui != year and int(year_from_ui)>int(year):
        driver.find_element(By.XPATH, "//a[@title='Prev']/span").click()

    elif year_from_ui != year and int(year_from_ui) < int(year):
        driver.find_element(By.XPATH, "//a[@title='Next']/span").click()
    elif year_from_ui == year:
        break
# 2023 Dec
calender= {"January":1,
           "February":2,
           "March":3,
           "April":4,"July":7,"August":8,
           "May":5,"September":9,"October":10,
           "June":6,"November":11,
           "December":12,
           }
for _ in range(20):
    mm_from_ui = driver.find_element(By.XPATH, "//div[@class='ui-datepicker-title']/span[1]").text
    print(mm_from_ui)  # Dec
    des_month_in_int = int(dt_des_time.strftime("%m"))#inter format of string
    ui_month_in_int = calender[mm_from_ui]
    if mm_from_ui != month and ui_month_in_int > des_month_in_int:
        driver.find_element(By.XPATH, "//a[@title='Prev']/span").click()
    elif mm_from_ui != month and ui_month_in_int < des_month_in_int:
        driver.find_element(By.XPATH, "//a[@title='Next']/span").click()
    elif mm_from_ui == month:
        break

driver.find_element(By.XPATH,f"//td/a[text()={date}]").click()

if dt_des_time.strftime("%m/%d/%Y") == driver.find_element(By.ID, "datepicker1").get_attribute("value"):
    print(driver.find_element(By.ID, "datepicker1").get_attribute("value"))




sleep(10)




