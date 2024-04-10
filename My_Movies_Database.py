import random

movies = {
    "The Shawshank Redemption": 9.5,
    "Pulp Fiction": 8.8,
    "The Room": 3.6,
    "The Godfather": 9.2,
    "The Godfather: Part II": 9.0,
    "The Dark Knight": 9.0,
    "12 Angry Men": 8.9,
    "Everything Everywhere All At Once": 8.9,
    "Forrest Gump": 8.8,
    "Star Wars: Episode V": 8.7
}

# Your code here
menu = ["List movies", "Add movie", "Delete movie", "Update movie", "Stats", "Random movie", "Search movie",
        "Movies Sorted by Rating"]


def list_movies():
    print("List of Movies:")
    for movie, rating in movies.items():
        print(f"{movie}: {rating}")


def add_movies():
    print("Add a New Movie")
    movie_name = input("Enter the name of the movie: ")
    movie_rating = float(input("Enter the rating of the movie: "))
    movies[movie_name] = movie_rating
    print(f"Movie '{movie_name}' with rating {movie_rating} added successfully!")


def delete_movies():
    print("Delete a movie")
    movie_to_delete = input("What Movie you want to delete:")
    if movie_to_delete in movies:
        removed_movie = movies.pop(movie_to_delete)
        print(f" Movie '{movie_to_delete}' was deleted successfully!")
    else:
        print(f"Movie '{movie_to_delete}' not found in the database. Please try again.")


def update_movies():
    print("Update Movie")
    movie_to_update = input("What Movie you want to update:")
    new_rating = float(input("Enter the new rating of the movie: "))
    movies[movie_to_update] = new_rating
    print(f"Movie {movie_to_update} with rating {new_rating} added successfully!")


def stats():
    print("Stats")
    average_rating = sum(movies.values()) / len(movies)
    median_rating = sorted(movies.values())[len(movies) // 2]
    best_movie = max(movies, key=movies.get)
    worst_movie = min(movies, key=movies.get)
    print(f"Average rating: {average_rating}")
    print(f"Median rating: {median_rating}")
    print(f"Best movie: {best_movie} with rating {movies[best_movie]}")
    print(f"Worst movie: {worst_movie} with rating {movies[worst_movie]}")


def random_movie():
    print("Radom Movie")
    print("You picked the random movie selector. The program will select a movie for you")
    movie, rate = random.choice(list(movies.items()))
    print(f"You should watch {movie}, it has {rate} rating.")


def search_movie():
    print("Search Movie")
    movie_search = input("Enter part of movie name: ").lower()
    found_movies = [movie for movie in movies.keys() if movie_search in movie.lower()]
    if found_movies:
        print("Movies found:")
        for movie in found_movies:
            print(movie)
    else:
        print("No movies found matching the search criteria.")


def movies_sorted_by_rating():
    print("Movies Sorted by Rating")
    sorted_movies = sorted(movies.items(), key=lambda x: x[1], reverse=True)
    print(f"These are the movies sorted my rating: {sorted_movies}")


def create_rating_histogram():
    print("Create Rating Histogram")


my_dict = {
    1: list_movies,
    2: add_movies,
    3: delete_movies,
    4: update_movies,
    5: stats,
    6: random_movie,
    7: search_movie,
    8: movies_sorted_by_rating
}


def choose_opt_dictionary(command):
    my_dict[command]


while True:
    print("\033[1;32m ********** My Movies Database **********\n")
    for index, item in enumerate(menu):
        print(index + 1, item)
    user_choice = int(input("\033[1;36m Enter choice (1-8):\n"))
    if user_choice in my_dict:
        my_dict[user_choice]()
    else:
        print("\033[1;33m Try Another Option\n")
