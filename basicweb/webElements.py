from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ClickAndSendKeys():

    def test(self):
        baseUrl = 'https://courses.letskodeit.com/practice'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        # driver.implicitly_wait(10)

        loginLink = driver.find_element(By.XPATH, "//a[normalize-space()='Sign In']")
        loginLink.click()

        emailField = driver.find_element(By.ID, 'email')
        emailField.send_keys('test@test.com')

        passwordField = driver.find_element(By.ID, 'password')
        passwordField.send_keys('test')

        time.sleep(3)

        emailField.clear()

        time.sleep(3)

        emailField.send_keys('test')



ff = ClickAndSendKeys()
ff.test()