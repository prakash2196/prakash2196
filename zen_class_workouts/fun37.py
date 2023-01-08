from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class jay:
    driver = webdriver.Chrome()

    def __init__(self,url):
        self.url = url

    def login_facebook(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        time.sleep(3)
        username = '9786855897'
        password = 'prakashJD'

        username_input = self.driver.find_element(by = By.XPATH, value = '//*[@id="email"]')
        password_input = self.driver.find_element(by = By.XPATH, value = '//*[@id="pass"]')
        submit_input = self.driver.find_element(by = By.XPATH, value = '//*[@id="loginbutton"]')

        username_input.send_keys(username)
        password_input.send_keys(password)
        submit_input.send_keys(Keys.ENTER)
        time.sleep(9)

url_1 = "https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=100"

s = jay(url_1)

s.login_facebook()