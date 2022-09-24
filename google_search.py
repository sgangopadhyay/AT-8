# Question : I want to search my name in Google using Python Selenium automation ?

# Problems :

# 1.) Locate the input box
# 2.) Locate the Search Button
# 3.) Fill the Input Box
# 4.) Click the Search Button

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
import time

class Suman:
    # constructor of class Suman
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Firefox()

    # method to do search on my name
    def google_search(self, name):
        self.driver.get(self.url)
        time.sleep(5)
        input_box = self.driver.find_element(by=By.NAME, value='q')
        input_box.send_keys(name)
        time.sleep(5)
        input_box.send_keys(Keys.ENTER)


url_1 = "https://www.google.com"

s=Suman(url_1)

s.google_search('suman gangopadhyay')
