# Powerball Data Streaming & Storage 
This project demonstrates streaming Powerball data from a FastAPI server and storing it in a SQLite database. It generates mock Powerball data and provides an API endpoint to stream the data in real-time. The streamed data is then consumed by a client application and stored in a local SQLite database. 

# Installation 
1. Clone the repository

`https://github.com/rojerdu-dev/Powerball.git`

2. Change into the project directory:

`cd powerball` 

3. Install dependencies:

`pip install -r requirements.txt`

# Usage 
1. Start the FastAPI server:

`uvicorn main:app --host 0.0.0.0 --port 8000`

2. In a separate terminal window, run the client application to fetch and ingest the data:

`python ingest.py` 
* Follow the prompts to specify the number of lucky winners
* The client application will connect to the FastAPI server, stream the specified number of Powerball data rows, and store them in a SQLite database `powerball_data.db` in the project directory.

#API Endpoint 
#GET /drawing/{rows}
This endpoint streams mock Powerball data rows in real-time. 
* 'rows': the number of rows to stream

Example usage: 
`GET http://localhost:8000/drawing/10`

The response will be a streaming response containing the requested number of Powerball data rows. 

# Database Schema
The SQLite database `powerball_data.db` contains a single table: 

**powerball_results** 
| Column           | Type    | Description                    |
|------------------|---------|--------------------------------|
| transaction_id   | TEXT    | Unique transaction identifier  |
| first_name       | TEXT    | First name of the customer     |
| last_name        | TEXT    | Last name of the customer      |
| city             | TEXT    | City of the customer           |
| state            | TEXT    | State of the customer          |
| customer_id      | TEXT    | Unique customer identifier     |
| powerball_1      | INTEGER | Powerball number 1             |
| powerball_2      | INTEGER | Powerball number 2             |
| powerball_3      | INTEGER | Powerball number 3             |
| powerball_4      | INTEGER | Powerball number 4             |
| powerball_5      | INTEGER | Powerball number 5             |
| powerball_number | INTEGER | Powerball number               |

# Acknowledgments 
* [FastAPI](https://fastapi.tiangolo.com/) - FastAPI framekworking for building APIs with Python
* [SQLite](https://www.sqlite.org/index.html) - Embedded relational database management system
* [Faker](https://faker.readthedocs.io/en/master/v) - Library for generating relaistc fake data
* [tqdm](https://tqdm.github.io/) - Fast, extensible progress bar for Python
* [requests](https://requests.readthedocs.io/en/latest/) - Library for making HTTP requests
