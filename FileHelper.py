import csv
import os


class FileHelper:
    @staticmethod
    def export_to_csv_file(data, file_name):
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Price"])
            for row in data:
                writer.writerow([row["title"], row["price"]])

    @staticmethod
    def get_project_path():
        project = "exercise"
        path = os.path.dirname(__file__)
        while len(path) > 0:
            if os.path.split(path)[1] == project:
                return path
            path = os.path.split(path)[0]