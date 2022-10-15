from selenium import webdriver
from waitTypes.explicit_wait_type import ExplicitWaitType
import time

class ExplicitWait2():

    def test(self):
        baseUrl = "https://courses.letskodeit.com/"
        driver = webdriver.Chrome()
        driver.implicitly_wait(2)
        driver.maximize_window()
        driver.get(baseUrl)

        wait = ExplicitWaitType(driver)
        element = wait.waitForElement(locator="SIGN IN", locatorType="link_text")
        element.click()

        time.sleep(2)
        driver.quit()

ch = ExplicitWait2()
ch.test()