from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import selenium.common.exceptions
import csv


def connect_to_driver():
    driver = webdriver.Chrome(chrome_driver_path)
    driver.maximize_window()
    driver.get(url)
    return driver


def find_element_by_id(timeout, parent, element_id):
    return WebDriverWait(parent, timeout).until(lambda driver: parent.find_element_by_id(id_=element_id))


def find_element_by_xpath(timeout, parent, xpath):
    return WebDriverWait(parent, timeout).until(lambda driver: parent.find_element_by_xpath(xpath))


def find_element_by_class(timeout, parent, class_name):
    return WebDriverWait(parent, timeout).until(lambda driver: parent.find_element_by_class_name(class_name))


def find_elements_by_class(timeout, parent, class_name):
    try:
        return WebDriverWait(parent, timeout).until(lambda driver: parent.find_elements_by_class_name(class_name))
    except selenium.common.exceptions.TimeoutException:
        return []


def export_to_csv_file(data, file_name):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Price"])
        for row in data:
            writer.writerow([row["title"], row["price"]])


if __name__ == '__main__':
    # Define variables
    url = "https://www.amazon.com"
    chrome_driver_path = 'C:/Users/papa/Downloads/chromedriver_win32/chromedriver'
    results_file = "results.csv"
    search_field_id = "twotabsearchtextbox"
    search_criteria = "software automation testing"
    search_button_xpath = "//input[@type='submit']"
    search_result_class = "s-main-slot.s-result-list.s-search-results.sg-row"
    items_class = "a-section.a-spacing-medium"
    title_class_1 = "a-size-base-plus.a-color-base.a-text-normal"
    title_class_2 = "a-size-medium.a-color-base.a-text-normal"
    price_class = "a-price"
    page_class = "a-last"

    # Open amazon site (multiple browsers)
    web_driver = connect_to_driver()

    # Find search engine
    search_field_element = find_element_by_id(10, web_driver, search_field_id)

    # Search for “software automation testing”
    search_field_element.send_keys(search_criteria)
    search_button_element = find_element_by_xpath(10, search_field_element, search_button_xpath)
    search_button_element.click()

    # Iterate for 4 pages and and collects items properties (title and name)
    collection = []
    current_page = 1
    while current_page < 4:
        # Find search result section
        search_result_element = find_element_by_class(10, web_driver, search_result_class)

        # Find search result items
        results = find_elements_by_class(10, search_result_element, items_class)

        # Collect items properties
        for i in range(len(results) - 1):
            unit = {}
            try:
                element = find_element_by_class(10, results[i], title_class_1)
            except selenium.common.exceptions.TimeoutException:
                element = find_element_by_class(10, results[i], title_class_2)
            unit.update({"title": element.text})
            prices_elements = find_elements_by_class(10, results[i], price_class)
            if not prices_elements:
                unit.update({"price": "$0"})
            else:
                for element in prices_elements:
                    if element.get_attribute("class") == price_class:
                        unit.update({"price": element.text.replace('\n', '.')})
            collection.append(unit)

        # Move to the next page
        page_element = find_elements_by_class(10, web_driver, page_class)
        page_element[0].click()
        current_page += 1

    # Write the result to SV file
    export_to_csv_file(collection, results_file)

    # Close driver
    web_driver.quit()

