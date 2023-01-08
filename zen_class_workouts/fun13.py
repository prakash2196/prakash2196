from selenium import webdriver
import codecs

class jay:
    driver = webdriver.Chrome()

    def __init__(self,url):
        self.url = url

    def get_title(self):
        self.driver.get(self.url)
        return self.driver.title

    def get_url(self):
        self.driver.get(self.url)
        return self.driver.current_url

    def get_webpage(self):
        self.driver.get(self.url)
        return self.driver.page_source

    

    def write_file(self):
        f = open('index5.html',"w",encoding='utf-8')
        f.write(self.get_webpage())
        print("success:file write done")
        f.close()

url_1 = 'https://w3schools.com'

s = jay(url_1)

s.write_file()

