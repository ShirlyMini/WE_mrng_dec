# customized locators---->
# css

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
# # tag/id
# driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("xyz.gmail.com")
# driver.find_element(By.CSS_SELECTOR, "#pass").send_keys("12345")
#
# sleep(15)
#
# driver.close()


###############################################33
# tag/class
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
# driver.find_element(By.CSS_SELECTOR,".search-box-text").send_keys("mobile")
#
# sleep(15)
#
# driver.close()


# tag/attr eg.  input[data-testid=royal_email]
# tag/class/attr eg.   button.button-1[type=submit]


########################################################################333
########################################################################33
# xpath

# relative
# abs

from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.nopcommerce.com/")
driver.find_element(By.XPATH,"//ul[@class='top-menu notmobile']/li/a[text()='Apparel ']").click()

sleep(15)

driver.close()

#https://money.rediff.com/feedback
# and  eg //input[@type='text' and @name='username']
# or   eg //input[@type='text' or @name='username']

# contains()--func-->//input[contains(@name,"email")] or //input[contains(@name,"emailId")]
#//b[contains(text(),"Enter characters")]

# start-with ---//*[starts-with(text(),"Enter")]
#//*[starts-with(@name,"user")]


##############################################33
# //a[contains(text(),'Tera Software')]/self::a
#//a[contains(text(),'Tera Software')]/parent::td/parent::tr
#//a[contains(text(),'Tera Software')]/parent::td/parent::tr/child::td/child::a

#//a[contains(text(),'Tera Software')]/parent::td/following-sibling::td
#//a[contains(text(),'Tera Software')]/parent::td/following::td

#//a[contains(text(),'Tera Software')]/parent::td/parent::tr/td[3]/preceding::td
#//a[contains(text(),'Tera Software')]/parent::td/parent::tr/td[3]/preceding-sibling::td

# descendant try
# descendant-or-self try
