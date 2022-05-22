# WAP to find a movie names starts with ‘g’ in the given list of movies

def find_movie_names_starts_with(movie_list,start_character):
    movie_names_starts=[]
    for movie in movie_list:
        if movie.startswith(start_character) or movie.startswith(start_character):
            movie_names_starts.append(movie)
    return movie_names_starts

movies = ["Star wars", "KGF", "Gundamma katha", "geetha govindanum", "gadzill", "Robo", "Rustic Oracle"]
movie_list_starts=find_movie_names_starts_with(movies,'K')
print(movie_list_starts)
