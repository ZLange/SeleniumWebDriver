# practice page link -> https://courses.letskodeit.com/practice

from selenium import webdriver


class FindByIdName():

    def test(self):
        baseurl = 'https://courses.letskodeit.com/practice'
        # driver = webdriver.Chrome() # use this if driver is added to PATH
        driver = webdriver.Chrome()
        driver.get(baseurl)
        elementbyid = driver.find_element_by_id("name")

        if elementbyid is not None: # check if element is found
            print('We found an element by Id')

        elementbyname = driver.find_elements_by_name("show-hide")

        if elementbyname is not None: # check if element is found
            print('We found an element by Name')


cc = FindByIdName()
cc.test()
