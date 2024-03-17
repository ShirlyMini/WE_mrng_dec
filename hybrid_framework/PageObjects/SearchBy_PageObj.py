from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class SearchBy:
    xpath_customer_menu="//ul[@role='menu']/li/a/p[contains(text(),'Customers')]"
    xpath_customer_item="//ul[@role='menu']/li//ul/li[1]/a/p[contains(text(),'Customers')]"
    id_email_search = "SearchEmail"
    id_firstname_search = "SearchFirstName"
    id_lastname_serach = "SearchLastName"
    xpath_email_col="//tbody/tr/td[2]"
    xpath_name_col="//tbody/tr/td[3]"
    id_search_button="search-customers"

    def __init__(self,driver):
        self.driver = driver
        self.wait_obj=WebDriverWait(self.driver,60)

    def NavigateToCustomerMenu(self):
        sleep(2)
        self.driver.find_element(By.XPATH, self.xpath_customer_menu).click()
        sleep(2)
        self.driver.find_element(By.XPATH, self.xpath_customer_item).click()

    def SearchEmail(self, email):
        self.driver.find_element(By.ID, self.id_email_search).send_keys(email)

    def SearchFirstname(self, name):
        self.driver.find_element(By.ID, self.id_firstname_search).send_keys(name)

    def SearchLastname(self, name):
        self.driver.find_element(By.ID, self.id_lastname_serach).send_keys(name)

    def ClickSearch(self):
        self.driver.find_element(By.ID, self.id_search_button).click()

    def GetEmailColumn(self):
        email_we = self.driver.find_elements(By.XPATH, self.xpath_email_col)
        search_output = []
        for elem in email_we:
            search_output.append(elem.text)
        return search_output

    def GetNameColumn(self):
        name_we = self.driver.find_elements(By.XPATH, self.xpath_name_col)
        search_output = []
        for elem in name_we:
            search_output.append(elem.text)
        return search_output

