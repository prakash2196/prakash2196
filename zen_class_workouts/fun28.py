from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class jay:
    driver = webdriver.Edge()

    def gmail_login(self):
        self.driver.get('https://accounts.google.com')
        time.sleep(5)
        email = 'prakashjai2811@gmail.com'
        
        email_input = self.driver.find_element(by = By.XPATH, value = '//*[@id="identifierId"]')
        next_button = self.driver.find_element(by = By.XPATH, value = '//*[@id="identifierNext"]/div/button/div[3]')
        
        email_input.send_keys(email)
        next_button.click()
        time.sleep(7)

s = jay()

s.gmail_login()

