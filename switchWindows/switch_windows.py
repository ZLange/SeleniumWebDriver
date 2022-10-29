from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller # checks current chrome version and if need updates chromedriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

class SwitchWindows():

    def test(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        chromedriver_autoinstaller.install()
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10) 
        driver.get(baseUrl)

        # Find parent handle -> Main Window
        parentHandle = driver.current_window_handle
        print("Parent Handle: " + parentHandle)

        # Find open window button and click it
        driver.find_element(By.ID, "openwindow").click()
        time.sleep(2)

        # Find all handles, there should two handles after clicking open window button
        handles = driver.window_handles

        # Switch to window and search course
        for handle in handles:
            print("Handle: " + handle)
            if handle not in parentHandle:
                driver.switch_to.window(handle)
                print("Switched to window:: " + handle)
                driver.find_element(By.XPATH, "//input[@id='search']").send_keys("python")
                time.sleep(2)
                driver.close()
                break

        # Switch back to the parent handle
        driver.switch_to.window(parentHandle)
        time.sleep(3)
        driver.find_element(By.XPATH, "//div[@id='alert-example-div']//input[@id='name']").send_keys("Test Successful")


cf = SwitchWindows()
cf.test()