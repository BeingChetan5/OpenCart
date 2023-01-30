from selenium.webdriver.common.by import By


class LoginPage:
    txt_email_css_sel = "input[name='email']"
    txt_passwrd_css_sel = "input[name='password'"
    btn_login_css_sel = "button[type='submit']"

    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, email):
        self.driver.find_element(By.CSS_SELECTOR, self.txt_email_css_sel).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.CSS_SELECTOR, self.txt_passwrd_css_sel).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_login_css_sel).click()

    def verify_login(self):
        try:
            return self.driver.find_element(By.XPATH, "//h2[text()='My Account']").is_displayed()
        except:
            return False
