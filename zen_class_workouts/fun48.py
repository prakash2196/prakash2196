from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import pytest

class Jay:
    url = 'https://www.cowin.gov.in/'
    driver = webdriver.Firefox()
    dashboard = '//*[@id="navbar"]/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[2]/a'

    def window(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(3)
        parent_window = self.driver.current_window_handle
        print("window id for portal",parent_window)
        self.driver.find_element(by = By.XPATH, value = self.dashboard).click()
        all_window_handles = self.driver.window_handles
        print(all_window_handles)
        for i in all_window_handles:
             if( i != parent_window):
                self.driver.switch_to.window(i)
                time.sleep(3)
                self.driver.close()
                break

s = Jay()

s.window()


       



