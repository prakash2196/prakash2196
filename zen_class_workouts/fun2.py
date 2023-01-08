from selenium import webdriver

class jay:
    driver = webdriver.Chrome()

    #constructor of  class jay
    def __init__ (self,url):
        self.url = url

    #fetch the title of the website
    def get_title(self):
        self.driver.get(self.url)
        return self.driver.title

url_1 = 'https://www.guvi.in'

s=jay(url_1)

print(s.get_title())



