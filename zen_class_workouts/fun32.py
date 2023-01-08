from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class jay:
    driver = webdriver.Chrome()

    def __init__(self,url):
        self.url = url

    def select_by_user_ratings(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        user_ratings = self.driver.find_element(by = By.NAME, value = 'user_rating-min')
        user_ratings.click()
        time.sleep(7)

url = "https://www.imdb.com/search/title/"

s = jay(url)

s.select_by_user_ratings()
