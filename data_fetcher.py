import sqlite3

def fetch_data_from_db():
    db_path = 'articles.db'  # Provide the correct path to your database file

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