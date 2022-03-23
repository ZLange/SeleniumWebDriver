# practice page link -> https://courses.letskodeit.com/practice

from selenium import webdriver
from selenium.webdriver.common.by import By

class FindByClass():

    def test(self):
        baseurl = 'https://courses.letskodeit.com/practice'
        # driver = webdriver.Chrome() # use this if driver is added to PATH
        driver = webdriver.Chrome()
        driver.get(baseurl)
        elementbycl = driver.find_element(By.XPATH, "/html//input[@id='name']")

        if elementbycl is not None:  # check if element is found
            print('We found an element by xpath')

        elementbyid = driver.find_element(By.ID, "name")

        if elementbyid is not None:  # check if element is found
            print('We found an element by ID')



cc = FindByClass()
cc.test()
