import sqlite3
from .movie import Movie
from .movie_factory import MovieFactory

class MovieDB:
    def __init__(self, db_name="movies.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_table()
        self.factory = MovieFactory()

    def _create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS movies (
                title TEXT,
                genre TEXT,
                release_year INTEGER,
                rating REAL
            )
        ''')
        self.conn.commit()

    @staticmethod
    def format_string(input_string):
        """
        This function handle the formatting of strings according to specific rules.
        Return a string with the first letter of each word capitalized and each word separated by a space.

        examples:
            The shawshank  redemption --> The Shawshank Redemption
            inception --> Inception
        """
        words = input_string.split()
        
        capitalized_words = [word.capitalize() for word in words]
        
        result = ' '.join(capitalized_words)

        return result

    def check_movie_exists(self, title, release_year):
        cursor = self.conn.cursor()
        title = self.format_string(title)
        cursor.execute("SELECT * FROM movies WHERE title = ? AND release_year = ?", (title, release_year))
        result = cursor.fetchone()
        return result is not None

    def add_movie(self, movie):
        movie.title = self.format_string(movie.title)
        movie.genre = self.format_string(movie.genre)
        if self.check_movie_exists(movie.title, movie.release_year):
            print(f"Movie '{movie.title}' already exists in the database.")
            return False
        self.cursor.execute('''
            INSERT INTO movies (title, genre, release_year, rating)
            VALUES (?, ?, ?, ?)
        ''', (movie.title, movie.genre, movie.release_year, movie.rating))
        print(f"Movie '{movie.title}' added successfully!")
        self.conn.commit()
        return True

    def get_movie_by_title(self, title):
        title = self.format_string(title)
        self.cursor.execute('SELECT * FROM movies WHERE title = ?', (title,))
        rows = self.cursor.fetchall()
        movies = []
        for row in rows:
            movie = self.factory.create_movie(
                title=row[0],
                genre=row[1],
                release_year=row[2],
                rating=row[3]
            )
            print(f"Movie '{title}' found!")
            movies.append(movie)
            return movies
        return None

    def get_all_movies(self):
        self.cursor.execute('SELECT * FROM movies')
        rows = self.cursor.fetchall()
        movies = []
        for row in rows:
            movie = self.factory.create_movie(
                 title=row[0],
                genre=row[1],
                release_year=row[2],
                rating=row[3]
            )
            movies.append(movie)
        return movies

    def get_movies_by_genre(self, genre):
        # genre = self.format_string(genre)
        self.cursor.execute('SELECT * FROM movies WHERE genre = ?', (genre,))
        rows = self.cursor.fetchall()
        movies = []
        for row in rows:
            movie = self.factory.create_movie(
                title=row[0],
                genre=row[1],
                release_year=row[2],
                rating=row[3]
            )
            movies.append(movie)
        return movies

    def get_movies_by_rating(self, min_rating, max_rating=None):
        if max_rating:
            self.cursor.execute('SELECT * FROM movies WHERE rating BETWEEN ? AND ?', (min_rating, max_rating))
        else:
            self.cursor.execute('SELECT * FROM movies WHERE rating >= ?', (min_rating,))
        rows = self.cursor.fetchall()
        movies = []
        for row in rows:
            movie = self.factory.create_movie(
                title=row[0],
                genre=row[1],
                release_year=row[2],
                rating=row[3]
            )
            movies.append(movie)
        return movies

    def calculate_statistics(self):
        cursor = self.conn.cursor()

        cursor.execute("SELECT AVG(rating) FROM movies")
        avg_rating = cursor.fetchone()[0]

        cursor.execute("SELECT title, MAX(release_year) FROM movies")
        most_recent_movie = cursor.fetchone()

        cursor.execute("SELECT title, MAX(rating) FROM movies")
        highest_rated_movie = cursor.fetchone()

        return {
            'average_rating': avg_rating,
            'most_recent_movie': most_recent_movie[0],
            'highest_rated_movie': highest_rated_movie[0]
        }
    
    def delete_movie(self, title, release_year):
        title = self.format_string(title)
        self.cursor.execute('''
            DELETE FROM movies WHERE title = ? AND release_year = ?
        ''', (title, release_year))
        self.conn.commit()
        print(f"Movie '{title}' deleted successfully!")

    def close(self):
        self.conn.close()
