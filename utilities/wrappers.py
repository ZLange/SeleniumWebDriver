from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import chromedriver_autoinstaller # checks current chrome version and if need updates chromedriver
import time
from handywrapers import HandyWrappers


class UseWrappers():

    def test(self):
        baseUrl = 'https://courses.letskodeit.com/practice'
        chromedriver_autoinstaller.install()
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        # wait = WebDriverWait(driver, 30) # not used for now 
        hw = HandyWrappers(driver)

        driver.get(baseUrl)
        

        elemField1 = hw.getElement("name")
        elemField1.send_keys("Test")
        time.sleep(2)
        elemField2 = hw.getElement("//input[@id='name']", locatorType="xpath")
        elemField2.clear()



ch = UseWrappers()
ch.test()