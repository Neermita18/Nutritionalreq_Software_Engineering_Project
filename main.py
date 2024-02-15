from flask import Flask, render_template, request
from meal import get_req
from waitress import serve
import requests
app= Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/process_meal', methods=['GET','POST'])
def process_meal():
    breakfast= request.form.get()
    food_nutrition=get_req(breakfast)
    return render_template(
        "food.html",
        items= food_nutrition
        
    )
if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)