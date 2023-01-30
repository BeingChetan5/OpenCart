import os

import pytest

from pageobject.HomePage import HomePage
from pageobject.AccountRegistrationPage import AccountRegistrationPage
from utilities.customLogger import LogGenerator
from utilities.read_properties import ReadConfig


class TestAccountRegistration:
    baseURL = ReadConfig.get_applications_URL()
    logger = LogGenerator.logger()

    @pytest.mark.bat
    def test_account_registration(self, setup):
        self.logger.info("Getting set up ready for test_account_registration")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.home_page = HomePage(self.driver)
        self.home_page.click_my_account()
        self.home_page.click_register()

        self.reg_page = AccountRegistrationPage(self.driver)

        self.reg_page.set_first_name("Diana")
        self.reg_page.set_last_name("Deerajkar")
        self.reg_page.set_email("dianam5mirajkar@gmail.com")
        self.reg_page.set_password('Dia@8383')
        self.reg_page.set_subscribe()
        self.reg_page.set_privacy_policy()
        self.reg_page.click_continue()
        conf_msg = self.reg_page.get_confirmation_msg()
        print("conf_msg: ", conf_msg)
        if conf_msg == 'Your Account Has Been Created!':
            self.logger.info("Account has been created successfully.")
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"test_account_registration.png")
            self.driver.close()
            pytest.fail("Account is not created.")
