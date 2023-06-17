from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()







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
db.create_all()
