from selenium import webdriver


class RunFFTests():

    def testMethod(self):
        # Instantiate firefox browser command
        driver = webdriver.Firefox(executable_path="C:\\Users\\langezai\\PycharmProjects\\drivers\\geckodriver.exe")
        # Open the provided url
        driver.get("http://www.letskodeit.com")


ff = RunFFTests()
ff.testMethod()
