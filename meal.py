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
            # return name,calories,
            foodlist.append([name, calories, fat_total,protein,carbs_total,cholesterol])
        return foodlist
    else:
        print("Error:", response.status_code, response.text)
 


    # Pass calculated totals to the template for rendering
    
if __name__ == "__main__":
     
    print('\n Get nutritional requirements\n')
    food= input("\n Enter food")
    items= get_req(food)
  
    print("\n")
    print(items)
    for item in items:
       print(item)
  
    
    # pprint(food_nutrition)S
    
    



