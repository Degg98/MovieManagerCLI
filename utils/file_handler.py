from utils.file_handler_factory import FileHandlerFactory

class FileHandler:
    """
    A class that handles loading and saving movies from different sources.

    Args:
        file_type (str, optional): The type of file to handle. Defaults to "json".
        db_name (str, optional): The name of the database file. Defaults to "movies.db".
        max_movies (int, optional): The maximum number of movies to handle. Defaults to None.

    Methods:
        load_movies(source): Loads movies from the specified source.
        save_movies(destination): Saves movies to the specified destination.
        close(): Closes the file handler.
    """
    def __init__(self, file_type="json", db_name="movies.db", max_movies=None):
        self.handler = FileHandlerFactory.create_file_handler(file_type, db_name, max_movies)

    def load_movies(self, source):
        self.handler.load_movies(source)

    def save_movies(self, destination):
        self.handler.save_movies(destination)

    def close(self):
        self.handler.close()
