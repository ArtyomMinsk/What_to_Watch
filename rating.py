import csv
from collections import defaultdict
from movie import Movie


class Rating:

    def __init__(self, file_path):
        rows_list = []

        with open(file_path, 'r') as rating_file:
            reader = csv.reader(rating_file, delimiter='\t')
            for row in reader:
                rows_list.append(row)

        # Store the rows read in from the file
        self.rating_rows_list = rows_list

        # Build a dictionary of movie_id to ratings list
        # Also build a dictionary of user_id to movie ratings
        my_dict1 = {}
        my_dict2 = {}
        for rating in self.rating_rows_list:
            my_dict1.setdefault(rating[1], []).append(rating[2])

            rating_tuple = (rating[1], rating[2])
            my_dict2.setdefault(rating[0], []).append(rating_tuple)

        self.rating_dictionary = my_dict1
        self.user_dictionary = my_dict2

    # Returns a list of ratings for a specific movie_id
    def get_movie_rating_list(self, item_id):
        try:
            self.rating_dictionary[item_id]
            # print(my_dict[item_id])
            return self.rating_dictionary[item_id]
        except KeyError:
            return []

    # Returns average movie rating by movie_id
    def get_avg_rating(self, item_id):
        rating_list = self.get_movie_rating_list(item_id)
        # print(rating_list)

        # Convert rating_list to a list of ints
        rating_list_int = list(map(int, rating_list))
        average = sum(rating_list_int) / len(rating_list_int)
        # print(average)

        return average

    # Returns a rating list with tuples (movie_id, movie_rating)
    def get_user_rating(self, user_id):
        # Return list of tuples
        return self.user_dictionary[user_id]

    # Returns true if user has seen the given movie.
    # Otherwise, returns false.
    def has_user_seen_movie(self, user_id, movie_id):
        # Returns list of [(movie_id, movie_rating)]
        movie_rating_list = self.get_user_rating(user_id)

        flag = False

        for item in movie_rating_list:
            # print("has_user_seen_movie movie_id: ", movie_id)
            # print("has_user_seen_movie item[0]: ", item[0])

            if movie_id == item[0]:
                # print("HERE!")
                flag = True

        if flag == True:
            # print('yes')
            return True
        else:
            # print('no')
            return False

    # Returns top x movies, with min_ratings each.
    def get_top_movies(self, top_x, min_ratings):
        movie_rows_list = Movie.read_movie_file()

        movie_list_with_min_ratings = []
        for movie in movie_rows_list:
            movie_id = movie[0]
            movie_name = movie[1]

            ratings_list = self.get_movie_rating_list(movie_id)
            # print("movie_id", movie_id)
            # print("ratings", ratings_list)

            if len(ratings_list) >= min_ratings:
                movie_avg_tup = (movie_id, movie_name, self.get_avg_rating(movie_id))
                movie_list_with_min_ratings.append(movie_avg_tup)

        sorted_list = sorted(movie_list_with_min_ratings, key = lambda x: x[2])
        reversed_list = list(reversed(sorted_list))
        # print(sorted_list)
        # print(reversed_list)

        top_x_list = reversed_list[:top_x]
        #print(top_x_list)

        return top_x_list

    # Returns top x movies, with min_ratings each, for a specific user_id.
    def get_top_movies_for_user(self, top_x, min_ratings, user_id):
        top_x_movies = self.get_top_movies(top_x, min_ratings)
        top_x_list = []

        for movie in top_x_movies:
            movie_id = movie[0]
            # print("movie_id is: ", movie_id)

            if not self.has_user_seen_movie(user_id, movie_id):
                top_x_list.append(movie)

        #print("User hasn't seen: ", top_x_list)
        return top_x_list

    # Function to print the rating list in a nice way
    def print_rating(self, rating_list):
        for item in rating_list:
            print("{}  |  {}".format(item[1], round(item[2], 4)))

# Rating.get_movie_rating_list('346')
# Rating.get_avg_rating('346')

# Rating.get_movie_rating_list('474')
# Rating.get_avg_rating('474')

# Rating.get_user_rating('196')
# Rating.get_user_rating('22')

# print(Rating.has_user_seen_movie('196', 144))
# print(Rating.has_user_seen_movie('196', 100))
# print(Rating.has_user_seen_movie('196', 112233))
# Rating.get_top_movies(3, 4)
# Rating.get_top_movies_for_user(3, 4, '196')
