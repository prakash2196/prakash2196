from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class jay:

    driver = webdriver.Chrome()

    def __init__ (self,url):
        self.url = url

    def by_id(self,id_link):
        self.driver.get(self.url)
        id_link = self.driver.find_element(by = By.ID,value = id_link)
        time.sleep(4)
        id_link.click()

url_1 = 'https://www.w3schools.com'

s = jay(url_1)

s.by_id('getdiploma')

