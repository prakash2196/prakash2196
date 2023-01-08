from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class jay:
    driver = webdriver.Chrome()

    def fb_login(self):
        self.driver.get('https://www.facebook.com/')
        time.sleep(5)

        username = '9944104323'
        password = 'deivajd143'

        username_input = self.driver.find_element(by = By.NAME, value = 'email')
        password_input = self.driver.find_element(by = By.NAME, value = 'pass')
        submit_button = self.driver.find_element(by = By.NAME, value = 'login')

        username_input.send_keys(username)
        password_input.send_keys(password)
        submit_button.click()
        time.sleep(18)

s = jay()

s.fb_login()

