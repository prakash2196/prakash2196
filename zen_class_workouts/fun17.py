from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class jay:

    driver = webdriver.Chrome()

    def __init__(self,url):
        self.url = url


    def by_anchor_tag(self,anchor_tag_link):
        try:
            self.driver.get(self.url)
            anchor_tag_link = self.driver.find_element(by = By.LINK_TEXT, value = anchor_tag_link)
            time.sleep(5)
            anchor_tag_link.click()

        except:
            print("anchor tag not found!")

url_1 = "https://www.guvi.in"

s = jay(url_1)

s.by_anchor_tag("Courses")

    