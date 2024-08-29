from movies.movie_factory import MovieFactory
from movies.movie_db import MovieDB
from utils.file_handler_base import FileHandlerBase

import xml.etree.ElementTree as ET

class XmlFileHandler(FileHandlerBase):
    def __init__(self, db_name="movies.db", max_movies=None):
        self.db = MovieDB(db_name)
        self.factory = MovieFactory()
        self.max_movies = max_movies

    def load_movies(self, xml_file):
        """Load movies from an XML file and add them to the database."""
        try:
            tree = ET.parse(xml_file)
            root = tree.getroot()
            added_movies = 0
            for movie_element in root.findall('movie'):
                title = movie_element.find('title').text
                genre = movie_element.find('genre').text
                release_year = movie_element.find('release_year').text
                rating = movie_element.find('rating').text

                if self.max_movies is not None and added_movies >= self.max_movies:
                    print(f"Maximum number of movies ({self.max_movies}) reached.")
                    added_movies = self.max_movies
                    break

                movie = self.factory.create_movie(
                    title=title,
                    genre=genre,
                    release_year=release_year,
                    rating=rating
                )
                added_movies = added_movies + int(self.db.add_movie(movie))

            print(f"Successfully loaded {added_movies} movies from {xml_file}.")
        except Exception as e:
            print(f"Error loading movies from {xml_file}: {e}")

    def save_movies(self, xml_file):
        """Save the current movies from the database to an XML file."""
        try:
            movies = self.db.get_all_movies()

            root = ET.Element('movies')
            for movie in movies:
                movie_element = ET.SubElement(root, 'movie')

                title_element = ET.SubElement(movie_element, 'title')
                title_element.text = movie[0]

                genre_element = ET.SubElement(movie_element, 'genre')
                genre_element.text = movie[1]

                release_year_element = ET.SubElement(movie_element, 'release_year')
                release_year_element.text = movie[2]

                rating_element = ET.SubElement(movie_element, 'rating')
                rating_element.text = movie[3]

            tree = ET.ElementTree(root)
            tree.write(xml_file)

            print(f"Successfully saved movies to {xml_file}.")
        except Exception as e:
            print(f"Error saving movies to {xml_file}: {e}")

    def close(self):
        """Close the database connection."""
        self.db.close()