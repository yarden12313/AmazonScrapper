from selenium.webdriver.support.ui import WebDriverWait
import selenium.common.exceptions


class PageObjectHelper:
    @staticmethod
    def find_element_by_id(timeout, parent, element_id):
        return WebDriverWait(parent, timeout).until(lambda driver: parent.find_element_by_id(id_=element_id))

    @staticmethod
    def find_element_by_xpath(timeout, parent, xpath):
        return WebDriverWait(parent, timeout).until(lambda driver: parent.find_element_by_xpath(xpath))

    @staticmethod
    def find_element_by_class(timeout, parent, class_name):
        return WebDriverWait(parent, timeout).until(lambda driver: parent.find_element_by_class_name(class_name))

    @staticmethod
    def find_elements_by_class(timeout, parent, class_name):
        try:
            return WebDriverWait(parent, timeout).until(lambda driver: parent.find_elements_by_class_name(class_name))
        except selenium.common.exceptions.TimeoutException:
            return []
