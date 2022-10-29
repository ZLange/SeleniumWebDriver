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
        driver.find_element(By.ID, "password").send_keys("")
        driver.find_element(By.NAME, "commit").click()
        self.takeScreenshot(driver)

    def takeScreenshot(self, driver):
        "Take screenshot of the current opened page"

        fileName = str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "C:\\Users\\zozol\\OneDrive\\test\\"
        destinationFile = screenshotDirectory + fileName

        try:
            driver.save_screenshot(destinationFile)
            print("Screenshot saved to directory --> :: " + destinationFile)
        except NotADirectoryError:
            print("Not a directory issue")

cf = Screenshots()
cf.test()