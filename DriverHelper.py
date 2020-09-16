from selenium import webdriver
from FileHelper import *


class DriverHelper:
    def __init__(self):
        browser_dict = {"1": self.chrome,
                        "2": self.explorer,
                        "3": self.firefox}
        index = input("Hello!\nPlease enter the browser index from the following list:\n1. Chrome\n2. IE "
                      "Explorer\n3. FireFox\n\nAnswer: ")
        self.driver = browser_dict[index]()

    @staticmethod
    def chrome():
        return webdriver.Chrome('chromedriver.exe')

    @staticmethod
    def explorer():
        return webdriver.Ie('IEDriverServer.exe')

    @staticmethod
    def firefox():
        path = FileHelper.get_project_path()
        return webdriver.Firefox(executable_path=os.path.join(path, "geckodriver.exe"))

    def connect_driver(self, url):
        self.driver.maximize_window()
        self.driver.get(url)
        return self.driver

    def disconnect_driver(self):
        self.driver.quit()
