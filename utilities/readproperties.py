
import configparser
import os

# Used to read data from the ini.file

config = configparser.RawConfigParser()
config.read(os.path.join(r"C:\Users\yalam\PycharmProjects\opecartv1\Opencart\configurations", "config.ini"))

class readconfig:
    @staticmethod
    def applicationurl():
        url = (config.get('commoninfo','baseurl'))
        return url

    @staticmethod
    def useremail():
        useremail = (config.get('commoninfo', 'email'))
        return useremail

    @staticmethod
    def userpassword():
        userpassword = (config.get('commoninfo', 'password'))
        return userpassword

