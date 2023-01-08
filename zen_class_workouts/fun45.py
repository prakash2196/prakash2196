from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest
from selenium.webdriver.common.action_chains import ActionChains

class Test_Jay:
    url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'

    driver = webdriver.Firefox()

    username = 'Admin'
    password = 'admin123'

    input_box_username = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input'
    input_box_password = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input'
    login_xpath = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    logout_xpath = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span'

    def logout_xpath(self):
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.find_element(by = By.XPATH, value = self.input_box_username).send_keys(self.username)
        self.driver.find_element(by = By.XPATH, value = self.input_box_password).send_keys(self.password)
        self.driver.find_element(by = By.XPATH, value = self.login_xpath).click()
        time.sleep(3)
        logout_button =  self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span')
        action = ActionChains(self.driver)
        action.click(on_element = logout_button).perform()
        time.sleep(3)
        self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a').click()


s = Test_Jay()

s.logout_xpath()


