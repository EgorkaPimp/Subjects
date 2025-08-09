from ..extensions import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    real_name = db.Column(db.String(50))
    password = db.Column(db.String(20))
    role_master = db.Column(db.Integer)