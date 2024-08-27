from abc import ABC, abstractmethod

class FileHandlerBase(ABC):
    @abstractmethod
    def load_movies(self, source):
        pass

    @abstractmethod
    def save_movies(self, destination):
        pass