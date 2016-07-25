# What to Watch

## Description

Movie recommender.

## How To Run The Program

Run the popylar_movies.py file to run the program. It'll ask you to enter the top number of popular movies and the minimum number of ratings. After it shows you the list of movies according to the input requirements the program will ask to input the user_id to filter popular movies list.


# Sample Output

Here is some sample output when you run the program. It shows a list of top 15 most popular movies, and then filters that list for user 555. As you can see, user 555 has already seen "Schindler's List" and "Star Wars (1977)" and therefore, these two movies do now show up in their list.

```
Welcome to Popular Movies program!
----------------------------------


Please enter the top number of popular movies: 15
Please enter the minimum number of ratings: 5

Top 15 movies are:

Name     |     Rating
Pather Panchali (1955)  |  4.625
Close Shave, A (1995)  |  4.4911
Schindler's List (1993)  |  4.4664
Wrong Trousers, The (1993)  |  4.4661
Casablanca (1942)  |  4.4568
Wallace & Gromit: The Best of Aardman Animation (1996)  |  4.4478
Shawshank Redemption, The (1994)  |  4.4452
Rear Window (1954)  |  4.3876
Usual Suspects, The (1995)  |  4.3858
Star Wars (1977)  |  4.3585
12 Angry Men (1957)  |  4.344
Third Man, The (1949)  |  4.3333
Citizen Kane (1941)  |  4.2929
Some Folks Call It a Sling Blade (1993)  |  4.2927
To Kill a Mockingbird (1962)  |  4.2922

--------------------------------------------------------


To filter popular movies by your user_id, please enter user_id: 555

Top unseen movies for user 555 are:

Name     |     Rating
Pather Panchali (1955)  |  4.625
Close Shave, A (1995)  |  4.4911
Casablanca (1942)  |  4.4568
Wallace & Gromit: The Best of Aardman Animation (1996)  |  4.4478
Shawshank Redemption, The (1994)  |  4.4452
Rear Window (1954)  |  4.3876
Usual Suspects, The (1995)  |  4.3858
12 Angry Men (1957)  |  4.344
Third Man, The (1949)  |  4.3333
Citizen Kane (1941)  |  4.2929
Some Folks Call It a Sling Blade (1993)  |  4.2927
To Kill a Mockingbird (1962)  |  4.2922

--------------------------------------------------------


Thank you! Goodbuy!
```
