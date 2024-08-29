from .json_file_handler import JsonFileHandler
from .xml_file_handler import XmlFileHandler

class FileHandlerFactory:
    """
    Create a file handler based on the given file type.

    Parameters:
        file_type (str): The type of the file handler to create. Supported types are "json" and "xml".
        db_name (str): The name of the database file. Default is "movies.db".

    Returns:
        FileHandler: An instance of the file handler based on the given file type.

    Raises:
        ValueError: If the given file type is not supported.
    """
    @staticmethod
    def create_file_handler(file_type, db_name="movies.db"):
        if file_type == "json":
            return JsonFileHandler(db_name)
        if file_type == "xml":
            return XmlFileHandler(db_name)
        else:
            raise ValueError(f"Unsupported file type: {file_type}")
