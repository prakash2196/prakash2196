from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class jay:
    driver = webdriver.Chrome()

    def __init__(self,url):
        self.url = url

    def login_orangehrm(self):
        self.driver.maximize_window
        self.driver.get(self.url)
        time.sleep(5)

        username = 'Admin'
        password = 'admin123'

        username_input = self.driver.find_element(by = By.NAME, value = "username")
        password_input = self.driver.find_element(by = By.NAME, value = "password")
        login_input = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')

        username_input.send_keys(username)
        password_input.send_keys(password)
        login_input.send_keys(Keys.ENTER)
        time.sleep(27)

url_1 = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'

s = jay(url_1)

s.login_orangehrm()