from dotenv import load_dotenv 
from pprint import pprint
import requests
import os

import json
from datetime import datetime
load_dotenv()
def get_req(food):
    url = f'https://api.calorieninjas.com/v1/nutrition?query='
    response = requests.get(url + food, headers={'X-Api-Key': os.getenv('API_KEY')})
    foodlist=[]
    if response.status_code == requests.codes.ok:
        r= response.text
        print(type(r))
       # from main import Meals
        current_date= datetime.now().date().isoformat()
        print(current_date)
        
        JSON= json.loads(r)
        print(JSON)
        for item in JSON["items"]:
            print(item["name"], item['calories'])
        
            
        
    # Extracting individual nutrient values
            name = item["name"]
            calories = item["calories"]
            fat_total = item["fat_total_g"]
            protein= item["protein_g"]
            carbs_total = item["carbohydrates_total_g"]
            cholesterol= item["cholesterol_mg"]
            sodium= item["sodium_mg"]
            potassium= item["potassium_mg"]
            sugar= item["sugar_g"]
            # return name,calories,
            foodlist.append([name, calories, fat_total,protein,carbs_total,cholesterol, sodium, potassium, sugar])
        return foodlist
    else:
        print("Error:", response.status_code, response.text)
def calories():
    url = "https://fitness-calculator.p.rapidapi.com/dailycalorie"

    querystring = {"age":"20","gender":"female","height":"158","weight":"53","activitylevel":"level_1"}

    headers = {
	"X-RapidAPI-Key": "8bc4c7e788msh805f2fd04062842p14cac2jsnca0ad7e47526",
	"X-RapidAPI-Host": "fitness-calculator.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    print(response.json())


    # Pass calculated totals to the template for rendering
    
if __name__ == "__main__":
     
    # print('\n Get nutritional requirements\n')
    # food= input("\n Enter food")
    # items= get_req(food)
  
    # print("\n")
    # print(items)
    # for item in items:
    #    print(item)
    calories()
    
    # pprint(food_nutrition)S
    
    



