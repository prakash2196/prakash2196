from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
import time
import pytest

class test_jay:
    url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'

    driver = webdriver.Firefox()

    username = 'Admin'
    password = 'admin123'
    input_box_username = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input'
    input_box_password = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input'
    login_xpath = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'

    def get_cookies(self):
        self.driver.maximize_window()
        time.sleep(4)
        self.driver.get(self.url)
        time.sleep(4)
        cookie = self.driver.get_cookies()
        cookie_before_login = cookie[0]['value']
        print("initial value of cookies before login",cookie_before_login)
        time.sleep(3)
        self.driver.find_element(by = By.XPATH, value = self.input_box_username).send_keys(self.username)
        self.driver.find_element(by = By.XPATH, value = self.input_box_password).send_keys(self.password)
        self.driver.find_element(by = By.XPATH, value = self.login_xpath).click()
        cookie = self.driver.get_cookies()
        cookie_after_login = cookie[0]['value']
        print("cookies_after_login_success",cookie_after_login)
        if(cookie_before_login != cookie_after_login):
            print("Login success. before_login_cookie is {a} and after_login_cookie is {b}".format( a = cookie_before_login ,  b = cookie_after_login ))
        else:
            print("error not found")

s = test_jay()

s.get_cookies()
