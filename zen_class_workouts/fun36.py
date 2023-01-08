from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class jay:
    driver = webdriver.Chrome()

    def __init__(self,url):
        self.url = url

    def by_xpath(self,xpath_url):
        self.driver.get(self.url)
        time.sleep(5)
        xpath_url = self.driver.find_element(by = By.XPATH, value = xpath_url )
        xpath_url.click()

url_1 = 'http://127.0.0.1:5500/ai.html'

s = jay(url_1)

s.by_xpath('//*[@id="jai"]/div[2]/p/a')