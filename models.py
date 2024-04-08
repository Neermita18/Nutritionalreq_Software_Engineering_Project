from flask_sqlalchemy import SQLAlchemy
db= SQLAlchemy()
import bcrypt
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def __init__(self,email,password,name):
        self.name = name
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    def check_password(self,password):
        return bcrypt.checkpw(password.encode('utf-8'),self.password.encode('utf-8'))
class Meals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    user_name = db.Column(db.String(100), nullable=False)
    breakfast = db.Column(db.String(200))
    lunch = db.Column(db.String(200))
    dinner = db.Column(db.String(200))
    
    def __init__(self, date, user_name, breakfast, lunch, dinner):
        self.date = date
        self.user_name = user_name
        self.breakfast = breakfast
        self.lunch = lunch
        self.dinner = dinner
