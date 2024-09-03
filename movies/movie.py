from abc import ABC, abstractmethod

""" 
    This file provides the Movie class and the AbstractMovieFactory class. 
    
    An abstract factory pattern is used to create Movie objects.
    The Movie class is an abstract base class that represents a movie.
    The AbstractMovieFactory class is an abstract base class that represents a factory for creating Movie objects.
"""

class Movie(ABC):
    @abstractmethod
    def __init__(self, title: str, genre: str, release_year: int, rating: float):
        pass
    
    @abstractmethod
    def __str__(self):
        pass

class AbstractMovieFactory(ABC):
    @abstractmethod
    def create_movie(self, title: str, genre: str, release_year: int, rating: float) -> Movie:
        pass
