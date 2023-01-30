import pytest
import os

from pageobject.HomePage import HomePage
from pageobject.LoginPage import LoginPage

from utilities.customLogger import LogGenerator
from utilities.read_properties import ReadConfig


class TestLogin:
    baseURL = ReadConfig.get_applications_URL()
    email = ReadConfig.get_user_email_id()
    password = ReadConfig.get_password()
    logger = LogGenerator.logger()

    @pytest.mark.sanity
    def test_login(self, setup):
        self.logger.info("Getting set up ready for test_account_registration")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.home_page = HomePage(self.driver)
        self.home_page.click_my_account()
        self.home_page.click_login()

        self.login_page = LoginPage(self.driver)
        self.login_page.enter_email(self.email)
        self.login_page.enter_password(self.password)
        self.login_page.click_login()
        logged_in = self.login_page.verify_login()
        if logged_in:
            self.logger.info("Logged in successfully.")
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"test_login.png")
            self.driver.close()
            pytest.fail("Login failed.")
