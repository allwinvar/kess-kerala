from data_fetcher import fetch_data_from_db
from data_fetcher import fetch_this_article
import data_put
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import os
from datetime import date
import random
import string

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../articles.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
class User(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    author = db.Column(db.String(100))
    published_date = db.Column(db.String(20))
    reading_time = db.Column(db.String(10))
    thumbnail_image = db.Column(db.String(100))
    detailed_article = db.Column(db.Text)
    article_url = db.Column(db.String(100))

admin = Admin(app, name='Admin Panel', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))


@app.route('/')
def index():
    data= fetch_data_from_db()
    return render_template('index.html',data=data)


@app.route('/article/<path:url>')
def article(url):
    article=fetch_this_article(url)
    return render_template('article.html', data=article)

@app.route('/postsmith', methods=['GET', 'POST'])
def postsmith():
    if request.method == 'POST' and 'thumbnail_image' in request.files:
        title = request.form.get('title')
        content = request.form.get('content')
        author = request.form.get('author')
        published_date = date.today()
        detailed_article = request.form.get('detailed_article')

        # Calculate reading time based on the number of words
        words = detailed_article.split()
        num_words = len(words)
        reading_time = num_words / 200  # Assuming an average reading speed of 200 words per minute

        if 'thumbnail_image' in request.files:
            file = request.files['thumbnail_image']
            if file.filename != '':
                random_filename=''.join(random.choices(string.ascii_letters, k=12))

                # Get the file extension
                _, ext = os.path.splitext(file.filename)
                # Append the extension to the random filename
                filename = random_filename + ext
                file.save(os.path.join(app.static_folder, 'uploads', filename))
        random_url = ''.join(random.choices(string.ascii_lowercase + string.digits, k=24))


        data_put.insert_post(title, content, author, published_date, reading_time,filename, detailed_article,random_url)
        return redirect('/')
    return render_template('postsmith.html')


if __name__ == '__main__':
    app.run(port=7777,debug=True,use_reloader=True)  # Change the port number to 7777 or any available port