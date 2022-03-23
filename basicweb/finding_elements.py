# practice page link -> https://courses.letskodeit.com/practice

from selenium import webdriver
from selenium.webdriver.common.by import By


class FindByIdName():

    def test(self):
        baseurl = 'https://courses.letskodeit.com/practice'
        # driver = webdriver.Chrome() # use this if driver is added to PATH
        driver = webdriver.Chrome()
        driver.get(baseurl)
        elementbyid = driver.find_element(By.ID,"name")

        if elementbyid is not None: # check if element is found
            print('We found an element by Id')

        elementbyname = driver.find_elements(By.NAME,"show-hide")

        if elementbyname is not None: # check if element is found
            print('We found an element by Name')


cc = FindByIdName()
cc.test()
