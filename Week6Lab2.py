#Ezra Felton CIS 261 Week 6 Lab 2

FILENAME = "movies.txt" 

def write_movies(movies):
    with open(FILENAME, "w") as file: # "w" writes erease what is already in the file (creates new file)
        for movie in movies:
            file.write(f"{movie}\n")


def read_movies():                  #This is where we read the file and store information
    movies = []                     #declaration of empty list 
    with open(FILENAME) as file:    #open file name : Movies.txt (File we saved eairler. This identifies info in file
        for line in file:
            line = line.replace("\n", "") #this code replace line feed (indentation is with and for)
            movies.append(line)
    return movies


def list_movies(movies): #((1))
    for i, movie in enumerate(movies, start=1):  #enumerate def: Mention a number of things one by one Video TS 12:30
        print(f"{i}. {movie}")
    print()


def add_movie(movies):   #((2))
    movie = input("Movie:  ") #input movie name.
    movies.append(movie)      # append Def: to attach 
    write_movies(movies)      #adds movie to text file. (Method)
    print(f"{movie} was added.\n")


def delete_movie(movies):  #((3))
    index = int(input("Numnber:   "))
    if index < 1 or index > len(movies):
        print("Invalid movie number. \n") 
    else:
        movie = movies.pop(index -1)    #pop removes movie 
        write_movies(movies)
        print(f"{movie} was deleted.\n")


def display_menu():
    print("The Movie List Program")
    print()
    print("COMMAND MENU")
    print("list -  List all movies")
    print("add  -  Add a movie")
    print("del  -  Delete a movie")
    print("exit -  Exit program")
    print()


def main():
    display_menu()
    movies = read_movies()  #Reading the text file into the list 
    while True:
        command = input("Command:   ")  #Displaying menu and checking for each command "list, add, delet, and exit"
        if command.lower() == "list": #((1))
            list_movies(movies)
        elif command.lower() == "add": #((2))
            add_movie(movies)
        elif command.lower() == "del": #((3))
            delete_movie(movies)
        elif command.lower() == "exit": #Exit is the break in the while loop 
            print("Bye!")
            break 
        else:
            print("Not a valid command. Please try again.")


if __name__ == "__main__":
    main()