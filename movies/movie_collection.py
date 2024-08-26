from movies.movie import Movie

""" 
    This module provides a class for managing a collection of movies. 
    
    The MovieCollection class provides methods for adding movies to the collection,
    retrieving movies by title, genre, or rating, and calculating statistics on the collection.
"""

class MovieCollection:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie: Movie):
        self.movies.append(movie)

    def get_movies_by_title(self, title: str):
        return [movie for movie in self.movies if title.lower() in movie.title.lower()]

    def get_movies_by_genre(self, genre: str):
        return [movie for movie in self.movies if movie.genre.lower() == genre.lower()]

    def get_movies_by_rating(self, min_rating: float):
        return [movie for movie in self.movies if movie.rating >= min_rating]

    def calculate_statistics(self):
        if not self.movies:
            return None
        avg_rating = sum(movie.rating for movie in self.movies) / len(self.movies)
        most_recent = max(self.movies, key=lambda movie: movie.release_year)
        highest_rated = max(self.movies, key=lambda movie: movie.rating)
        return {
            "average_rating": avg_rating,
            "most_recent_movie": most_recent,
            "highest_rated_movie": highest_rated
        }
