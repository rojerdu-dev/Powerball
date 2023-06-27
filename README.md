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
