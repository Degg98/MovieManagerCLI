from .json_file_handler import JsonFileHandler
from .xml_file_handler import XmlFileHandler

class FileHandlerFactory:
    @staticmethod
    def create_file_handler(file_type, db_name="movies.db"):
        if file_type == "json":
            return JsonFileHandler(db_name)
        if file_type == "xml":
            return XmlFileHandler(db_name)
        else:
            raise ValueError(f"Unsupported file type: {file_type}")
