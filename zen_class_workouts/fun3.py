from selenium import webdriver

class jay:
    driver = webdriver.Chrome()

    #constructor of class jay
    def __init__ (self,url):
        self.url = url

    #fetch the title of website
    def get_title(self,url):
        self.driver.get(self.url)
        return self.driver.title

url_1 = 'https://www.guvi.in'

url_2 = 'https://www.google.com'

s = jay(url_1)

s1 = jay(url_2)

print(s.get_title(url_1))
print(s1.get_title(url_2))