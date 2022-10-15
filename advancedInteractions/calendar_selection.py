from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller # checks current chrome version and if need updates chromedriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalendarSelection():

    def test(self):
        baseUrl = 'https://www.expedia.com/'
        chromedriver_autoinstaller.install()
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10) 

        driver.get(baseUrl)

        # Click flights tab
        driver.find_element(By.LINK_TEXT, "Flights").click()
        # Find departing field and click it
        driver.find_element(By.XPATH, "//button[@id='d1-btn']").click()
        # Select date and clik the date
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-day='28']"))).click()
        # scond click to select only start date
        driver.find_element(By.XPATH, "//button[@data-day='28']").click()

        time.sleep(5)

        # for done button
        driver.find_element(By.XPATH, "//button[@data-stid='apply-date-picker']").click()

        time.sleep(5)
        
        driver.quit()

ch = CalendarSelection()
ch.test()