import csv

class Rating:


    def __init__(self, user_id, item_id, rating, timestamp):
        self.user_id = user_id
        self.item_id = item_id
        self.rating = rating
        self.timestamp = timestamp

rows = []

with open('ml-100k/u.data', 'r') as rating_file:
    reader = csv.reader(rating_file, delimiter = '\t')
    for row in reader:
        rows.append(row)
    print(rows)
    print("\nrow[0]: ", rows[0])
