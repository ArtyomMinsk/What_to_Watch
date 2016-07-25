from movie import Movie
from rating import Rating

def main():
    print("Welcome to Popular Movies program!")
    print("----------------------------------\n\n")

    top_x = int(input("Please enter the top number of popular movies: "))
    min_ratings = int(input("Please enter the minimum number of ratings: "))

    rating = Rating('ml-100k/u.data')

    top_list = rating.get_top_movies(top_x, min_ratings)

    print("\nTop {} movies are:\n".format(top_x))
    print("Name     |     Rating")
    rating.print_rating(top_list)

    print("\n--------------------------------------------------------\n\n")
    user_id = input("To filter popular movies by your user_id, please enter user_id: ")

    top_list_filtered = rating.get_top_movies_for_user(top_x, min_ratings, user_id)

    print("\nTop unseen movies for user {} are:\n".format(user_id))
    print("Name     |     Rating")
    rating.print_rating(top_list_filtered)

    print("\n--------------------------------------------------------\n\n")
    print("Thank you! Goodbuy!")




    # rating = Rating('ml-100k/u.data_test')
    # print(rating.rating_rows_list)
    #
    # #rating_list = rating.get_movie_rating_list('346')
    # #print(rating_list)
    #
    # ratings = rating.rating_dictionary
    # print(ratings)
    #
    # user = rating.user_dictionary
    # print(user)
    #
    # print(rating.get_movie_rating_list('302'))
    # print(rating.get_avg_rating('474'))

if __name__ == '__main__':
    main()
