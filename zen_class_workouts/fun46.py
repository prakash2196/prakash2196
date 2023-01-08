from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest
from selenium.webdriver.common.action_chains import ActionChains

class Test_Jay:

    url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'

    driver = webdriver.Firefox()

    username = 'Admin'
    password = 'admin123'
    Admin = 'Admin'

    input_box_username = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input'
    input_box_password = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input'
    login_xpath = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'

    def search_admin(self,search_param):
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.find_element(by = By.XPATH, value = self.input_box_username).send_keys(self.username)
        self.driver.find_element(by = By.XPATH, value = self.input_box_password).send_keys(self.password)
        self.driver.find_element(by = By.XPATH, value = self.login_xpath).click()
        time.sleep(3)

        search_xpath = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')
        search_xpath.send_keys(search_param)
        time.sleep(3)
        search_xpath.send_keys(Keys.ENTER)
        admin_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span').click()

    def search_PIM(self,search_param):
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.find_element(by = By.XPATH, value = self.input_box_username).send_keys(self.username)
        self.driver.find_element(by = By.XPATH, value = self.input_box_password).send_keys(self.password)
        self.driver.find_element(by = By.XPATH, value = self.login_xpath).click()
        time.sleep(3)
        search_xpath = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')
        search_xpath.send_keys(search_param)
        time.sleep(3)
        search_xpath.send_keys(Keys.ENTER)
        admin_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span').click()

    def search_Leave(self,search_param):
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.find_element(by = By.XPATH, value = self.input_box_username).send_keys(self.username)
        self.driver.find_element(by = By.XPATH, value = self.input_box_password).send_keys(self.password)
        self.driver.find_element(by = By.XPATH, value = self.login_xpath).click()
        time.sleep(3)

        search_xpath = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')
        search_xpath.send_keys(search_param)
        time.sleep(3)
        search_xpath.send_keys(Keys.ENTER)
        admin_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span').click()

    def search_Time(self,search_param):
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.find_element(by = By.XPATH, value = self.input_box_username).send_keys(self.username)
        self.driver.find_element(by = By.XPATH, value = self.input_box_password).send_keys(self.password)
        self.driver.find_element(by = By.XPATH, value = self.login_xpath).click()
        time.sleep(3)

        search_xpath = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')
        search_xpath.send_keys(search_param)
        time.sleep(3)
        search_xpath.send_keys(Keys.ENTER)
        admin_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span').click()

    def search_Recruitment(self,search_param):
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.find_element(by = By.XPATH, value = self.input_box_username).send_keys(self.username)
        self.driver.find_element(by = By.XPATH, value = self.input_box_password).send_keys(self.password)
        self.driver.find_element(by = By.XPATH, value = self.login_xpath).click()
        time.sleep(3)

        search_xpath = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')
        search_xpath.send_keys(search_param)
        time.sleep(3)
        search_xpath.send_keys(Keys.ENTER)
        admin_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span').click()

    def search_My_Info(self,search_param):
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.find_element(by = By.XPATH, value = self.input_box_username).send_keys(self.username)
        self.driver.find_element(by = By.XPATH, value = self.input_box_password).send_keys(self.password)
        self.driver.find_element(by = By.XPATH, value = self.login_xpath).click()
        time.sleep(3)

        search_xpath = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')
        search_xpath.send_keys(search_param)
        time.sleep(3)
        search_xpath.send_keys(Keys.ENTER)
        admin_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span').click()

    def search_Performance(self,search_param):
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.find_element(by = By.XPATH, value = self.input_box_username).send_keys(self.username)
        self.driver.find_element(by = By.XPATH, value = self.input_box_password).send_keys(self.password)
        self.driver.find_element(by = By.XPATH, value = self.login_xpath).click()
        time.sleep(3)

        search_xpath = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')
        search_xpath.send_keys(search_param)
        time.sleep(3)
        search_xpath.send_keys(Keys.ENTER)
        admin_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span').click()

    def search_Dashboard(self,search_param):
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.find_element(by = By.XPATH, value = self.input_box_username).send_keys(self.username)
        self.driver.find_element(by = By.XPATH, value = self.input_box_password).send_keys(self.password)
        self.driver.find_element(by = By.XPATH, value = self.login_xpath).click()
        time.sleep(3)

        search_xpath = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')
        search_xpath.send_keys(search_param)
        time.sleep(3)
        search_xpath.send_keys(Keys.ENTER)
        admin_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span').click()

    def search_Directory(self,search_param):
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.find_element(by = By.XPATH, value = self.input_box_username).send_keys(self.username)
        self.driver.find_element(by = By.XPATH, value = self.input_box_password).send_keys(self.password)
        self.driver.find_element(by = By.XPATH, value = self.login_xpath).click()
        time.sleep(3)

        search_xpath = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')
        search_xpath.send_keys(search_param)
        time.sleep(3)
        search_xpath.send_keys(Keys.ENTER)
        admin_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span').click()

    def search_Maintenance(self,search_param):
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.find_element(by = By.XPATH, value = self.input_box_username).send_keys(self.username)
        self.driver.find_element(by = By.XPATH, value = self.input_box_password).send_keys(self.password)
        self.driver.find_element(by = By.XPATH, value = self.login_xpath).click()
        time.sleep(3)

        search_xpath = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')
        search_xpath.send_keys(search_param)
        time.sleep(3)
        search_xpath.send_keys(Keys.ENTER)
        admin_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span').click()

    def search_Buzz(self,search_param):
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.find_element(by = By.XPATH, value = self.input_box_username).send_keys(self.username)
        self.driver.find_element(by = By.XPATH, value = self.input_box_password).send_keys(self.password)
        self.driver.find_element(by = By.XPATH, value = self.login_xpath).click()
        time.sleep(3)

        search_xpath = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')
        search_xpath.send_keys(search_param)
        time.sleep(3)
        search_xpath.send_keys(Keys.ENTER)
        admin_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span').click()


s = Test_Jay()

s.search_admin("Admin")

#s.search_PIM("PIM")

#s.search_Leave("Leave")

#s.search_Time("Time")

#s.search_Recruitment("Recruitment")

#s.search_My_Info("My_Info")

#s.search_performance("Performance")

#s.search_Dashboard("Dashboard")

#s.search_Directory("Directory")

#s.search_Maintenance("Maintenance")

#s.search_Buzz("Buzz")

