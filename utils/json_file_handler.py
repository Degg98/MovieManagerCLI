import json
from movies.movie_factory import MovieFactory
from movies.movie_db import MovieDB
from utils.file_handler_base import FileHandlerBase

class JsonFileHandler(FileHandlerBase):
    def __init__(self, db_name="movies.db"):
        self.db = MovieDB(db_name)
        self.factory = MovieFactory()

    def load_movies(self, json_file):
        """Load movies from a JSON file and add them to the database."""
        try:
            with open(json_file, 'r') as file:
                movies_data = json.load(file)
                
                for movie_data in movies_data:
                    movie = self.factory.create_movie(
                        title=movie_data['title'], 
                        genre=movie_data['genre'], 
                        release_year=movie_data['release_year'], 
                        rating=movie_data['rating']
                    )
                    self.db.add_movie(movie)
            print(f"Successfully loaded movies from {json_file}.")
        except Exception as e:
            print(f"Error loading movies from {json_file}: {e}")

    def save_movies(self, json_file):
        """Save the current movies from the database to a JSON file."""
        try:
            movies = self.db.get_all_movies()
            movies_data = []
            for movie in movies:
                movie_data = {
                    "title": movie[0],
                    "genre": movie[1],
                    "release_year": movie[2],
                    "rating": movie[3]
                }
                movies_data.append(movie_data)

            with open(json_file, 'w') as file:
                json.dump(movies_data, file, indent=4)
            print(f"Successfully saved movies to {json_file}.")
        except Exception as e:
            print(f"Error saving movies to {json_file}: {e}")

    def close(self):
        """Close the database connection."""
        self.db.close()
