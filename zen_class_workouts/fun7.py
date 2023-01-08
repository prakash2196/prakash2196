 
from selenium import webdriver
from selenium.webdriver.edge.options import Options 
 
url_1 = 'https://www.guvi.in'
 
options = Options()
options.headless = True
driver = webdriver.Edge(options=options)
driver.get(url_1)
data = [driver.title, driver.current_url]
print(data)
driver.quit()
 
