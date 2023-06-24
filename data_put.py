import sqlite3
from os import path
def insert_post(title, content, author, published_date, reading_time, thumbnail_image, detailed_article):
    # Get the directory of the current script
    current_dir = path.dirname(path.abspath(__file__))

    # Specify the filename of the database
    db_filename = 'articles.db'

    # Construct the full path to the database
    db_path = path.join(current_dir, db_filename)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO posts (title, content, author, published_date, reading_time, thumbnail_image, detailed_article) "
        "VALUES (?, ?, ?, ?, ?, ?, ?)",
        (title, content, author, published_date, reading_time, thumbnail_image, detailed_article))

    conn.commit()
    conn.close()
