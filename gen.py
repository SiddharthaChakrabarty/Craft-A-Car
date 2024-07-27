import google.generativeai as genai
import regex as re
import os
import random

API_KEY = "AIzaSyDNOtokPHTUm9WCJ1pOPaweUp_Rks9DhjI"
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')

def get_vehicle(requirements):
    prompt = f"""
    Please provide the paths of three suitable subdirectories that match the vehicle requirements from the following project directory structure:

    Cars Dataset
    ├── Bus
    ├── Cars
    │   ├── Compact
    │   │   ├── Mini
    │   │   └── Regular
    │   ├── Minivan
    │   ├── Sedan
    │   │   ├── Compact
    │   │   ├── Luxurious
    │   │   ├── Services
    │   │   │   ├── Police
    │   │   │   ├── Taxi
    │   │   └── Standard
    │   ├── Sportscar
    │   ├── Supercar
    │   ├── SUV
    │   │   ├── Hybrid
    │   │   ├── Jeep
    │   │   ├── Pickup
    │   │   ├── Services
    │   │   │   ├── Ambulance
    │   │   │   ├── Police
    │   │   │   └── Taxi
    │   │   └── Standard
    ├── Tactical
    ├── Truck
    │   ├── Goods
    │   ├── Pickup
    │   ├── Services
    │   │   ├── Ambulance
    │   │   ├── Carrier
    │   │   ├── Fire
    │   │   ├── Police
    │   │   └── Tanker

    Provide the paths in the following format:
    1. **Path1**
    2. **Path2**
    3. **Path3**

    Based on the vehicle requirements provided, identify three suitable subdirectories within the structure above. 
    Requirements: {requirements}
    """
    response = model.generate_content(prompt)
    return response.text
    
import re

def extract_paths(response_text):
    matches = re.findall(r'\*\*(.+?)\*\*', response_text)
    return [match.strip() for match in matches[:3]]  # Extract up to three matches

# Example usage
response = get_vehicle('A vehicle required to accommodate a family of 5 people.')
paths = extract_paths(response)
print(paths)
