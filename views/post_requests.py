import sqlite3
from models import Post, User, Categories

#  This module will import sqlite3 and Post class from models
# This module will show the initial structure of an POSTS dictionary
# This module will hold the functions created to get_all_posts and get_single_post

def get_all_posts():
    # connection to the database
    with sqlite3.connect("./loaddata.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # SQL query to get the information you want
        db_cursor.execute("""
        SELECT 
            a.id,
            a.user_id,
            a.category_id,
            a.title,
            a.publication_date,
            a.image_url,
            a.content,
            a.approved,
            b.id user_id,
            b.first_name user_first_name,
            b.last_name user_last_name,
            b.email user_email,
            c.id category_id,
            c.label
            FROM Posts a
            JOIN Users b 
            ON b.id = a.user_id
            JOIN Categories c 
            ON c.id = a.category_id
        """)

        # Initialize an empty list to hold all posts representations
        posts = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        # for row in dataset:

        for row in dataset:

            # Create a post instance from the current row
            post = Post(row['id'], row['user_id'], row['category_id'], row['title'], row ['publication_date'], row['image_url'], row['content'], row['approved'])

            # Create a user instance from the current row
            user = User(row['id'], row['user_first_name'], row['user_last_name'], row['email'], row['bio'], row['username'], row['password'], row['profile_image_url'], row['created_on'], row['active'])

            # Create an category instance from the current row
            category = Categories(row['id'], row['label'])

            # # Add the dictionary representation of the posts to the list

            post.user = user.__dict__
            post.category = category.__dict__

            posts.append(post.__dict__)

    return posts

def get_single_post(id):
    with sqlite3.connect("./loaddata.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT 
            a.id,
            a.user_id,
            a.category_id,
            a.title,
            a.publication_date,
            a.image_url,
            a.content,
            a.approved,
            b.id user_id,
            b.first_name user_first_name,
            b.last_name user_last_name,
            b.email user_email,
            c.id category_id,
            c.label
            FROM Posts a
            JOIN Users b 
            ON b.id = a.user_id
            JOIN Categories c 
            ON c.id = a.category_id
        WHERE a.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an post instance from the current row
        post = Post(data['id'], data['user_id'], data['category_id'], data['title'], data ['publication_date'], data['image_url'], data['content'], data['approved'])

        return post.__dict__