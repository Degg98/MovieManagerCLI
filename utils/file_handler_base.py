from abc import ABC, abstractmethod

class FileHandlerBase(ABC):
    @abstractmethod
    def load_movies(self, source, max_movies):
        pass

    @abstractmethod
    def save_movies(self, destination):
        pass