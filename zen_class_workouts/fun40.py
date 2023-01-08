from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#to add new employee in pim module of orangehrm

class jay:
    driver = webdriver.Firefox()

    def __init__(self,url):
        self.url = url

    def login_hrm(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        time.sleep(5)
        username = 'Admin'
        password = 'admin123'

        input_box_username = self.driver.find_element(by = By.NAME, value = 'username')
        input_box_password = self.driver.find_element(by = By.NAME, value = 'password')
        login_xpath = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')

        input_box_username.send_keys(username)
        input_box_password.send_keys(password)
        login_xpath.click()
        time.sleep(7)

        pim_module_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span')
        pim_module_xpath.click()
        time.sleep(9)

        add_employee_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a')
        add_employee_xpath.click()
        time.sleep(12)

        first_name = 'JAYAPRAKASH'
        last_name = 'S'

        first_name_input = self.driver.find_element(by = By.NAME, value = 'firstName')
        last_name_input = self.driver.find_element(by= By.NAME, value = 'lastName')
        create_login_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]')

        first_name_input.send_keys(first_name)
        last_name_input.send_keys(last_name)
        create_login_xpath.click()
        time.sleep(7)

        save_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]')
        save_xpath.click()
        time.sleep(7)




    



url_1 = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

s = jay(url_1)

s.login_hrm()