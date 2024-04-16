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
from sqlalchemy import desc


# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

# Create a Flask app context
with app.app_context():
    # Fetch all meals from the database
    current_date = datetime.now().date().isoformat()

#     # Retrieve meal items for the current date
    meals= Meals.query.filter_by(date=current_date).order_by(desc(Meals.id)).first()
    print(meals)
    # meals = Meals.query.all()
    print(meals.date)
    print("User Name:", (meals.user_name))
    print("Breakfast:", meals.breakfast)
    print("Lunch:", meals.lunch)
    print("Dinner:", meals.dinner)
    print(type(meals.breakfast)) #entire list is a string!!
    bi= ast.literal_eval(meals.breakfast)
    li=ast.literal_eval(meals.lunch)
    di=ast.literal_eval(meals.dinner)
    # Loop through the fetched meals and print their attributes

        
    foodcal=0
    print(type(meals.date))
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
        
    total_carbs = 0
    total_carbs += sum(item[4] for item in bi)
    total_carbs += sum(item[4] for item in li)
    total_carbs += sum(item[4] for item in di)
    print("carbs: ",total_carbs )
        
    total_cholesterol = 0
    total_cholesterol += sum(item[5] for item in bi)
    total_cholesterol += sum(item[5] for item in li)
    total_cholesterol += sum(item[5] for item in di)
    print("cholesterol: ", total_cholesterol)
        
    sodium= 0
    sodium += sum(item[6] for item in bi)
    sodium += sum(item[6] for item in li)
    sodium+= sum(item[6] for item in di)
    print("sodium: ", sodium)
        
    potas=0
    potas += sum(item[7] for item in bi)
    potas+= sum(item[7] for item in li)
    potas += sum(item[7] for item in di)
    print("potassium: ", potas)
        
    sugar = 0
    sugar += sum(item[8] for item in bi)
    sugar+= sum(item[8] for item in li)
    sugar+= sum(item[8] for item in di)
    print("sugar: ", sugar)
