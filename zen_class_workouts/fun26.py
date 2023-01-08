from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class jay:
    driver =  webdriver.Chrome()

    def search_yahoo(self,search_param):
        self.driver.get("https://www.yahoo.com")
        search_box = self.driver.find_element(by = By.NAME, value = 'p')
        search_box.send_keys(search_param)
        time.sleep(3)
        search_box.send_keys(Keys.ENTER)

s = jay()

s.search_yahoo("India wikipedia")