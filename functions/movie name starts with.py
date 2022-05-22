# WAP to find a movie names starts with  in the given list of movies

def find_movie_names_starts_with(movie_list,start_character):
    start_with_movies=[]
    for movie in movie_list:
        if movie.startswith(start_character):
            start_with_movies.append(movie)
    return start_with_movies

movies = ["Star wars", "Gandhi", "Gundamma katha", "geetha govindanum", "gadzill", "Robo", "Rustic Oracle"]
movie_names = find_movie_names_starts_with(movies,'R')

print(movie_names)
