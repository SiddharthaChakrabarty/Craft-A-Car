import google.generativeai as genai
import regex as re

API_KEY = "AIzaSyDNOtokPHTUm9WCJ1pOPaweUp_Rks9DhjI"
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')

def get_vehicle(requirements):
    prompt = f"""
    Please provide three suitable vehicle types that match the following requirements from the project directory structure:

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

    Provide the vehicle types in the following format:
    1. *VehicleType1*
    2. *VehicleType2*
    3. *VehicleType3*

    Based on the vehicle requirements provided, identify three suitable vehicle types within the structure above. Provide only the three vehicle types and nothing else.
    Requirements: {requirements}
    """
    response = model.generate_content(prompt)
    return response.text

def extract_vehicle_types(response_text):
    # Split the response text by new lines
    matches = response_text.strip().splitlines()
    return [match.strip() for match in matches[:3]]  # Extract up to three matches

def get_vehicle_specifications(vehicle_type):
    prompt = f"""
    Please provide the specifications for a vehicle of type: {vehicle_type}

    The specifications should include:
    - Seating capacity
    - Fuel type
    - Engine capacity
    - Key features
    - Cost
    """
    response = model.generate_content(prompt)
    return response.text

# Example usage
response = get_vehicle('A vehicle required to accommodate a family of 5 people.')
print(response)
vehicle_types = extract_vehicle_types(response)
print("Vehicle Types:", vehicle_types)

for vehicle_type in vehicle_types:
    specs = get_vehicle_specifications(vehicle_type)
    print(f"Specifications for {vehicle_type}:\n{specs}\n")


# def get_vehicle_specifications(vehicle_type):
#     prompt = f"""
#     Please provide the specifications for a vehicle of type: {vehicle_type}

#     The specifications should include:
#     - Seating capacity
#     - Fuel type
#     - Engine capacity
#     - Key features
#     - Cost
#     """
#     response = model.generate_content(prompt)
#     return response.text

# @app.route('/specs', methods=['GET'])
# def specs():
#     vehicle_type = request.args.get('vehicle_type')
#     if not vehicle_type:
#         return jsonify({'error': 'Vehicle type is required'}), 400

#     specs = get_vehicle_specifications(vehicle_type)
#     specs_lines = specs.split('\n')
#     specs_dict = {}
#     for line in specs_lines:
#         if ':' in line:
#             key, value = line.split(':', 1)
#             specs_dict[key.strip()] = value.strip()
    
#     response = jsonify({'vehicle_type': vehicle_type, 'specs': specs_dict})
#     return response
