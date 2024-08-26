from movies.movie import Movie
from movies.movie_collection import MovieCollection

class MovieRecommendation:
    def recommend(self, collection: MovieCollection, base_movie: Movie):
        recommended_movies = []
        for movie in collection.get_movies_by_genre(base_movie.genre):
            if abs(movie.rating - base_movie.rating) <= 1:
                recommended_movies.append(movie)
        return recommended_movies
