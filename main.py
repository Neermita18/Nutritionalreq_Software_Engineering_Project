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
    breakfast= request.form.get('breakfast')
    # lunch= request.form.get('lunch')
    # dinner= request.form.get('dinner')
    breaky=get_req(breakfast)
    # lunchy=get_req(lunch)
    # diny=get_req(dinner)
    return render_template(
        "process_meal.html",
        bitems= breaky,
        # litems= lunchy,
        # ditems= diny
        
  )
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)