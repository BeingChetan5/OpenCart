from selenium.webdriver.common.by import By
import time

class AccountRegistrationPage:
    txt_firstname_name = "firstname"
    txt_lastname_name = "lastname"
    txt_email_name = "email"
    txt_telephone_name = "telephone"
    txt_password_name = "password"
    chk_subscribe_css_sel = "input[id='input-newsletter-yes']"
    chk_policy_css_sel = "input[name='agree']"
    btn_continue_cl_name = "btn-primary"
    txt_conf_msg_xpath = "//h1[normalize-space()='Your Account Has Been Created!']"

    def __init__(self, driver):
        self.driver = driver

    def set_first_name(self, first_name):
        self.driver.find_element(By.NAME, self.txt_firstname_name).send_keys(first_name)

    def set_last_name(self, last_name):
        self.driver.find_element(By.NAME, self.txt_lastname_name).send_keys(last_name)

    def set_email(self, email):
        self.driver.find_element(By.NAME, self.txt_email_name).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(By.NAME, self.txt_password_name).send_keys(password)

    def set_subscribe(self):
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, self.chk_subscribe_css_sel).click()

    def set_privacy_policy(self):
        self.driver.find_element(By.CSS_SELECTOR, self.chk_policy_css_sel).click()

    def click_continue(self):
        self.driver.find_element(By.CLASS_NAME, self.btn_continue_cl_name).click()
        time.sleep(10)

    def get_confirmation_msg(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_conf_msg_xpath).text
        except:
            return None
