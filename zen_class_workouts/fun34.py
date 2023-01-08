from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class jay:
    driver = webdriver.Chrome()

    def display_per_pages(self):
        self.driver.get('https://www.imdb.com/search/title/')
        self.driver.maximize_window
        user_ratings = self.driver.find_element(by = By.NAME, value = 'user_rating-min')
        user_ratings_dropdown = Select(user_ratings)
        user_ratings_dropdown.select_by_visible_text('6.3')
        display_ratings = self.driver.find_element(by = By.NAME, value = 'count')
        display_ratings_dropdown = Select(display_ratings)
        display_ratings_dropdown.select_by_visible_text('250 per page')
        display_ratings.click()
        time.sleep(9)
        submit_button = self.driver.find_element(by = By.XPATH, value = '//*[@id="main"]/p[3]/button')
        submit_button.click()
        time.sleep(14)

s = jay()

s.display_per_pages()