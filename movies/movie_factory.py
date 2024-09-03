from .movie import Movie, AbstractMovieFactory

""" 
    This module provides a concrete implementation of the AbstractMovieFactory class.

    The ConcreteMovie class is a concrete implementation of the Movie class.
    The MovieFactory class is a concrete implementation of the AbstractMovieFactory class.
"""

class ConcreteMovie(Movie):
    def __init__(self, title: str, genre: str, release_year: int, rating: float):
        self.title = title
        self.genre = genre
        self.release_year = release_year
        self.rating = rating

    def __str__(self):
        return f"{self.title} ({self.release_year}), Genre: {self.genre}, Rating: {self.rating}"

class MovieFactory(AbstractMovieFactory):
    def create_movie(self, title: str, genre: str, release_year: int, rating: float) -> Movie:
        return ConcreteMovie(title, genre, release_year, rating)


class Reel(Movie):
    def __init__(self, title: str, genre: str, release_year: int, rating: float, duration: int):
        self.duration = duration
        self.title = title
        self.genre = genre
        self.release_year = release_year
        self.rating = rating

    def __str__(self):
        return f"{self.title} ({self.release_year}), Genre: {self.genre}, Rating: {self.rating}, Duration: {self.duration} minutes"
    
class ReelFactory(AbstractMovieFactory):
    def create_movie(self, title: str, genre: str, release_year: int, rating: float, duration: int) -> Movie:
        return Reel(title, genre, release_year, rating, duration)