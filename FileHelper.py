import csv


class FileHelper:
    @staticmethod
    def export_to_csv_file(data, file_name):
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Price"])
            for row in data:
                writer.writerow([row["title"], row["price"]])