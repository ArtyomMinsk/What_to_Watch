import csv
#from rating import Rating



class Movie:

    def __init__(self, row):
        self.movie_id = row[0]
        self.movie_title = row[1]
        self.release_date = row[2]
        self.video_release_date = row[3]
        self.IMDb_url = row[4]
        self.unknown = row[5]
        self.Action = row[6]
        self.Adventure = row[7]
        self.Animation = row[8]
        self.Childrens = row[9]
        self.Comedy = row[10]
        self.Crime = row[11]
        self.Documentary = row[12]
        self.Drama = row[13]
        self.Fantasy = row[14]
        self.Film_Noir = row[15]
        self.Horror = row[16]
        self.Musical = row[17]
        self.Mystery = row[18]
        self.Romance = row[19]
        self.Sci_Fi = row[20]
        self.Thriller = row[21]
        self.War = row[22]
        self.Western = row[23]

        # Returns list of lists
    def read_movie_file():
        #list of the lists
        movie_rows_list = []

        with open('ml-100k/u.item', encoding = 'latin_1') as movie_file:
            reader = csv.reader(movie_file, delimiter = '|')
            for row in reader:
                movie_rows_list.append(row)

        # print(movie_rows_list)
        return movie_rows_list

    # Return mobie names by movie_id as dictionary
    def get_movie_name(item_id):
        movie_rows_list = Movie.read_movie_file()

        movie_row = movie_rows_list[item_id - 1]
        movie_name = movie_row[1]

        print(movie_name)
        return movie_name
