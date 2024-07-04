from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pattern(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pattern_type = db.Column(db.String(50))
    size = db.Column(db.String(10))
    data = db.Column(db.Text)