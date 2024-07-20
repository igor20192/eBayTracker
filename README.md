# eBayTracker

eBay Tracker is a Python application that monitors eBay daily based on specified keywords and stores the retrieved data in a SQLite database. This project includes web scraping, data storage, scheduling, and logging functionalities.

## Features

- Retrieve data from eBay based on given keywords
- Store the retrieved data in a SQLite database
- Schedule daily data retrieval
- Log the process and errors

## Requirements

- Python 3.x
- Required libraries: `requests`, `beautifulsoup4`, `pandas`, `sqlite3`, `schedule`, `unittest`

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/igor20192/eBayTracker.git
    cd ebay-tracker
    ```

2. Install the required libraries:
    ```bash
    pip install requests beautifulsoup4 pandas schedule
    ```

## Usage

1. Run the script:
    ```bash
    python ebay_tracker.py
    ```

2. When prompted, enter the keyword for eBay search and the start time for daily retrieval:
    ```text
    Enter keyword: laptop
    Start time (e.g., 10:00): 10:00
    ```

## Code Overview

- `get_ebay_data(keywords)`: Retrieves data from eBay based on given keywords and returns it as a DataFrame.
- `store_data(df, db_name="ebay_data.db")`: Stores the given DataFrame into a SQLite database.
- `job()`: Executes the job of retrieving data from eBay and storing it into the database.

## Logging

The application logs its activities in `ebay_tracker.log` file, including data retrieval and errors.

## Running Tests

The project includes unit tests for the main functionalities. To run the tests, execute the following command:
```bash
python -m unittest test.py
```

## Contributing

1. Fork the repository
2. Create your feature branch (git checkout -b feature/feature-name)
3. Commit your changes (git commit -am 'Add some feature')
4. Push to the branch (git push origin feature/feature-name)
5. Create a new Pull Request

## Contact

If you have any questions, feel free to open an issue or contact me directly at [igor.udovenko2015@gmail.com].