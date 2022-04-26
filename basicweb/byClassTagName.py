# practice page link -> https://courses.letskodeit.com/practice

from selenium import webdriver
from selenium.webdriver.common.by import By

class FindByCalassTag():

    def test(self):
        baseurl = 'https://courses.letskodeit.com/practice'
        # driver = webdriver.Chrome() # use this if driver is added to PATH
        driver = webdriver.Chrome()
        driver.get(baseurl)
        elementbyclass = driver.find_elements(By.CLASS_NAME, "displayed-class")

        if elementbyclass is not None:  # check if element is found
            print('We found an element by Class name')

        elementbytag = driver.find_elements(By.TAG_NAME, "a")

        if elementbytag is not None: # check if element is found
            print('We found an element by Tag name')


cc = FindByCalassTag()
cc.test()
