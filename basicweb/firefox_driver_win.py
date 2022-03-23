from selenium import webdriver


class RunFFTests():

    def testMethod(self):
        # Instantiate firefox browser command
        driver = webdriver.Chrome()
        # Open the provided url
        driver.get("http://www.letskodeit.com")


ff = RunFFTests()
ff.testMethod()
