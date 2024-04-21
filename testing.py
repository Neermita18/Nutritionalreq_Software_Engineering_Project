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
from sqlalchemy import func
from datetime import timedelta


# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/91982/Desktop/SEPROJECT/instance/database.db'
db.init_app(app)

# Create a Flask app context
with app.app_context():
    # Fetch all meals from the database
    current_date = datetime.now().date()
    start_date = current_date - timedelta(days=7)
    
    # Query the database to get the last row for each date in the range
    last_meals = db.session.query(Meals.date, func.max(Meals.id)).\
                 filter(Meals.date >= start_date, Meals.date <= current_date).\
                 group_by(Meals.date).all()
    print(last_meals)
    # Initialize a list to store the last meal for each date
    last_meals_data = []    
    for date, max_id in last_meals:
        meal = Meals.query.filter_by(date=date, id=max_id).first()
        print(meal)
    
    # meals = Meals.query.all()
        print(meal.date)
        print("User Name:", (meal.user_name))
        print("Breakfast:", meal.breakfast)
        print("Lunch:", meal.lunch)
        print("Dinner:", meal.dinner)
        print(type(meal.breakfast)) #entire list is a string!!
        bi= ast.literal_eval(meal.breakfast)
        li=ast.literal_eval(meal.lunch)
        di=ast.literal_eval(meal.dinner)
        # Loop through the fetched meals and print their attributes

                
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
        
        last_meals_data.append({
                'date': date,
                'total_calories': foodcal,
                'total_proteins': proteins,
                'total_carbs': total_carbs,
                'total_fats': fats,
                'total_cholesterol': total_cholesterol,
                'total_sodium': sodium,
                'total_potassium': potas,
                'total_sugar': sugar
            })
        meals=[]
print((last_meals_data))
print(last_meals_data[0]['date'])
print(len(last_meals_data))
for item in last_meals_data[::-1]:
        meals.append(item)
        
print(meals)