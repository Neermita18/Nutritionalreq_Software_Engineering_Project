from dotenv import load_dotenv 
from pprint import pprint
import requests
import os

load_dotenv()
def get_req(food1= "egg"):
    url = f'https://api.nal.usda.gov/fdc/v1/foods/search?api_key={os.getenv("API_KEY")}&query={food1}'
    r = requests.get(url)
    print(r.status_code)  # 200
    return r.json
if __name__ == "__main__":
    print('\n Get nutritional requirements\n')
    food= input("\n Enter food")
    food_nutrition= get_req(food)
    
    print("\n")
    pprint(food_nutrition)