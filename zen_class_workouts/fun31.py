from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class jay:
    driver =webdriver.Chrome()

    def gmail_login(self):
        self.driver.get("https://accounts.google.com/v3/signin/identifier?dsh=S-1090364547%3A1670582461842037&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AeAAQh4rvASHRJtbZCFAbraNdV3nKrTeo0idp0jDWqJu8oKyAwHIQPNchLarD6Zt0Y5B7MflNZ8cWQ")
        time.sleep(5)
        username = 'prakashjd2196@gmail.com'

        username_input = self.driver.find_element(by = By.NAME, value = 'identifier')
        submit_button = self.driver.find_element(by = By.XPATH, value = '//*[@id="identifierNext"]/div/button/span')

        username_input.send_keys(username)
        submit_button.click()
        time.sleep(9)

        password = 'deivajd143'

        password_input = self.driver.find_element(by = By.NAME, value = 'Passwd')
        submit_button = self.driver.find_element(by = By.XPATH, value = '//*[@id="passwordNext"]/div/button/span')

        password_input = 'password'
        submit_button.click()
        time.sleep(14)



s = jay()

s.gmail_login()