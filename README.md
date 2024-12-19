# Weather Data Storage Web Application

This application reads real-world weather data from a CSV file (`Weather Training Data.csv`), stores it in an SQLite database, and allows users to view the data and statistical summaries through a web interface built with Flask. The application follows a 3-tier architecture, utilizing Flask for the web server, SQLAlchemy for database management, and HTML templates for the frontend interface.

## Features

- **Core Files and Classes:** 
  - `WeatherFileReader`: Handles reading weather data from the CSV file.
  - `WeatherDataClass`: Manages loading data and storing it in the database.
  - `WeatherStatistics`: Calculates statistical summaries from the stored weather data.

- **Database Integration:**
  - The data is stored in an SQLite database using SQLAlchemy.
  - SQLAlchemy’s ORM is used to define the `WeatherData` model, which represents the weather data table in the database.

- **Web Interface:**
  - Built with Flask, with HTML templates using Jinja for dynamic content rendering.
  - Users can load data from the CSV file into the database and view data and calculated statistics on dedicated web pages.

- **Authentication System:**
  - Password-protected access to all routes
  - Session-based authentication
  - Secure login page
  - Protected routes using Flask's session management

- **Error Handling and Logging:** 
  - Comprehensive error handling is implemented for file reading, data loading, and database operations.
  - Logging is set up across all modules to track application activity.

## Prerequisites

- Python 3.12
- `alex_nin_module`
- `pandas`
- `Flask`
- `Flask-SQLAlchemy`
- `SQLAlchemy`
- A CSV file named `Weather Training Data.csv` (because the file name within the program is not editable) containing weather data, with the first column as the date.

## Package Installation

To install the appropriate packages, execute the following command in your terminal in the program directory:

- **Mac:**
```bash
python3 -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ alex_nin_module pandas flask flask-sqlalchemy sqlalchemy
```
- **Windows:**
```bash
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ alex_nin_module pandas flask flask-sqlalchemy sqlalchemy
```
## Installation

1. Ensure you have Python 3.12 installed on your system.
2. Place the `Weather Training Data.csv` file in a `/data` directory, if it's not there already.

## Usage

- **Program Execution:**
  - To run the program, execute the following command in your terminal in the program directory:

```bash
python3 app.py
```

- **Authentication:**
  - When first accessing the application, you'll be prompted for a password
  - Default password is set in app.py (CORRECT_PASSWORD variable)
  - After successful authentication, you'll have access to all features

- **Application Routes:**
  - `/`: Login page for authentication
  - `/index`: The main page with options to load data and view data/statistics (requires authentication)
  - `/load-data`: Reads the weather database, stores data in the SQLite database (requires authentication)
  - `/list-data`: Displays all weather data from the database along with calculated statistics (requires authentication)

## Example Walkthrough

1. **Access the Application:** After executing program in terminal go to http://127.0.0.1:5000
2. **Login:** Enter the correct password in the login page, default password is 'pythonisfun'. It is also located on line 16 of app.py
3. **Navigate:** After successful authentication, you'll be redirected to the main page
4. **Load Data:** Click on the "Load Data" link to read the CSV file and store the data in the database
5. **View Data and Statistics:** Navigate to "View Data and Statistics" to see the stored data and summary statistics

## Code Overview

- **Main Application File (`app.py`)**:
  - Sets up the Flask application and database connection and defines routes defined in the Usage section.

- **Authentication System (`app.py`):**
  - Implements Flask session management for secure access
  - Uses decorators to protect routes
  - Manages user authentication state

- **Configuration Settings (`config.py`)**:
  - Contains database and app settings for Flask.
  - Uses `SQLALCHEMY_DATABASE_URI` to specify the SQLite database location.

- **Database Model (`models.py`)**:
  - Defines the WeatherData class, representing weather data entries in the SQLite database.
  - The `db` object from SQLAlchemy is initialized here to create the database structure.

- **Weather Data Reader (`utils/weather_reader.py`):**
  - Contains `WeatherFileReader`, which reads the CSV file and converts it into a pandas DataFrame.
  - Implements error handling for file reading issues.

- **Weather Data Management (`utils/weather_data.py`):**
  - Contains the `WeatherData` class, which loads weather data using `WeatherFileReader`.
  - Manages data loading, storage in the database, and logging.

- **Weather Statistics Calculation (`utils/weather_statistics.py`):**
  - Contains `WeatherStatistics`, which calculates statistics like average min/max temperature and total rainfall.
  - Uses pandas for data processing.

