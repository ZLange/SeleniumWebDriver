# practice page link -> https://courses.letskodeit.com/practice

from selenium import webdriver


class FindByLinkText():

    def test(self):
        baseurl = 'https://courses.letskodeit.com/practice'
        # driver = webdriver.Chrome() # use this if driver is added to PATH
        driver = webdriver.Chrome(executable_path="C:\\Users\\langezai\\PycharmProjects\\drivers\\chromedriver.exe")
        driver.get(baseurl)
        elementbylinktext = driver.find_elements_by_link_text("Open Tab")

        if elementbylinktext is not None:  # check if element is found
            print('We found an element by Link Text')

        elementbypartial = driver.find_elements_by_partial_link_text("ALL COU")

        if elementbypartial is not None: # check if element is found
            print('We found an element by partial Link Text')


cc = FindByLinkText()
cc.test()
