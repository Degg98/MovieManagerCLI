import argparse
import os
import yaml

from movies.movie_collection import MovieCollection
from movies.movie_factory import MovieFactory, ReelFactory
from movies.movie_recommendation import MovieRecommendation
from utils.file_handler import FileHandler

""" 
    Command-line interface for managing a movie collection. 
    
    The cli function provides a command-line interface for managing a movie collection.
    It uses the argparse module to parse command-line arguments and perform the appropriate actions.
    
    The cli function supports the following command-line arguments:
    --list: List all movies in the collection.
    --add: Add a new movie to the collection.
    --delete: Delete a movie from the collection.
    --load: Load movies from a file.
    --retrieve: Retrieve movies by title, genre, or rating.
    --stats: Calculate statistics about the collection.
    --recommend: Recommend movies similar to a given title.


    The cli function uses the MovieCollection and MovieRecommendation classes to manage the movie collection and recommend movies.
    The cli function uses the FileHandler class to load movies from a file.
    The cli function uses the MovieFactory class to create Movie objects.
"""

def cli():
    parser = argparse.ArgumentParser(description="Movie Manager CLI")
    parser.add_argument("--add", nargs=4, metavar=("TITLE", "GENRE", "YEAR", "RATING"), help="Add a new movie")
    parser.add_argument("--delete", nargs=2, metavar=("TITLE", "YEAR"), help="Delete a movie")
    parser.add_argument("--load", metavar="FILE", help="Load movies from a file.")
    parser.add_argument("--retrieve", nargs=2, metavar=("FILTER", "VALUE"), help="Retrieve movies by title, genre, or rating")
    parser.add_argument("--stats", action="store_true", help="Calculate and display collection statistics")
    parser.add_argument("--recommend", metavar="TITLE", help="Recommend movies based on title")
    parser.add_argument("--list", action="store_true", help="List all movies in the collection")

    args = parser.parse_args()

    with open("config.yaml", "r") as file:
        config = yaml.safe_load(file)
    
    db_name = config['database']['db_name']
    rating_tolerance = config['recommendation']['rating_tolerance']
    max_movies = config['file_import']['max_movies']
    default_command = config['cli_settings']['default_command']

    factory = MovieFactory()
    collection = MovieCollection(db_name=db_name, factory=factory)


    if args.list:
        movies = collection.list_movies()
        for movie in movies:
            print(movie)

    if args.add:
        title, genre, year, rating = args.add
        movie = factory.create_movie(title, genre, int(year), float(rating))
        collection.add_movie(movie)
    
    if args.delete:
        title, year = args.delete
        confirm = input(f"Are you sure you want to delete the movie {title} ({year})? (y/n): ")
        if confirm.lower() == "y":
            collection.delete_movie(title, int(year))
        else:
            print("Deletion canceled.")

    if args.load:
        if not os.path.isfile(args.load):
            print(f"File '{args.load}' does not exist.")
            return
        file_type = args.load.split(".")[-1]
        file_handler = FileHandler(file_type=file_type, max_movies=max_movies, db_name=db_name)
        file_handler.load_movies(args.load)

    if args.retrieve:
        filter_type, value = args.retrieve
        if filter_type == "title":
            movies = collection.get_movie_by_title(value)
        elif filter_type == "genre":
            movies = collection.get_movies_by_genre(value)
            print(f"Movies with genre '{value}':")
        elif filter_type == "rating":
            movies = collection.get_movies_by_rating(float(value))
            print(f"Movies with rating >= {value}:")
        else:
            print("Invalid filter type.")
            return
        if movies:
            for movie in movies:
                print(movie)

    if args.stats:
        stats = collection.calculate_statistics()
        if stats:
            print(f"Average Rating: {stats['average_rating']}")
            print(f"Most Recent Movie: {stats['most_recent_movie']}")
            print(f"Highest Rated Movie: {stats['highest_rated_movie']}")
        else:
            print("No movies in the collection.")

    if args.recommend:
        base_movie = collection.get_movie_by_title(args.recommend)
        if not base_movie:
            print(f"Movie '{args.recommend}' not found.")
        else:
            base_movie = base_movie[0] # Get the first movie with the given title
            print(f"Base movie: {base_movie}")
            print(f"Suggesting movies with rating within {rating_tolerance} of the base movie.")
            recommender = MovieRecommendation()
            recommendations = recommender.recommend(collection, base_movie, rating_tolerance)
            print("Recommended movies:")
            for movie in recommendations:
                print(movie)
    
    if not any(vars(args).values()):
        print(parser.print_help())

    collection.close()

