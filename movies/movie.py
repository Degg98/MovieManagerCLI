from abc import ABC, abstractmethod

class Movie(ABC):
    def __init__(self, title: str, genre: str, release_year: int, rating: float):
        self.title = title
        self.genre = genre
        self.release_year = release_year
        self.rating = rating

    def __str__(self):
        return f"{self.title} ({self.release_year}), Genre: {self.genre}, Rating: {self.rating}"

class AbstractMovieFactory(ABC):
    @abstractmethod
    def create_movie(self, title: str, genre: str, release_year: int, rating: float) -> Movie:
        pass
