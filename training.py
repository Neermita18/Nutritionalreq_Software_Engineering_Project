import numpy as np
import pandas as pd
import requests

# URL of the DRI Calculator page
url = 'https://www.nal.usda.gov/human-nutrition-and-food-safety/dri-calculator'

# User information (replace with actual user data)
user_info = {
    'Weight': '70',    # in kg
    'Height': '170',   # in cm
    'Age': '30',       # in years
    'Sex': 'male'
}

# Send a POST request with user information
response = requests.post(url, data=user_info)

# Check if the request was successful
if response.status_code == 200:
    # Process and display the response
    print(response.text)
else:
    print("Failed to retrieve DRI values.")