# practice page link -> https://courses.letskodeit.com/practice

from selenium import webdriver
from selenium.webdriver.common.by import By

class ListOfElements():

    def test(self):
        baseurl = 'https://courses.letskodeit.com/practice'
        # driver = webdriver.Chrome() # use this if driver is added to PATH
        driver = webdriver.Chrome(executable_path="C:\\Users\\langezai\\PycharmProjects\\drivers\\chromedriver.exe")
        driver.get(baseurl)
        listbyclassname = driver.find_elements_by_class_name('inputs')
        # length = len(listbyclassname)

        if listbyclassname is not None:  # check if element is found
            print('Size of the list is: ' + str(len(listbyclassname)))

        listbytagname = driver.find_elements(By.TAG_NAME, 'h1')

        if listbytagname is not None:  # check if element is found
            print('Size of the list is: ' + str(len(listbytagname)))


cc = ListOfElements()
cc.test()
