import configparser
import os

config = configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+"\\configurations\\pytest.ini")


class ReadConfig:
    @staticmethod
    def get_applications_URL():
        url = config.get('pytest', 'baseURL')
        return url

    @staticmethod
    def get_user_email_id():
        email_id = config.get('pytest', 'email')
        return email_id

    @staticmethod
    def get_password():
        password = config.get('pytest', 'password')
        return password
