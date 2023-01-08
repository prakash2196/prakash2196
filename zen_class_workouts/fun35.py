from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class jay:
    driver = webdriver.Chrome()

    def __init__(self,url):
        self.url = url

    def select_by_user_ratings(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        user_ratings = self.driver.find_element(by = By.NAME, value = "user_rating-min")
        user_ratings_dropdown = Select(user_ratings)
        user_ratings_dropdown.select_by_visible_text('7.2')
        user_ratings.click()
        time.sleep(7)

    def display_per_page(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        display_pages = self.driver.find_element(by = By.NAME, value = 'count')
        display_ratings = Select(display_pages)
        display_ratings.select_by_value('100')
        display_pages.click()
        time.sleep(14)

    def select_by_language(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        language = self.driver.find_element(by = By.NAME, value = 'languages')
        language = Select(language)
        language.select_by_value('hi')
        #language_dropdown = Select(language)
        #language_dropdown.select_by_value('hi')
        #language_dropdown.select_by_visible_text('Hokkien')
        #language.click()
        time.sleep(14)

    def select_multiple_languages(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        language = self.driver.find_element(by = By.NAME, value = 'languages')
        language = Select(language)
        language.select_by_value('de')
        time.sleep(3)
        language.select_by_value('kfa')
        time.sleep(7)
        language.select_by_value('ml')
        time.sleep(12)

    def disselect_multiple_languages(self):
        language = self.driver.find_element(by = By.NAME, value = 'languages')
        language_dropdown = Select(language)
        language_dropdown.deselect_by_value('ml')
        time.sleep(3)
        language_dropdown.deselect_by_value('kfa')
        time.sleep(7)
        language_dropdown.deselect_by_value('de')
        time.sleep(9)

    def select_by_text(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        time.sleep(3)
        title_data = self.driver.find_element(by = By.NAME, value = 'has')
        title_data = Select(title_data)
        title_data.select_by_visible_text('Alternate Versions')
        time.sleep(7)
        title_data.select_by_visible_text('Quotes')
        time.sleep(12)
        title_data.select_by_visible_text('Goofs')
        time.sleep(9)

    def disselect_by_text(self):
        title_data = self.driver.find_element(by = By.NAME, value = 'has')
        tite_data = Select(title_data)
        title_data.deselect_by_visible_text('Quotes')
        time.sleep(7)
        title_data.deselect_by_visible_text('Alternate Versions')
        time.sleep(9)

    def select_by_country(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        time.sleep(3)
        country = self.driver.find_element(by = By.NAME, value = 'countries')
        country = Select(country)
        country.select_by_value('dz')
        time.sleep(5)
        country.select_by_visible_text('Angola')
        time.sleep(9)

    def deselect_by_country(self):
        country = self.driver.find_element(by = By.NAME, value = 'countries')
        country= Select(country)
        country.deselect_by_value('ao')
        time.sleep(5)

    def select_all(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        language = self.driver.find_element(by = By.NAME, value = 'languages')
        language = Select(language)
        language_options = language.options
        for i in language_options:
            i.click()
        #country = self.driver.find_element(by = By.NAME, value = 'countries')
        #country = Select(country)
        #country_options = country.options
        #for i in country_options:
        #    i.click()

    def select_by_genres(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        genre_type = self.driver.find_element(by = By.XPATH, value = '//*[@id="main"]/div[6]/div[2]/table/tbody/tr[2]/td[2]/label')
        genre_type.click()
        time.sleep(5)
        genre_type_1 = self.driver.find_element(by = By.XPATH, value = '//*[@id="main"]/div[6]/div[2]/table/tbody/tr[1]/td[2]/label')
        genre_type_1.click()
        time.sleep(7)






url_1 = 'https://www.imdb.com/search/title/'

s = jay(url_1)

s.select_by_genres()

#s.select_all()

#s.select_by_country()
#s.deselect_by_country()

#s.select_by_text()

#s.disselect_by_text()

#s.select_multiple_languages()
#time.sleep(7)
#s.disselect_multiple_languages()

#s.select_by_language()

#s.display_per_page()

#s.select_by_user_ratings()
