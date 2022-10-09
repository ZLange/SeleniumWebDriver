from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import chromedriver_autoinstaller # checks current chrome version and if need updates chromedriver
import time

class GetText():

    def test(self):
        baseUrl = 'https://courses.letskodeit.com/practice'
        chromedriver_autoinstaller.install()
        driver = webdriver.Chrome()
        driver.maximize_window()
        wait = WebDriverWait(driver, 30) # not used for now 
        driver.get(baseUrl)
        # driver.implicitly_wait(10)

        openTabelem = driver.find_element(By.ID, "opentab")
        elemText = openTabelem.text
        print("Text on elem is: " + elemText)
        time.sleep(1)
        driver.quit()

ch = GetText()
ch.test()