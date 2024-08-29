# MovieManagerCLI

## Overview

**MovieManagerCLI** is a command-line application designed to manage a collection of movies. It allows users to add new movies, retrieve movies based on specific criteria, calculate statistics about the collection, and recommend similar movies based on genre and rating. The application also uses the Factory Method design pattern for efficient movie creation.

## Features

- **List Movie**: List movies in the collection.
- **Add Movie**: Add a new movie to the collection by specifying the title, genre, release year, and rating.
- **Delete Movie**: Remove a movie from the collection specifying the title and the release year.  
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
4. **Install Packages**
    ```bash
    pip install -e .
    ```
## Usage

The application is controlled via the command line. Below are some example commands to get you started.

### Configuration File (`config.yaml`)

The application is highly configurable via the `config.yaml` file, located in the root directory of the project. This file contains key parameters that define the behavior of the application. (**To do**: Define also the Movie Structure)

### Show collection

To show films in the collection:
```bash
moviemanager --list
```

### Adding a Movie

To add a new movie to the collection:
```bash
moviemanager --add "Inception" "Sci-Fi" 2010 8.8
```
### Removing a Movie
To remove a movie from the collection:
```bash
moviemanager --delete "Inception" 2010
```
### Loading Movies from a File

To load a collection of movies from a JSON file:
```bash
moviemanager --load data/collections/movies.json
```
To load a collection of movies froma XML file:
```bash
moviemanager --load data/collections/movies.xml
```

### Retrieving Movies

To retrieve movies by title, genre, or rating:
```bash
# By title
moviemanager --retrieve title "Inception"

# By genre
moviemanager --retrieve genre "Sci-Fi"

# By minimum rating
moviemanager --retrieve rating 8.5
```

### Calculating Statistics

To calculate and display statistics about the collection:
```bash
moviemanager --stats
```

### Recommending Movies

To get movie recommendations based on a given movie:
```bash
moviemanager --recommend "Inception"
```

## File Structure

```
MovieManagerCLI/               # Root directory of the project
├── cli.py                     # Handles command-line interface logic, parsing user inputs and invoking the appropriate functionality
├── config.xml                 # Configuration file that contains the settings for the movie recommender system.
├── data
│   └── collections            # Directory for storing movie data in various formats
│       ├── movies.json        # Sample movie data in JSON format
│       └── movies.xml         # Sample movie data in XML format
├── LICENSE                    # License file specifying the terms under which the project can be used
├── setup.py                   # Script used to install the MovieManagerCLI package and its dependencies.
├── main.py                    # Entry point of the application, initializes and runs the CLI
├── movies                     # Package containing core functionality related to movie management
│   ├── __init__.py            # Marks the directory as a Python package
│   ├── movie_collection.py    # Manages a collection of Movie objects, handles addition, retrieval, and statistics
│   ├── movie_db.py            # Manages database operations, such as storing and retrieving movies from an SQLite database
│   ├── movie_factory.py       # Implements the Factory Method pattern to create Movie instances
│   ├── movie.py               # Defines the Movie class with attributes like title, genre, release_year, and rating
│   ├── movie_recommendation.py# Contains logic to recommend movies based on genre and rating
│   └── .__pycache__           # Directory for storing compiled Python bytecode files for performance optimization
├── movies.db                  # SQLite database file where movies are stored persistently
├── README.md                  # Project documentation with instructions on setup, usage, and development
├── requirements.txt           # List of dependencies required to run the project, used with pip to install them
└── utils                      # Package containing utility modules for handling different file formats
    ├── csv_file_handler.py    # Handles reading and writing movie data in CSV format
    ├── file_handler_base.py   # Abstract base class defining a common interface for file handlers
    ├── file_handler_factory.py# Implements the Factory Method pattern to instantiate the appropriate file handler
    ├── file_handler.py        # Centralized logic to manage different file types (delegates to specific handlers)
    ├── __init__.py            # Marks the directory as a Python package
    ├── json_file_handler.py   # Handles reading and writing movie data in JSON format
    └── xml_file_handler.py    # Handles reading and writing movie data in XML format
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