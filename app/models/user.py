from ..router import app
from .model import db

class User(db.Model):
    __tablename__ = 't_user'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    email = db.Column(db.String(255))
    tel = db.Column(db.String(255))
    birth_date = db.Column(db.String(255))
    
    def __init__(self, username, password, email, tel, birthdate) -> None:
        self.username = username
        self.password = password
        self.email = email
        self.tel = tel
        self.birthdate = birthdate
        
        db.create_all()
    
    