import csv
#from rating import Rating



class Movie:

    #m = Movie()

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
    def read_file():
        #list of the lists
        movie_rows_list = []

        with open('ml-100k/u.item', encoding = 'latin_1') as movie_file:
            reader = csv.reader(movie_file, delimiter = '|')
            for row in reader:
                movie_rows_list.append(row)
            print(movie_rows_list)
            print("\ntitle: ", row[1])
            print("\nmovie_rows_list[0]: ", movie_rows_list[0])

        return movie_rows_list

    # Return mobie names by movie_id as dictionary
    def get_movie_name():
        movie_rows_list = Movie.read_file()
        for movie in movie_rows_list:
            my_dict = dict([(int(movie[0]), movie[1])])
            print(my_dict)
        #movie_name = self.movie_title

        return my_dict

Movie.get_movie_name()

    # def get_movie_id(self):
    #     return self.movie_id
    #
    # def get_title(self):
    #     return self.movie_title
    #
    # def get_release_date(self):
    #     return self.release_date


    #####
    # my_movie1 = Movie(row[0])
    # movie_title1 = my_movie1.get_title()

    # my_movie2 = Movie(row[1])
    # movie_title2 = my_movie2.get_title()
