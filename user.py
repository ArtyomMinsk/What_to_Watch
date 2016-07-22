import csv

class User:


    def __init__(self, user_id, age, gender, occupation, zip_code):
        self.user_id = user_id
        self.age = age
        self.gender = gender
        self.occupation = occupation
        self.zip_code = zip_code

rows = []

# def user_file():
with open('ml-100k/u.user', 'r') as user_file:
    reader = csv.reader(user_file, delimiter = '|')
    for row in reader:
        rows.append(row)
    print(rows)

    print("\nrow[0]: ", rows[0])
