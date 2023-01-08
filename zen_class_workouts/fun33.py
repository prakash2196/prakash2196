from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class jay:
    driver = webdriver.Chrome()

    def __init__(self,url):
        self.url = url

    def display_per_page(self):
        self.driver.maximize_window
        self.driver.get(self.url)
        user_ratings = self.driver.find_element(by = By.NAME, value = 'user_rating-min')
        user_ratings_dropdown = Select(user_ratings)
        user_ratings_dropdown.select_by_visible_text('7.2')
        time.sleep(14)

url = "https://www.imdb.com/search/title/"

s = jay(url)

s.display_per_page()