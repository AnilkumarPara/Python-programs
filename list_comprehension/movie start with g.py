
# WAP to find a movie names starts with ‘g’ in the given list of movies
movies = ["Star wars", "Gandhi", "Gundamma katha", "geetha govindanum", "gadzill", "Robo", "Rustic Oracle"]

print("---using for loop---")
movies_g=[]
for movie in movies:
    if movie.startswith('g') or movie.startswith('G'):
        movies_g.append(movie)

print(movies_g)

print("---using List Comprehension---")

movies_names_g = [movie for movie in movies if movie.startswith('g') or movie.startswith('G')]

print(movies_names_g)
