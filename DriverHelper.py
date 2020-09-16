from selenium import webdriver


class DriverHelper:
    def __init__(self, driver):
        self.driver = driver

    def connect_driver(self, url):
        self.driver.maximize_window()
        self.driver.get(url)
        return self.driver

    def disconnect_driver(self):
        self.driver.quit()