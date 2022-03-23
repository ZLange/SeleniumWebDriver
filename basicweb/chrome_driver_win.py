from selenium import webdriver
import time


class ChromeDriverWin():

    def test(self):
        # brings up the browser
        driver = webdriver.Chrome()
        # opens needed web page
        driver.get("http://www.letskodeit.com")
        time.sleep(10)


cc = ChromeDriverWin()
cc.test()
