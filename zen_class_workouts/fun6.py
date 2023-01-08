from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class jay:
    def __init__ (self,url):
        self.url = url

    def headless_get_data(self):
        options = options()
        options.headless = true 
        driver = webdriver.Chrome(options = options)
        driver.get(self.url)
        data = [driver.title,driver.current_url]
        return data()

url_1 = 'https://www.guvi.in'

s = jay(url_1)

print(s.headless_get_data())
    
