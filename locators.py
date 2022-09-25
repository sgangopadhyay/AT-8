from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Suman:
    driver = webdriver.Firefox()

    # use the selector ID
    def use_id(self, url, link_id):
        try:
            self.driver.get(url)
            link_id = self.driver.find_element(by=By.ID, value=link_id)
            time.sleep(5)
            link_id.click()
        except:
            print("Error : ID not found !")
    
    #use the XPATH 
    def use_xpath(self, url, xpath_link):
        try:
            self.driver.get(url)
            xpath_link = self.driver.find_element(by=By.XPATH, value=xpath_link)
            time.sleep(9)
            xpath_link.click() 
        except:
            print("Error : XPATH not found !")



s = Suman()

url_1 = "https://www.w3schools.com/"

url_2 = "https://www.guvi.in/"

link_id = "w3loginbtn"

class_id = "nav-link btn btn-primary text-white px-4"

xpath_link = '/html/body/div[3]/div[1]/a'

# s.use_id(url_1, link_id)

# s.use_class(url_2, class_id)


s.use_xpath(url_1, xpath_link)
