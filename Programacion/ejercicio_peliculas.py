peliculas = [
    ("Shrek", 90),
    ("Toy Story", 81),
    ("Buscando a Nemo", 100)
]

for titulo, duracion in peliculas:
    print(titulo, duracion)

peliculas.append(("Los Increíbles", 115))

for titulo, duracion in peliculas:
    print(titulo, duracion)

# peliculas[0][1] = 95
