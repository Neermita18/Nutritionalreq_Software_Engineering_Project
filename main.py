from flask import Flask, render_template, request
from meal import get_req
from waitress import serve
import requests
app= Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/process_meal', methods=['GET', 'POST'])
def process_meal():
    breaky=None
    lunchy= None
    diny= None
    if request.method == 'POST':
        if 'breakfast' in request.form:
            breakfast= request.form.get('breakfast')
    
        
            breaky=get_req(breakfast)
        elif 'lunch' in request.form:
            lunch= request.form.get('lunch')
            lunchy=get_req(lunch)
            
        elif 'dinner' in request.form:
            dinner= request.form.get('dinner')
            diny=get_req(dinner)
        
    return render_template(
        "process_meal.html",
        bitems= breaky,
        litems= lunchy,
        ditems= diny
        
  )
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)