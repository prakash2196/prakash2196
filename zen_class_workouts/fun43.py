from selenium import webdriver


url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

def Jay():
    driver = webdriver.Firefox()
    driver.get(url)
    get_cookie = driver.get_cookies()
    print(get_cookie)

Jay()