# practice page link -> https://courses.letskodeit.com/practice

from selenium import webdriver
from selenium.webdriver.common.by import By


class FindByXpathCss():

    def test(self):
        baseurl = 'https://courses.letskodeit.com/practice'
        # driver = webdriver.Chrome() # use this if driver is added to PATH
        driver = webdriver.Chrome()
        driver.get(baseurl)
        elementbyxpath = driver.find_elements(By.XPATH,"/html//input[@id='name']")

        if elementbyxpath is not None: # check if element is found
            print('We found an element by Xpath')

        elementbycss = driver.find_elements(By.CSS_SELECTOR,"#displayed-text")

        if elementbycss is not None: # check if element is found
            print('We found an element by CSS selector')


cc = FindByXpathCss()
cc.test()
