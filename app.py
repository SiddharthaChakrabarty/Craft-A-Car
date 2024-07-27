import google.generativeai as genai
import regex as re
import os
import random
from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()



API_KEY = os.getenv("API_KEY")
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')

app = Flask(__name__)
CORS(app)

def get_vehicle(requirements):
    prompt = f"""
    Please provide the paths of three suitable subdirectories that match the vehicle requirements from the following project directory structure:

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
    matches = re.findall(r'\*\*(.+?)\*\*', response.text)
    
    if matches:
        return [match.strip() for match in matches]
    else:
        return "No suitable subdirectories found"

@app.route('/get_vehicle', methods=['POST'])
def vehicle_endpoint():
    user_requirements = request.json.get("requirements")
    selected_paths = get_vehicle(user_requirements)

    final_paths = []
    
    for path in selected_paths:
        dir_path = os.path.join("Cars Dataset", path.replace("/", os.sep))
        
        if os.path.isdir(dir_path):
            files = [f for f in os.listdir(dir_path) if f.endswith('.glb')]
            if files:
                selected_files = random.sample(files, min(len(files), 5))
                final_paths.append({
                "path": dir_path,
                "models": [os.path.join(dir_path, selected_file) for selected_file in selected_files]
                })
                print(final_paths)
                    
            else:
                return jsonify({"error": f"No .glb files found in the directory: {dir_path}"}), 404
        else:
            return jsonify({"error": f"Directory does not exist: {dir_path}"}), 404

    return jsonify({"selected_files": final_paths})


@app.route('/get_vehicle_specs', methods=['POST'])
def vehicle_specs_endpoint():
    vehicle_type = request.json.get("vehicle_type")
    print(vehicle_type)
    
    if not vehicle_type:
        return jsonify({"error": "Vehicle type is required"}), 400

    prompt = f"""
    Provide detailed specifications for the following vehicle type:
    
    Vehicle Type: {vehicle_type}
    """
    
    response = model.generate_content(prompt)
    specifications = response.text.strip()
    specifications = specifications.replace('*',"")
    specifications = specifications.replace('#',"")
    specifications = specifications.split(sep='\n')
    # specifications = specifications.replace(',')
    
    if specifications:
        return jsonify({"specifications": specifications})
    else:
        return jsonify({"error": "Specifications not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
