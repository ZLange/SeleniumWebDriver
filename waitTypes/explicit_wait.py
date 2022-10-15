from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller # checks current chrome version and if need updates chromedriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *



class ExplicitWait():

    def test(self):
        # baseUrl = 'https://courses.letskodeit.com/practice'
        chromedriver_autoinstaller.install()
        driver = webdriver.Chrome()
        driver.maximize_window()
        # driver.get(baseUrl)
        driver.execute_script("window.location = 'https://courses.letskodeit.com/';")  #javascript code

        wait = WebDriverWait(driver, timeout=10, poll_frequency=1,
                                                ignored_exceptions=[NoSuchElementException,
                                                                    ElementNotVisibleException,
                                                                    ElementNotSelectableException])
        element = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "SIGN IN")))
        element.click()

        time.sleep(2)
        driver.quit()
        
        
ch = ExplicitWait()
ch.test()