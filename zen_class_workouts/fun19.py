from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class jay:

    driver = webdriver.Chrome()

    def __init__(self,url):
        self.url = url

    def by_class(self,class_name):
        try:
            self.driver.get(self.url)
            class_name = self.driver.find_element(by = By.CLASS, value = class_name)
            time.sleep(7)
            class_name.click()

        except:
            print('class not found !')


url_1 = "https://www.w3schools.com"

s = jay(url_1)

s.by_class("w3-")

