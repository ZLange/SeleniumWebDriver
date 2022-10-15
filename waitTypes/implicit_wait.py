from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
import chromedriver_autoinstaller # checks current chrome version and if need updates chromedriver
import time



class ImplicitWait():

    def test(self):
        baseUrl = 'https://courses.letskodeit.com/practice'
        chromedriver_autoinstaller.install()
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        # loging in
        driver.find_element(By.LINK_TEXT, "SIGN IN").click()
        email = driver.find_element(By.ID, "email")
        email.send_keys("test@email.com")
        
        

ch = ImplicitWait()
ch.test()