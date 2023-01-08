from selenium import webdriver
from selenium.webdriver.common.by import By
options = webdriver.FirefoxOptions()
options.add_argument('--headless')
import time

class jay:

    driver = webdriver.Firefox()

    def __init__(self,url):
        self.url = url

    def by_anchor_tag(self,anchor_tag_link):
        try:
            driver = webdriver.Firefox(firefox_options=options)
            self.driver.get(self.url)
            anchor_tag_link = self.driver.find_element(by = By.LINK_TEXT , value = anchor_tag_link)
            time.sleep(7)
            anchor_tag_link.click()

        except:
            print("anchor tag not found !")

url_1 = "https://www.w3schools.com"

s = jay(url_1)

s.by_anchor_tag("HTML Reference")
