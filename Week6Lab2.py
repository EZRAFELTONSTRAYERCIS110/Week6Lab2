#Ezra Felton CIS 261 Week 6 Lab 2

FILENAME = "movies.txt" 

def write_movies(movies):
    with open(FILENAME, "w") as file:
        for movie in movies:
            file.write(f"{movie}\n")


def read_movies():
    movies = []
    with open(FILENAME) as file:
        for line in file:
            line = line.replace("\n", "")
            movies.append(line)
    return movies


def list_movies(movies):
    for i, movie in enumerate(movies, start=1):
        print(f"{i}. {movie}")
    print()


def add_movie(movies):
    movie = input("Movie:  ")
    movies.append(movie)
    write_movies(movies)
    print(f"{movie} was added.\n")


def delete_movie(movies):
