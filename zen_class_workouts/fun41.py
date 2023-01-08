from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#to edit new employee in pim module of orangehrm

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

        edit_xpath = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div/div[23]/div/div')
        edit_xpath.click()
        edit_xpath.click()
        time.sleep(5)

        nationality_path = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div')
        male_xpath = self.driver.find_element(by = By.XPATH, value ='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label')
        male_xpath.click()
        time.sleep(5)

        job_xpath = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[6]/a')
        job_xpath.click()
        time.sleep(5)

        job_specification = 'Quality Tester'
        job_specification_xpath = self.driver.find_element(by = By.XPATH, value ='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/div/p')
        job_specification_xpath.send_keys(job_specification)
        time.sleep(7)

        job_save_xpath = self.driver.find_element(by = By.XPATH, value = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button')
        job_save_xpath.click()
        time.sleep(9)




    



url_1 = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

s = jay(url_1)

s.login_hrm()