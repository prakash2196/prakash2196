from selenium import webdriver


class jay:

    driver = webdriver.Chrome()

    #constructor of class jay
    def __init__(self,url):
        self.url = url

    #fetch the title of website
    def get_title (self):
        self.driver.get(self.url)
        return self.driver.title

    #fetch the url of website
    def get_url(self):
        self.driver.get(self.url)
        return self.driver.current_url

    #fetch the content of website
    def get_webpage(self):
        self.driver.get(self.url)
        return self .driver.page_source

    #write the content of website
    def write_file(self):
        f = open('index2.html',"w")
        f.write(self.get_webpage())
        print('SUCCESS : File Write Done')
        f.close()

    

url_1 = 'https://www.guvi.in'

s=jay(url_1)

s.write_file()

#print(s.get_webpage())