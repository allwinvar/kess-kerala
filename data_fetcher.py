import sqlite3
from os import path

def fetch_data_from_db():
    # Get the directory of the current script
    current_dir = path.dirname(path.abspath(__file__))

    # Specify the filename of the database
    db_filename = 'articles.db'

    # Construct the full path to the database
    db_path = path.join(current_dir, db_filename)


    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM posts ')

    # Iterate over the results and create a list of dictionaries.
    data = [
        {'id': value[0], 'title': value[1], 'content': value[2], 'author': value[3], 'date': value[4], 'reading_time': value[5], 'thumbnail': value[6], 'detailed_article': value[7]}
        for value in cursor.fetchall()
    ]

    conn.close()

    return data