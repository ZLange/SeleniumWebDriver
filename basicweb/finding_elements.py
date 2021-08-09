# practice page link -> https://courses.letskodeit.com/practice

from selenium import webdriver


class FindByIdName():

    def test(self):
        baseurl = 'https://courses.letskodeit.com/practice'
        # driver = webdriver.Chrome()
        driver = webdriver.Chrome(executable_path="C:\\Users\\langezai\\PycharmProjects\\drivers\\chromedriver.exe")
        driver.get(baseurl)
        elementbyid = driver.find_element_by_id("name")

        if elementbyid is not None: # check if elemnt is found
            print('We found an element by Id')

        elementbyname = driver.find_elements_by_name("show-hide")

        if elementbyname is not None: # check if elemnt is found
            print('We found an element by Name')


cc = FindByIdName()
cc.test()
