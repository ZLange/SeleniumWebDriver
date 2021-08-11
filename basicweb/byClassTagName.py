# practice page link -> https://courses.letskodeit.com/practice

from selenium import webdriver


class FindByCalassTag():

    def test(self):
        baseurl = 'https://courses.letskodeit.com/practice'
        # driver = webdriver.Chrome() # use this if driver is added to PATH
        driver = webdriver.Chrome(executable_path="C:\\Users\\langezai\\PycharmProjects\\drivers\\chromedriver.exe")
        driver.get(baseurl)
        elementbyclass = driver.find_elements_by_class_name("displayed-class")

        if elementbyclass is not None:  # check if element is found
            print('We found an element by Class name')

        elementbytag = driver.find_elements_by_tag_name("a")

        if elementbytag is not None: # check if element is found
            print('We found an element by Tag name')


cc = FindByCalassTag()
cc.test()
