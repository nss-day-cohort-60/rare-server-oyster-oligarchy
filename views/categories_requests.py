import sqlite3
from models import Categories

def get_all_catagories():
    # connection to the database
    with sqlite3.connect("./loaddata.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            a.id,
            a.label
            FROM Categories a
            ORDER BY label ASC
        """)
        # Initialize an empty list to hold all posts representations
        categories = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        # for row in dataset:

        for row in dataset:

            category = Categories(row['id'], row['label'])

            categories.append(category.__dict__)

    return categories

def create_category(new_response):
    """Args: category (json string), returns new dictionary with id property added"""
    with sqlite3.connect('./loaddata.sqlite3') as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Categories
            ( label )
        VALUES
            ( ?);
        """, (new_response['label'],  ))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid
        
        # Adds the `id` property to the categories dictionary
        # so that the client sees the
        # primary key in the response.
        new_response['id'] = id

    return new_response