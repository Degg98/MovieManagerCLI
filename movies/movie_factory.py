from .movie import Movie, AbstractMovieFactory

""" 
    This module provides a concrete implementation of the AbstractMovieFactory class.

    The ConcreteMovie class is a concrete implementation of the Movie class.
    The MovieFactory class is a concrete implementation of the AbstractMovieFactory class.
"""

class ConcreteMovie(Movie):
    pass

class MovieFactory(AbstractMovieFactory):
    def create_movie(self, title: str, genre: str, release_year: int, rating: float) -> Movie:
        return ConcreteMovie(title, genre, release_year, rating)
