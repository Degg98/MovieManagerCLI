import argparse
from movies.movie_collection import MovieCollection
from movies.movie_recommendation import MovieRecommendation
from utils.file_handler import FileHandler
from movies.movie_factory import MovieFactory

def main():
    parser = argparse.ArgumentParser(description="Manage your movie collection.")
    
    parser.add_argument("--add", nargs=4, metavar=('TITLE', 'GENRE', 'YEAR', 'RATING'),
                        help="Add a new movie to the collection.")
    parser.add_argument("--load", metavar="FILE", help="Load movies from a file.")
    parser.add_argument("--retrieve", nargs=2, metavar=('CRITERIA', 'VALUE'),
                        help="Retrieve movies by title, genre, or rating.")
    parser.add_argument("--stats", action='store_true', help="Calculate statistics about the collection.")
    parser.add_argument("--recommend", metavar="TITLE", help="Recommend movies similar to the given title.")
    
    args = parser.parse_args()
    collection = MovieCollection()
    factory = MovieFactory()

    if args.add:
        title, genre, year, rating = args.add
        movie = factory.create_movie(title, genre, int(year), float(rating))
        collection.add_movie(movie)
        print(f"Added movie: {movie}")

    if args.load:
        movies = FileHandler.load_from_file(args.load)
        for movie in movies:
            collection.add_movie(movie)
        print(f"Loaded {len(movies)} movies from {args.load}")

    if args.retrieve:
        criteria, value = args.retrieve
        if criteria.lower() == "title":
            movies = collection.get_movies_by_title(value)
        elif criteria.lower() == "genre":
            movies = collection.get_movies_by_genre(value)
        elif criteria.lower() == "rating":
            movies = collection.get_movies_by_rating(float(value))
        else:
            movies = []
        
        for movie in movies:
            print(movie)

    if args.stats:
        stats = collection.calculate_statistics()
        if stats:
            print(f"Average Rating: {stats['average_rating']:.2f}")
            print(f"Most Recent Movie: {stats['most_recent_movie']}")
            print(f"Highest Rated Movie: {stats['highest_rated_movie']}")
        else:
            print("No movies in the collection.")

    if args.recommend:
        base_movie = collection.get_movies_by_title(args.recommend)[0]
        recommender = MovieRecommendation()
        recommendations = recommender.recommend(collection, base_movie)
        print("Recommended movies:")
        for movie in recommendations:
            print(movie)

if __name__ == "__main__":
    main()
