# practice page link -> https://courses.letskodeit.com/practice

from selenium import webdriver
from selenium.webdriver.common.by import By

class FindByLinkText():

    def test(self):
        baseurl = 'https://courses.letskodeit.com/practice'
        # driver = webdriver.Chrome() # use this if driver is added to PATH
        driver = webdriver.Chrome()
        driver.get(baseurl)
        elementbylinktext = driver.find_elements(By.LINK_TEXT,"Open Tab")

        if elementbylinktext is not None:  # check if element is found
            print('We found an element by Link Text')

        elementbypartial = driver.find_elements(By.PARTIAL_LINK_TEXT,"ALL COU")

        if elementbypartial is not None: # check if element is found
            print('We found an element by partial Link Text')


cc = FindByLinkText()
cc.test()
