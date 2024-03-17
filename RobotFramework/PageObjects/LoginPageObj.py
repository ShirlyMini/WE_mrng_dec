
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class LoginPageObj:
    id_email="Email"
    id_password="Password"
    xpath_login = "//button[@type='submit']"
    xpath_dashbord_title="//h1[contains(text(),'Dashboard')]"
    xpath_logout="//a[contains(text(),'Logout')]"

    # def __init__(self,driver):
    #     self.driver = driver
    #     self.wait_obj=WebDriverWait(self.driver,60)

    def SetEmail(self, driver, email):
        driver.find_element(By.ID, self.id_email).clear()
        driver.find_element(By.ID, self.id_email).send_keys(email)

    def SetPassword(self, driver, pswd):
        driver.find_element(By.ID, self.id_password).clear()
        driver.find_element(By.ID, self.id_password).send_keys(pswd)

    def ClickSubmit(self, driver):
        driver.find_element(By.XPATH, self.xpath_login).click()

    def VerifyDashbord(self, driver):
        try:
            return driver.find_element(By.XPATH, self.xpath_dashbord_title).is_displayed()
        except Exception as msg:
            return False

    def ClickLogout(self, driver):
        # self.wait_obj.until(expected_conditions.element_to_be_clickable((By.XPATH, self.xpath_logout)))
        driver.find_element(By.XPATH, self.xpath_logout).click()
