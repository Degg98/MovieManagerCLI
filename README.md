# MovieManagerCLI

## Overview

**MovieManagerCLI** is a command-line application designed to manage a collection of movies. It allows users to add new movies, retrieve movies based on specific criteria, calculate statistics about the collection, and recommend similar movies based on genre and rating. The application also uses the Factory Method design pattern for efficient movie creation.

## Features

- **Add Movie**: Add a new movie to the collection by specifying the title, genre, release year, and rating.
- **Retrieve Movies**: Retrieve movies by title, genre, or rating.
- **Calculate Statistics**:
    - Calculate the average rating of all movies.
    - Identify the most recent movie based on the release year.
    - Identify the highest-rated movie in the collection.
- **Recommend Movies**: Given a movie, recommend other movies from the same genre with a similar rating.
- **Design Pattern**: Utilizes the Factory Method pattern to manage the creation of movie objects.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Degg98/MovieManagerCLI.git
    cd MovieManagerCLI
    ```

2. **Create a virtual environment** (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

The application is controlled via the command line. Below are some example commands to get you started.

### Adding a Movie

To add a new movie to the collection:
```bash
python main.py --add "Inception" "Sci-Fi" 2010 8.8
```

### Loading Movies from a File

To load a collection of movies from a JSON file:
```bash
python main.py --load movies.json
```

### Retrieving Movies

To retrieve movies by title, genre, or rating:
```bash
# By title
python main.py --retrieve title "Inception"

# By genre
python main.py --retrieve genre "Sci-Fi"

# By minimum rating
python main.py --retrieve rating 8.5
```

### Calculating Statistics

To calculate and display statistics about the collection:
```bash
python main.py --stats
```

### Recommending Movies

To get movie recommendations based on a given movie:
```bash
python main.py --recommend "Inception"
```

## File Structure

```
MovieManagerCLI/
│
├── movies/
│   ├── __init__.py
│   ├── movie.py                  # Base class Movie and Factory Method
│   ├── movie_factory.py          # Factory implementation for creating movies
│   ├── movie_collection.py       # Movie collection management
│   ├── movie_recommendation.py   # Recommendation algorithm
│
├── utils/
│   ├── __init__.py
│   ├── file_handler.py           # Functions for loading and saving files
│
├── cli.py                        # Command-line interface
├── main.py                       # Application entry point
├── requirements.txt              # Project dependencies
├── README.md                     # Project documentation
└── tests/                        # Test cases for the project
    ├── __init__.py
    ├── test_movie.py
    ├── test_movie_collection.py
    ├── test_movie_recommendation.py
    └── test_movie_factory.py     # Factory method tests
```

<!-- ## Testing

Unit tests have been implemented for all core components of the application. To run the tests, use the following command:

```bash
python -m unittest discover -s tests
```

The tests cover:
- Movie creation using the Factory Method.
- Managing the movie collection (adding, retrieving, calculating statistics).
- The recommendation algorithm.
- Factory Method functionality. -->

## JSON File Example

Below is an example of a `movies.json` file that can be used with this application:

```json
[
    {
        "title": "Inception",
        "genre": "Sci-Fi",
        "release_year": 2010,
        "rating": 8.8
    },
    {
        "title": "The Matrix",
        "genre": "Sci-Fi",
        "release_year": 1999,
        "rating": 8.7
    },
    {
        "title": "Interstellar",
        "genre": "Sci-Fi",
        "release_year": 2014,
        "rating": 8.6
    },
    {
        "title": "Parasite",
        "genre": "Thriller",
        "release_year": 2019,
        "rating": 9.1
    },
    {
        "title": "The Dark Knight",
        "genre": "Action",
        "release_year": 2008,
        "rating": 9.0
    },
    {
        "title": "Pulp Fiction",
        "genre": "Crime",
        "release_year": 1994,
        "rating": 8.9
    },
    {
        "title": "Forrest Gump",
        "genre": "Drama",
        "release_year": 1994,
        "rating": 8.8
    },
    {
        "title": "The Shawshank Redemption",
        "genre": "Drama",
        "release_year": 1994,
        "rating": 9.3
    },
    {
        "title": "Fight Club",
        "genre": "Drama",
        "release_year": 1999,
        "rating": 8.8
    },
    {
        "title": "The Godfather",
        "genre": "Crime",
        "release_year": 1972,
        "rating": 9.2
    }
]
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue.

---

**MovieManagerCLI** provides an efficient way to manage your movie collection directly from the command line, with built-in support for searching, statistical analysis, and recommendations.