from flask import Flask, render_template, request, session, url_for, flash, redirect
import bcrypt
import json
from meal import get_req
from flask_sqlalchemy import SQLAlchemy
from waitress import serve
import requests
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from models import db,User, Meals
import ast
from sqlalchemy import desc
app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/91982/Desktop/SEPROJECT/instance/database.db'
db.init_app(app)
app.secret_key='heudbw2735snd0182bdh376ch3865271'


        	
with app.app_context():
    db.create_all()
with app.app_context():
    metadata = db.metadata
    
    # Get the specific table you want to drop from the metadata
    table_name = 'usersdb'
    table_to_drop = metadata.tables.get(table_name)
    
    # Drop the table if it exists
    if table_to_drop is not None:
        table_to_drop.drop(db.engine)
  

@app.route('/')
def dash():
    return render_template('dash.html')

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        # handle request
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        session['name'] = name 
        new_user = User(name=name,email=email,password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/login')



    return render_template('register.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        
        if user and user.check_password(password):
            session['email'] = user.email
            session['name']=user.name
            
            return redirect('/index')
        else:
            return render_template('login.html',error='Invalid user')

    return render_template('login.html')


@app.route('/index')
def index():
    session.pop('meals', None)
    return render_template('index.html')


@app.route('/process_meal', methods=['GET', 'POST'])
def process_meal():
    
    if request.method == 'POST':
        meals = session.get('meals', {'breakfast': None, 'lunch': None, 'dinner': None})
        if 'breakfast' in request.form:
            breakfast= request.form.get('breakfast')
            meals['breakfast']=get_req(breakfast)
             
        elif 'lunch' in request.form:
            lunch= request.form.get('lunch')
            meals['lunch']=get_req(lunch)
             
        elif 'dinner' in request.form:
            dinner= request.form.get('dinner')
            meals['dinner']=get_req(dinner)
         
        if all(meals.values()):
            
            # Store all meals in the database
            
           
            store_meal_in_database(meals)
            # flash('Meals information stored successfully!')
            # return redirect('/process_meal')  # Redirect to another page
        session['meals']=meals    
        session.modified= True
        
        # if all(meals.values()) and 'check_nutrition' in request.form:
        #     # Store meal information in the database
        #     date = datetime.now().date()  # Get the current date
        #     # user_id = session.get('user_id')  # Assuming user_id is stored in the session

        #     new_meal = Meals(date=date, breakfast=meals['breakfast'], lunch=meals['lunch'], dinner=meals['dinner'])
        #     db.session.add(new_meal)
        #     db.session.commit()
            
        #     flash('Meals information stored successfully!')
        #     session.pop('meals', None)  # Clear the stored meals from the session

        #     return redirect('/process_meal')
        
        
        
    return render_template(
        "process_meal.html",
        bitems= meals['breakfast'],
        litems= meals['lunch'],
        ditems= meals['dinner']
        
  )
def store_meal_in_database(meals):
    # Get the current date
    date = datetime.now().date()
    email = session.get('email')
    name = session.get('name')
    
    
    user_name = name
    # Get user_id from session, assuming it's stored there
    breakfast_json = json.dumps(meals['breakfast'])
    
    lunch_json = json.dumps(meals['lunch'])
    dinner_json = json.dumps(meals['dinner'])
    
    # Store the meal in the database
    new_meal =Meals(date=date,user_name=user_name, breakfast=breakfast_json, lunch=lunch_json, dinner=dinner_json)
    db.session.add(new_meal)
    db.session.commit()
    session.pop('meals', None)
    flash('Meals information stored successfully!')   
    
@app.route('/dashboard', methods=['GET','POST'])

def dashboard():
    current_date = datetime.now().date().isoformat()
    meals= Meals.query.filter_by(date=current_date).order_by(desc(Meals.id)).first()

    bi= ast.literal_eval(meals.breakfast)
    li=ast.literal_eval(meals.lunch)
    di=ast.literal_eval(meals.dinner)
    #     # Initialize variables to store totals
    total_calories = 0
    total_calories += sum(item[1] for item in bi)
    total_calories += sum(item[1] for item in li)
    total_calories += sum(item[1] for item in di)

    
    total_fats = 0
    total_fats += sum(item[2] for item in bi)
    total_fats += sum(item[2] for item in li)
    total_fats += sum(item[2] for item in di)
        
    total_proteins = 0
    total_proteins += sum(item[3] for item in bi)
    total_proteins += sum(item[3] for item in li)
    total_proteins += sum(item[3] for item in di)
        
    total_carbs = 0
    total_carbs += sum(item[4] for item in bi)
    total_carbs += sum(item[4] for item in li)
    total_carbs += sum(item[4] for item in di)
        
    total_cholesterol = 0
    total_cholesterol += sum(item[5] for item in bi)
    total_cholesterol += sum(item[5] for item in li)
    total_cholesterol += sum(item[5] for item in di)
        
    sodium= 0
    sodium += sum(item[6] for item in bi)
    sodium += sum(item[6] for item in li)
    sodium+= sum(item[6] for item in di)
        
    potas=0
    potas += sum(item[7] for item in bi)
    potas+= sum(item[7] for item in li)
    potas += sum(item[7] for item in di)
        
    sugar = 0
    sugar += sum(item[8] for item in bi)
    sugar+= sum(item[8] for item in li)
    sugar+= sum(item[8] for item in di)
        

#     # Iterate through meal items and calculate totals
#     for meal in meals:
#         # Parse JSON data for each meal item
#         breakfast_items = json.loads(meal.breakfast)
#         lunch_items = json.loads(meal.lunch)
#         dinner_items = json.loads(meal.dinner)

#         # Calculate totals for each meal
#         total_calories += sum(item['calories'] for item in breakfast_items['items'])
#         total_proteins += sum(item['protein_g'] for item in breakfast_items['items'])
#         total_fats += sum(item['fat_total_g'] for item in breakfast_items['items'])
#         total_carbs += sum(item['carbohydrates_total_g'] for item in breakfast_items['items'])
#         total_cholesterol += sum(item['cholesterol_mg'] for item in breakfast_items['items'])

#         total_calories += sum(item['calories'] for item in lunch_items['items'])
#         total_proteins += sum(item['protein_g'] for item in lunch_items['items'])
#         total_fats += sum(item['fat_total_g'] for item in lunch_items['items'])
#         total_carbs += sum(item['carbohydrates_total_g'] for item in lunch_items['items'])
#         total_cholesterol += sum(item['cholesterol_mg'] for item in lunch_items['items'])

#         total_calories += sum(item['calories'] for item in dinner_items['items'])
#         total_proteins += sum(item['protein_g'] for item in dinner_items['items'])
#         total_fats += sum(item['fat_total_g'] for item in dinner_items['items'])
#         total_carbs += sum(item['carbohydrates_total_g'] for item in dinner_items['items'])
#         total_cholesterol += sum(item['cholesterol_mg'] for item in dinner_items['items'])

#     # Pass calculated totals to the template for rendering
    return render_template('dashboard.html', total_calories=total_calories, total_fats=total_fats,total_proteins=total_proteins,
                            total_carbs=total_carbs, total_cholesterol=total_cholesterol, total_sodium=sodium, total_potassium=potas, total_sugar=sugar)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug= True)