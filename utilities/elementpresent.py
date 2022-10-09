from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import chromedriver_autoinstaller # checks current chrome version and if need updates chromedriver
import time
from handywrapers import HandyWrappers


class IsPresent():

    def test(self):
        baseUrl = 'https://courses.letskodeit.com/practice'
        chromedriver_autoinstaller.install()
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        # wait = WebDriverWait(driver, 30) # not used for now 
        hw = HandyWrappers(driver) # from handywrapers file

        driver.get(baseUrl)
        
        elemResult1 = hw.isElementPresent("name", By.ID)
        print(str(elemResult1))

        # elemResult2 = hw.elementPresenceCheck("//input[@id='name']", By.XPATH) # positive case
        elemResult2 = hw.elementPresenceCheck("//input[@id='name1']", By.XPATH) # negative case
        print(str(elemResult2))


ch = IsPresent()
ch.test()