from selenium import webdriver
from selenium.webdriver.firefox.options import Options

url = "https://www.guvi.in"

def suman_headless_browsing(url):
    options = Options()
    options.headless = True 
    driver=webdriver.Firefox(options=options)
    driver.get(url)
    print(driver.title)
    print(driver.current_url)
    driver.close()

suman_headless_browsing(url)

