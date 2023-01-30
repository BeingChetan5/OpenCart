from selenium.webdriver.common.by import By


class HomePage:
    lnk_myaccount_cl_name = "d-md-inline"
    lnk_register_linktext = "Register"
    lnk_login_linktext = "Login"

    def __init__(self, driver):
        self.driver = driver

    def click_my_account(self):
        elements = self.driver.find_elements(By.CLASS_NAME, self.lnk_myaccount_cl_name)
        for element in elements:
            if element.text == "My Account":
                element.click()
                break

    def click_register(self):
        self.driver.find_element(By.LINK_TEXT, self.lnk_register_linktext).click()

    def click_login(self):
        self.driver.find_element(By.LINK_TEXT, self.lnk_login_linktext).click()