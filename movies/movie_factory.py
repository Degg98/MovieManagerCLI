from .movie import Movie, AbstractMovieFactory

class ConcreteMovie(Movie):
    pass

class MovieFactory(AbstractMovieFactory):
    def create_movie(self, title: str, genre: str, release_year: int, rating: float) -> Movie:
        return ConcreteMovie(title, genre, release_year, rating)
