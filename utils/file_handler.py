import json
from movies.movie_factory import MovieFactory

""" This module provides a class for handling file I/O operations. """

class FileHandler:
    @staticmethod
    def load_from_file(file_path: str) -> list:
        with open(file_path, 'r') as file:
            data = json.load(file)
            factory = MovieFactory()
            return [factory.create_movie(**movie_data) for movie_data in data]

    @staticmethod
    def save_to_file(file_path: str, movies: list):
        with open(file_path, 'w') as file:
            json.dump([movie.__dict__ for movie in movies], file, indent=4)
