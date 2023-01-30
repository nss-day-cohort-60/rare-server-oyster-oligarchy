import sqlite3

from models import Post, User, Categories, PostDetails

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
            b.first_name user_first_name,
            b.last_name user_last_name,
            c.label category_label
            FROM Posts a
            JOIN Users b 
            ON b.id = a.user_id
            JOIN Categories c 
            ON c.id = a.category_id
            ORDER BY a.publication_date DESC
        """)        # Initialize an empty list to hold all posts representations
        posts = []
        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()
        # Iterate list of data returned from database
        # for row in dataset:
        for row in dataset:
            # Create a post instance from the current row
            post = Post(row['id'], row['user_id'], row['category_id'], row['title'], row ['publication_date'], row['image_url'], row['content'], row['approved'])
            # Create a user instance from the current row
            user = User(row['id'], row['user_first_name'], row['user_last_name'], None, None, None, None, None, None, None)
            # Create an category instance from the current row
            category = Categories(row['id'], row['category_label'])
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
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved,
            u.id user_id,
            u.first_name,
            u.last_name,
            u.email user_email,
            c.id category_id,
            c.label
            FROM Posts p
            JOIN Users u 
            ON u.id = p.user_id
            JOIN Categories c 
            ON c.id = p.category_id
        WHERE p.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an post instance from the current row
        post = PostDetails(data['title'], data['first_name'], data['last_name'], data['label'], data ['publication_date'],  data['content'], )

    return post.__dict__

def get_posts_by_user(query_params):
    # connection to the database
    with sqlite3.connect("./loaddata.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        sort_by = ""
        where_clause = ""
        if len(query_params) != 0:
            param = query_params[0]
            qs_key = 0
            [qs_key, qs_value] = param.split("=")

            if qs_key == "user_id":
                if qs_value != '0':
                    where_clause = f"WHERE p.user_id = {qs_value}"
                    sort_by = " ORDER BY u.id"
                # elif qs_value == '2':
                #     where_clause = f"WHERE a.user_id = {qs_value}"
                #     sort_by = " ORDER BY u.id"
                # elif qs_value == '3':
                #     where_clause = f"WHERE a.user_id = {qs_value}"
                #     sort_by = " ORDER BY u.id"
                # elif qs_value == '4':
                #     where_clause = f"WHERE a.user_id = {qs_value}"
                    # sort_by = " ORDER BY u.id"
        else:
            where_clause = ""
            sort_by = ""



        # SQL query to get the information you want
        sql_to_execute = f"""
        SELECT 
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved,
            u.id,
            u.first_name,
            u.last_name,
            u.email,
            u.bio,
            u.username,
            u.password,
            u.profile_image_url,
            u.created_on,
            u.active
            FROM Posts p
            JOIN `Users` u
                on u.id = p.user_id
            {where_clause}
            {sort_by}
        """

        
        db_cursor.execute(sql_to_execute)
        # Initialize an empty list to hold all posts representations
        posts = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        # for row in dataset:

        for row in dataset:

            # Create a post instance from the current row
            post = Post(row['id'], row['user_id'], row['category_id'], row['title'], row ['publication_date'], row['image_url'], row['content'], row['approved'])


            posts.append(post.__dict__)

    return posts
