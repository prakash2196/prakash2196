from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class jay:
    driver = webdriver.Firefox()

    def __init__(self,url):
        self.url =url

    def edit_pim(self):
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

        employee_name = 'JAYAPRAKASH S'
        input_employee_name = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input').send_keys(employee_name)
        search_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()
        time.sleep(5)
        id_xpath = self.driver.find_element(by= By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div').click()
        time.sleep(3)

        #job_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[6]/a').click()
        #time.sleep(3)

        #job_specification = 'Quality Tester'
        #job_specification_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[6]/a').send_keys(job_specification)
        #job_title = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]').click()
        #job_title.select_by_innerHTML('QA Engineer').click()
        #job_title = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]').click()
        #save_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button').click()
        #time.sleep(5)

        salary_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[7]/a').click()
        add_xpath = self.driver.find_element(by = By.CSS Path, value = 'html body div#app div.oxd-layout div.oxd-layout-container div.oxd-layout-context div.orangehrm-background-container div.orangehrm-card-container div.orangehrm-edit-employee div.orangehrm-edit-employee-content div.orangehrm-horizontal-padding.orangehrm-vertical-padding div.orangehrm-action-header button.oxd-button.oxd-button--medium.oxd-button--text').click()
        time.sleep(5)
        salary_component_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input').send_keys('3CTC')
        amount_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/input').send_keys('15000')
        currency_by_class = self.driver.find_element(by = By.CLASS_NAME, value = 'oxd-select-text-input').Select
        save_xpath = self.driver.find_element(by = By.XPATH, value = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button[2]').click()
        time.sleep(3)



url_1 = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

s = jay(url_1)

s.edit_pim()

