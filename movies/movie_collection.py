from .movie_db import MovieDB
from .movie_factory import AbstractMovieFactory

class MovieCollection:
    def __init__(self, db_name="movies.db", factory=AbstractMovieFactory):
        self.db = MovieDB(db_name, factory)

    def list_movies(self):
        return self.db.get_all_movies()
    
    def add_movie(self, movie):
        self.db.add_movie(movie)

    def delete_movie(self, title, release_year):
        self.db.delete_movie(title, release_year)

    def get_movie_by_title(self, title):
        return self.db.get_movie_by_title(title)

    def get_movies_by_genre(self, genre):
        return self.db.get_movies_by_genre(genre)

    def get_movies_by_rating(self, rating):
        return self.db.get_movies_by_rating(rating)

    def calculate_statistics(self):
        return self.db.calculate_statistics()

    def close(self):
        self.db.close()
