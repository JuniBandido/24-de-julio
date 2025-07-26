def addMovie():
    how_many = int(input("¿Cuantas películas quieres agregar?\n"))
    count = 1
    for i in range(how_many):
        movie = []
        name = input(f"Ingresa el nombre de la {count} película: ")
        year = int(input(f"Ingresa el año en que se estrenó {name}: "))
        gener = input(f"Ingresa el género de {name}: ")
        count += 1
        movie.append(name)
        movie.append(year)
        movie.append(gener)
        movies.append(movie)

def showMovies():
    print(f"La lista de películas es:", movies)



movies = []
