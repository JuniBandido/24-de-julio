def addMovie():
    how_many = int(input("¿Cuantas películas quieres agregar?\n"))
    count = 1
    for i in range(how_many):
        movie = []
        name = input(f"Ingresa el nombre de la {count} película: ").lower()
        year = int(input(f"Ingresa el año en que se estrenó {name}: "))
        gener = input(f"Ingresa el género de {name}: ").lower()
        count += 1
        movie.append(name)
        movie.append(year)
        movie.append(gener)
        movies.append(movie)

def showMovies():
    print(f"La lista de películas es:", movies)

def showByGener():
    show_gener = input("¿Qué género quiere ver?\n").lower()
    for i in movies:
        if i[2] == show_gener:
            print(i)

def deleteMovieByTittle():
    print(movies)
    movie_name = input("Ingreas el nombre de la pelicula que quieres eliminar\n").lower()
    for i in movies:
        if i[0] == movie_name:
            movies.remove(i)
            print("La película fué eliminada")
            print(f"Tu lista de películas ahora es: ", movies)

def moviesStats():
    print(f"Tienes {len(movies)} películas registradas!")

    cont_gener = {}

    for i in movies:
        gener = i[2]
        if gener in cont_gener:
            cont_gener[gener] += 1
        else:
            cont_gener[gener] = 1
    for gener, cant in cont_gener.items():
        print(f"{cant} peliculas de {gener}")

    for i in movies:
        print(f"La pelicula más antigua es del año {i[1]}")



movies = [["scary movie", 2001, "miedo"], ["caca", 2003, "comedia"]]
moviesStats()
