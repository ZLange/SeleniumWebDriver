from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller # checks current chrome version and if need updates chromedriver
import time

class JavaScriptExecution():

    def test(self):
        # baseUrl = "https://letskodeit.teachable.com/"
        chromedriver_autoinstaller.install()
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.execute_script("window.location = 'https://letskodeit.teachable.com/'")
        driver.implicitly_wait(10) 

        time.sleep(6)

        # element = driver.find_element(By.ID, "name")
        element = driver.execute_script("return document.getElementById('name');")
        element.send_keys("Test")


cf = JavaScriptExecution()
cf.test()