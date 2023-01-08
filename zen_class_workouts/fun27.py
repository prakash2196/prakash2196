from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class jay:
    driver = webdriver.Chrome()

    def instagram_login(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(3)
        username = 'mediocritty-witty'
        password = 'Deivajd@143'

        username_input = self.driver.find_element(by = By.NAME, value = 'username')
        password_input = self.driver.find_element(by = By.NAME, value = 'password')
        submit_button = self.driver.find_element(by = By.XPATH, value = '//*[@id="loginForm"]/div/div[3]')

        username_input.send_keys(username)
        password_input.send_keys(password)
        submit_button.click()
        time.sleep(5)
        print(username_input.text)
        print(password_input.text)

s = jay()

s.instagram_login()