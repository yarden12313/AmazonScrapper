from selenium import webdriver
from FileHelper import *
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class DriverHelper:
    def __init__(self):
        browser_dict = {"1": self.chrome,
                        "2": self.edge,
                        "3": self.firefox,
                        "4": self.explorer}
        index = input("Hello!\nPlease enter the browser index from the following list:\n1. Chrome\n2. Edge\n3. "
                      "FireFox\n4. IE Explorer\n\nAnswer: ")
        self.driver = browser_dict[index]()

    @staticmethod
    def chrome():
        return webdriver.Chrome('chromedriver.exe')

    @staticmethod
    def edge():
        return webdriver.Edge('msedgedriver.exe')

    @staticmethod
    def explorer():
        # create capabilities
        capabilities = DesiredCapabilities.INTERNETEXPLORER

        # delete platform and version keys
        capabilities['ignoreProtectedModeSettings'] = True

        capabilities['ignoreZoomSetting'] = True

        capabilities.setdefault("nativeEvents", False)
        return webdriver.Ie('IEDriverServer.exe', capabilities=capabilities)

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
