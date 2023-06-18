from data_fetcher import fetch_data_from_db
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

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

@app.route('/')
def index():
    data= fetch_data_from_db()
    print(data)
    return render_template('index.html',data=data)


@app.route('/new')
def new():
    return  render_template('new.html')


if __name__ == '__main__':
    app.run(port=7777,debug=True,use_reloader=True)  # Change the port number to 7777 or any available port