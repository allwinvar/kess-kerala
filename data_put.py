import sqlite3

def insert_post(title, content, author, published_date, reading_time, thumbnail_image, detailed_article):
    conn = sqlite3.connect('articles.db')
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO posts (title, content, author, published_date, reading_time, thumbnail_image, detailed_article) "
        "VALUES (?, ?, ?, ?, ?, ?, ?)",
        (title, content, author, published_date, reading_time, thumbnail_image, detailed_article))

    conn.commit()
    conn.close()
