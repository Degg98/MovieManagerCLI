from utils.file_handler_factory import FileHandlerFactory

class FileHandler:
    def __init__(self, file_type="json", db_name="movies.db"):
        self.handler = FileHandlerFactory.create_file_handler(file_type, db_name)

    def load_movies(self, source):
        self.handler.load_movies(source)

    def save_movies(self, destination):
        self.handler.save_movies(destination)

    def close(self):
        self.handler.close()
