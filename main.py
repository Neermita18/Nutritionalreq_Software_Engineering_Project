from flask import Flask, render_template, request, session, url_for, flash, redirect
from meal import get_req
from flask_sqlalchemy import SQLAlchemy
from waitress import serve
import requests
from forms import RegistrationForm, LoginForm  # Assuming you've created these forms
from werkzeug.security import generate_password_hash, check_password_hash

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nutrition.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.secret_key='heudbw2735snd0182bdh376ch3865271'
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    
@app.route('/')
@app.route('/index')
def index():
    session.clear()
    return render_template('index.html')
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            session['logged_in'] = True
            session['user_id'] = user.id
            flash('You have been logged in!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)
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