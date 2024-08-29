from movies.movie import Movie
from movies.movie_collection import MovieCollection

""" 
    This module provides a class for recommending movies based on genre and rating. 
    
    The MovieRecommendation class provides a method for recommending movies based on a base movie.
    The recommend method takes a MovieCollection and a base movie as input and returns a list of recommended movies.
    The recommended movies are movies with the same genre as the base movie and a rating within 1 point of the base movie's rating.
"""

class MovieRecommendation():
    def recommend(self, collection: MovieCollection, base_movie: Movie, rating_tolerance: float = 1) -> list:
        recommended_movies = []
        for movie in collection.get_movies_by_genre(base_movie.genre):
            if abs(movie.rating - base_movie.rating) <= rating_tolerance:
                recommended_movies.append(movie)
        return recommended_movies
