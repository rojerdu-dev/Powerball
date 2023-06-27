import sqlite3

import requests
from tqdm import tqdm


def get_data_from_api(rows: int) -> None:
    url = f"http://127.0.0.1:8000/drawing/{rows}"

    with requests.get(url, stream=True) as r:
        conn = sqlite3.connect("powerball_data.db")
        cursor = conn.cursor()

        create_table_query = """
            CREATE TABLE IF NOT EXISTS powerball_results (
                transaction_id TEXT PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                city TEXT,
                state TEXT,
                customer_id TEXT, 
                powerball_1 INTEGER, 
                powerball_2 INTEGER, 
                powerball_3 INTEGER, 
                powerball_4 INTEGER, 
                powerball_5 INTEGER, 
                powerball_number INTEGER
                )
        """
        cursor.execute(create_table_query)

        insert_query = """  
            INSERT INTO powerball_results (
                transaction_id,
                first_name,
                last_name,
                city,
                state,
                customer_id, 
                powerball_1, 
                powerball_2, 
                powerball_3, 
                powerball_4, 
                powerball_5,
                powerball_number) 
                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

        for chunk in tqdm(r.iter_lines()):
            print(chunk)
            if chunk:
                data = chunk.decode("utf-8").strip()[1:-1].split(", ")
                cursor.execute(insert_query, data)
                conn.commit()

        cursor.close()
        conn.close()


if __name__ == "__main__":
    get_number = int(input("How many lucky winners today? "))
    get_data_from_api(get_number)
