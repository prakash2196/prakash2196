from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class jay:
    driver = webdriver.Firefox()

    def __init__(self,url):
        self.url = url

    def open_jira(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        time.sleep(3)
        jira = self.driver.find_element(by = By.XPATH, value = '/html/body/main/div[2]/div/div[2]/div/div/div/div[2]/div/a')
        jira.send_keys(Keys.ENTER)
        time.sleep(7)
        username = 'prakashjai2811@gmail.com'
        username_input = self.driver.find_element(by = By.XPATH, value = '//*[@id="identifierId"]')
        next_input = self.driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span')
        username_input.send_keys(username)
        next_input.click()
        time.sleep(14)

url_1 = 'https://www.atlassian.com/software/jira?&aceid=&adposition=&adgroup=143485223644&campaign=18442427757&creative=639487383262&device=c&keyword=jira&matchtype=e&network=g&placement=&ds_kids=p73345677068&ds_e=GOOGLE&ds_eid=700000001558501&ds_e1=GOOGLE&gclid=Cj0KCQiAnNacBhDvARIsABnDa68Jsnz12yq-lTO1goaQmtHaA0FCx8WIqZ3yZs5R1K20D0MQQyompBcaAh6bEALw_wcB&gclsrc=aw.ds'

s = jay(url_1)

s.open_jira()


#/html/body/div[1]/main/div[2]/div/div[2]/div/div/div/a
#//*[@id="start-trial"]/div/div[2]/div/div/div/a