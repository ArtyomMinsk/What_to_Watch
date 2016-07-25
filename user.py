import csv


class User:

    def __init__(self, file_path):
        user_rows_list = []

        with open(file_path, 'r') as user_file:
            reader = csv.reader(user_file, delimiter = '|')
            for row in reader:
                # rows is a list of lists
                user_rows_list.append(row)

        # Store the rows read in from the file
        self.user_rows = user_rows_list
