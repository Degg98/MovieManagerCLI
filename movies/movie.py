from abc import ABC, abstractmethod

""" 
    This file provides the Movie class and the AbstractMovieFactory class. 
    
    An abstract factory pattern is used to create Movie objects.
    The Movie class is an abstract base class that represents a movie.
    The AbstractMovieFactory class is an abstract base class that represents a factory for creating Movie objects.
"""

class Movie(ABC):
    def __init__(self, title: str, genre: str, release_year: int, rating: float):
        self.title = title
        self.genre = genre
        self.release_year = release_year
        self.rating = rating

    def __str__(self):
        return f"{self.title} ({self.release_year}), Genre: {self.genre}, Rating: {self.rating}"

    @staticmethod
    def capitalize_words(input_string):
        # Format the input 
        words = input_string.split()
        capitalized_words = [word.capitalize() for word in words]
        result = ' '.join(capitalized_words)
        
        return result

class AbstractMovieFactory(ABC):
    @abstractmethod
    def create_movie(self, title: str, genre: str, release_year: int, rating: float) -> Movie:
        pass
