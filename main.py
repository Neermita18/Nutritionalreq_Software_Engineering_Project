from flask import Flask, render_template, request, session, url_for, flash, redirect
from meal import get_req
from flask_sqlalchemy import SQLAlchemy
from waitress import serve
import requests
from forms import RegistrationForm, LoginForm  # Assuming you've created these forms
from werkzeug.security import generate_password_hash, check_password_hash

app= Flask(__name__)

app.secret_key='heudbw2735snd0182bdh376ch3865271'

    
@app.route('/')
@app.route('/index')
def index():
    session.clear()
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
        session['meals']=meals    
        session.modified= True
        
    return render_template(
        "process_meal.html",
        bitems= meals['breakfast'],
        litems= meals['lunch'],
        ditems= meals['dinner']
        
  )
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug= True)