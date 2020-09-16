from DriverHelper import *
from FileHelper import *
from AmazonPageObject import *


class Main:
    def __init__(self):
        # Define variables
        self.url = "https://www.amazon.com"
        self.results_file = "results.csv"
        self.search_criteria = "software automation testing"
        self.file_helper = FileHelper()
        self.amazon_obj = AmazonPageObject()
        self.driver_helper = DriverHelper()

    def main(self):
        # Open amazon site (multiple browsers)
        web_driver = self.driver_helper.connect_driver(self.url)

        # Search for “software automation testing”
        self.amazon_obj.search_in_amazon(web_driver, self.search_criteria)

        # Iterate for 4 pages and and collect items properties (title and name)
        collection = []
        current_page = 1
        while current_page < 4:
            collection.extend(self.amazon_obj.get_items_list(web_driver))
            self.amazon_obj.move_to_the_next_page(web_driver)
            current_page += 1

        # Write the result to SV file
        self.file_helper.export_to_csv_file(collection, self.results_file)

        # Close driver
        self.driver_helper.disconnect_driver()


if __name__ == '__main__':
    Main().main()