## Templates Overview

**`templates/index.html`**:
  - The homepage with links to load data and view data/statistics.

**`templates/list_data.html`**:
  - Displays weather data stored in the database.
  - Shows calculated statistics, such as average temperatures and total rainfall.

**`templates/login.html`**:
  - Provides secure login interface
  - Handles password submission
  - Displays error messages for incorrect passwords


## OOP Design and Principles Applied

- **Encapsulation:** Data fetching, processing, and storage are encapsulated within distinct classes (`WeatherData` and `WeatherStatistics`), keeping functionality modular and maintainable.

- **Abstraction:** Implementation details such as reading data from a file and calculating statistics are hidden behind class methods, exposing only the necessary interfaces (`store_weather_data()` and `calculate_statistics()`).

- **Single Responsibility Principle (SRP):** Each class has a single responsibility:
  - `WeatherFileReader`: Reads weather data from the CSV file.
  - `WeatherData`: Manages the data loading and access.
  - `WeatherStatistics`: Handles statistical calculations on the data.

- **Composition:** The `WeatherData` class depends on `WeatherFileReader` to fetch the data, demonstrating the composition principle by including the file reader object within `WeatherData`.

- **Error Handling:** Each class has its own error handling mechanisms, ensuring that issues like file not found or improper data usage are dealt with appropriately.

- **Logging:** Comprehensive logging is implemented across all classes for better debugging and monitoring.

## Testing and Debugging

  - **Debug Mode:** Flask's debug mode is enabled in app.py for development. Restart the application after any code changes to see updates immediately.
  - **Error Messages:** Errors (e.g., file not found) are logged and displayed as JSON responses or messages on the web interface.

## Pytest and Doctest Overview

- The pytest framework is used to test the functionality of the `WeatherFileReader`, `WeatherData`, and `WeatherStatistics` classes.
- Each class has a corresponding test file in the `tests` directory.
- Tests are written using the `assert` statement to verify expected behavior.

- **test_weather_reader.py:** Tests the `WeatherFileReader` class.
  - `test_weather_reader_instantiation()`: Tests the instantiation of the `WeatherFileReader` class.
  - `test_read_file_data()`: Tests the `read_file()` method of the `WeatherFileReader` class.
  - `test_read_file_data_io_error()`: Tests the `read_file()` method of the `WeatherFileReader` class with an IOError.
  - `test_test_read_file_data_data_failed_to_read()`: Tests the `read_file()` method of the `WeatherFileReader` class with a RuntimeError.
  
- **test_weather_data.py:** Tests the `WeatherData` class.
  - `test_weather_data_instantiation()`: Tests the instantiation of the `WeatherData` class.
  - `test_load_data()`: Tests the `load_data()` method of the `WeatherData` class.
  - `test_load_data_io_error()`: Tests the `load_data()` method of the `WeatherData` class with an IOError.
  - `test_load_data_failed_to_load_data()`: Tests the `load_data()` method of the `WeatherData` class with a RuntimeError.

- **test_weather_statistics.py:** Tests the `WeatherStatistics` class.
  - `test_weather_statistics_instantiation()`: Tests the instantiation of the `WeatherStatistics` class.
  - `test_calculate_statistics()`: Tests the `calculate_statistics()` method of the `WeatherStatistics` class.
  - `test_calculate_statistics_invalid_format()`: Tests the `calculate_statistics()` method of the `WeatherStatistics` class with an invalid data format.

- Doctests have been added to the `main.py` file:
  - `stats_generator()`: Includes doctests to verify the function's behavior with both list and single item inputs.
  - `setup_logger()`: Includes a doctest to verify that the function returns a `logging.Logger` instance.
  - `filter_high_rainfall_days()`: Includes a doctest to verify the function filters days with rainfall exceeding 50mm correctly.

## Doctest Instructions

To run the doctests in the `main.py` file, execute the following command in your terminal:

```bash
python3 -m doctest -v main.py
```

## Pytest Instructions 

- To run the tests, execute the following command in your terminal:

```bash
PYTHONPATH=$(pwd) pytest test_weather_reader.py test_weather_data.py
```

## Pydoc Instructions 

- To create a document, execute the following command in your terminal:

```bash
python3 -m pydoc -w main
```

- To run the newly created .html file, execute the following command in your terminal:

```bash
open main.html
```