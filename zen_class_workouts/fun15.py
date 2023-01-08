from selenium import webdriver


class jay:

    driver = webdriver.Chrome()

    def __init__ (self,url):
        self.url = url

    def get_title(self):
        self.driver.get(self.url)
        return self.driver.title

    def get_webpage(self):
        self.driver.get(self.url)
        return self.driver.page_source

    def get_url(self):
        self.driver.get(self.url)
        return self.driver.current_url

    def write_file(self):
        f = open('google.htmls',"w",encoding='utf-8')
        f.write(self.get_webpage())
        print('SUCCESS : File Write Done')
        f.close()

url_1 = 'https://www.google.com'

s = jay(url_1)

s.write_file()

#print(s.get_webpage())


