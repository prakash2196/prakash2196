from selenium import webdriver
 
driver_firefox = webdriver.Firefox()
 
url = "https://www.guvi.in"
 
driver_firefox.get(url)
