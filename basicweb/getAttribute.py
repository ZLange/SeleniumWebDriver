from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import chromedriver_autoinstaller # checks current chrome version and if need updates chromedriver
import time

class GetAttrib():

    def test(self):
        baseUrl = 'https://courses.letskodeit.com/practice'
        chromedriver_autoinstaller.install()
        driver = webdriver.Chrome()
        driver.maximize_window()
        wait = WebDriverWait(driver, 30) # not used for now 
        driver.get(baseUrl)
        # driver.implicitly_wait(10)

        elem = driver.find_element(By.ID, "name")
        # result = elem.get_attribute("class")
        result = elem.get_attribute("type")
        print("Value of the attribute is: " + result)
        time.sleep(1)
        driver.quit()

ch = GetAttrib()
ch.test()