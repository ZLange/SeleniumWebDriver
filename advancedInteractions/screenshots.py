from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller # checks current chrome version and if need updates chromedriver
import time

class Screenshots():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/"
        chromedriver_autoinstaller.install()
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10) 

        driver.get(baseUrl)

        driver.find_element(By.LINK_TEXT, "Login").click()
        driver.find_element(By.ID, "email").send_keys("abc@email.com")
        driver.find_element(By.ID, "password").send_keys("") # left empty in order to get error
        driver.find_element(By.NAME, "commit").click()
        destinationFileName = "C:\\Users\\zozol\\OneDrive\\test\\test.png"

        try:
            driver.save_screenshot(destinationFileName)
            print("Screenshot saved to directory --> :: " + destinationFileName)
        except NotADirectoryError:
            print("Not a directory issue")

cf = Screenshots()
cf.test()