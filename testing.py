from models import db, Meals
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.inspection import inspect
from models import db, Meals
from flask import Flask
import json
import ast
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

# Create a Flask app context
with app.app_context():
    # Fetch all meals from the database
    current_date = datetime.now().date().isoformat()

#     # Retrieve meal items for the current date
    meals = Meals.query.filter_by(date=current_date).all()

    # meals = Meals.query.all()

    # Loop through the fetched meals and print their attributes
    for meal in meals:
        print("Date:", meal.date)
        print("User Name:", (meal.user_name))
        print("Breakfast:", meal.breakfast)
        print("Lunch:", meal.lunch)
        print("Dinner:", meal.dinner)
        print(type(meal.breakfast)) #entire list is a string!!
        bi= ast.literal_eval(meal.breakfast)
        li=ast.literal_eval(meal.lunch)
        di=ast.literal_eval(meal.dinner)
        foodcal=0
        print(type(meal.date))
        for i in bi:
            foodcal+= i[1]
        for i in li:
            foodcal+=i[1]
        for i in di:
            foodcal+=i[1]
        print("Total Calories today: ",foodcal)
        
        fats=0
    
        for i in bi:
            fats+= i[2]
        for i in li:
            fats+=i[2]
        for i in di:
            fats+=i[2]
        print("Total Fats consumed today: ",fats, "g")

        proteins=0
    
        for i in bi:
            proteins+= i[3]
        for i in li:
            proteins+=i[3]
        for i in di:
            proteins+=i[3]
        print("Total Proteins consumed today: ",proteins, "g")
