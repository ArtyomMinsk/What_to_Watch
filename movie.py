import csv

class Movie:

    #def __init(self, movieRow)
    def __init__(self, movie_id, movie_title, release_date, video_release_date, IMDb_url,
                    unknown, Action, Adventure, Animation, Childrens, Comedy, Crime, Documentary,
                    Drama, Fantasy, Film_Noir, Horror, Musical, Mystery, Romance, Sci_Fi,
                    Thriller, War, Western):
        self.movie_id = movie_id
        # self.movie_id = movieRow[0]
        self.movie_title = movie_title
        # self.movie_title = movieRow[1]
        self.release_date = release_date
        # self.release_date = movieRow[2]
        self.video_release_date = video_release_date
        self.IMDb_url = IMDb_url
        self.unknown = unknown
        self.Action = Action
        self.Adventure = Adventure
        self.Animation = Animation
        self.Childrens = Childrens
        self.Comedy = Comedy
        self.Crime = Crime
        self.Documentary = Documentary
        self.Drama = Drama
        self.Fantasy = Fantasy
        self.Film_Noir = Film_Noir
        self.Horror = Horror
        self.Musical = Musical
        self.Mystery = Mystery
        self.Romance = Romance
        self.Sci_Fi = Sci_Fi
        self.Thriller = Thriller
        self.War = War
        self.Western = Western

    def get_movie_id(self):
        return self.movie_id

    def get_title(self):
        return self.movie_title

    def get_release_date(self):
        return self.release_date


rows = []

# def user_file():
with open('ml-100k/u.item', encoding = 'latin_1') as movie_file:
    reader = csv.reader(movie_file, delimiter = '|')
    for row in reader:
        rows.append(row)
    print(rows)
    print("\nrows[0]: ", rows[0])



    #####
    # my_movie1 = Movie(row[0])
    # movie_title1 = my_movie1.get_title()

    # my_movie2 = Movie(row[1])
    # movie_title2 = my_movie2.get_title()
