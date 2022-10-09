from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import chromedriver_autoinstaller # checks current chrome version and if need updates chromedriver
import time



class DynamicXPath():

    def test(self):
        baseUrl = 'https://courses.letskodeit.com/practice'
        chromedriver_autoinstaller.install()
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        # wait = WebDriverWait(driver, 30) # not used for now 

        driver.get(baseUrl)

        # loging in
        driver.find_element(By.LINK_TEXT, "SIGN IN").click()
        email = driver.find_element(By.ID, "email")
        email.send_keys("test@email.com")
        password = driver.find_element(By.ID, "password")
        password.send_keys("abcabc")
        driver.find_element(By.XPATH, "//input[@value='Login']").click()

        # open all courses
        driver.find_element(By.XPATH, "//a[normalize-space()='ALL COURSES']").click()
    

        #select the course
        _course = "//h4[contains(@class,'dynamic-heading') and contains(text(),'{0}')]" # in zero value will be changed
        _courseLocator = _course.format("JavaScript for beginners") # replaces zero with this text

        courseElement = driver.find_element(By.XPATH, _courseLocator)
        courseElement.click()
        


ch = DynamicXPath()
ch.test()