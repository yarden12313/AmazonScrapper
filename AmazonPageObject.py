from PageObjectHelper import *


class AmazonPageObject:
    def __init__(self):
        self.obj_helper = PageObjectHelper()

    def search_field(self, parent):
        return self.obj_helper.find_element_by_id(10, parent, "twotabsearchtextbox")

    def search_button(self, parent):
        return self.obj_helper.find_element_by_xpath(10, parent, "//input[@type='submit']")

    def search_in_amazon(self, parent, search_criteria):
        # Find search engine
        search_field_element = self.search_field(parent)

        # Search for “software automation testing”
        search_field_element.send_keys(search_criteria)
        search_button_element = self.search_button(search_field_element)
        search_button_element.click()

    def search_result(self, parent):
        return self.obj_helper.find_element_by_class(10, parent, "s-main-slot.s-result-list.s-search-results.sg-row")

    def items_class(self, parent):
        return self.obj_helper.find_elements_by_class(10, parent, "a-section.a-spacing-medium")

    def title(self, parent):
        try:
            element = self.obj_helper.find_element_by_class(10, parent, "a-size-base-plus.a-color-base.a-text-normal")
        except selenium.common.exceptions.TimeoutException:
            element = self.obj_helper.find_element_by_class(10, parent, "a-size-medium.a-color-base.a-text-normal")
        return element

    def price(self, parent):
        class_name = "a-price"
        prices_elements = self.obj_helper.find_elements_by_class(10, parent, class_name)
        if not prices_elements:
            return {"price": "$0"}
        else:
            for element in prices_elements:
                if element.get_attribute("class") == class_name:
                    return {"price": element.text.replace('\n', '.')}

    def get_items_list(self, parent):
        collection = []

        # Find search result section
        search_result_element = self.search_result(parent)

        # Find search result items
        results = self.items_class(search_result_element)

        # Collect items properties
        for i in range(len(results) - 1):
            unit = {}
            unit.update({"title": self.title(results[i]).text})
            unit.update(self.price(results[i]))
            collection.append(unit)
        return collection

    def move_to_the_next_page(self, parent):
        page_element = self.obj_helper.find_elements_by_class(10, parent, "a-last")
        page_element[0].click()
