# Craft-A-Car--An-AI-Enabled-3D-Model-Generator-with-VR-incorporated
## Overview
The core idea of this project strives to align the customer experience with the automotive industry, providing with new models that fit the demands and preferences of the customer. The primary goal is to offer a number of options personalised to each customer's specific needs.
![WhatsApp Image 2024-07-27 at 18 37 13_37e1bb17](https://github.com/user-attachments/assets/a5b49429-71f6-4db3-8333-e87bbe2e7102)
![WhatsApp Image 2024-07-27 at 18 37 13_fe9536d6](https://github.com/user-attachments/assets/0a710333-8b67-496a-b9b1-6ed71102db5b)
![WhatsApp Image 2024-07-27 at 18 37 14_8e4be58a](https://github.com/user-attachments/assets/b263a27e-8afa-4c01-8d1a-0268e5876d22)


  ## Getting Started
  To get started with Craft-A-Car, follow these steps:

  1. **Clone the repository**:
   ```bash
   git clone https://github.com/SiddharthaChakrabarty/Craft-A-Car.git
  ```

  2. **Navigate to the project directory**:
    ```bash
     cd Craft-A-Car
   ```
  3. **Install backend dependencies**:
   ```bash
   python3 -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS and Linux
   source venv/bin/activate
   pip install flask, flask-cors, google-generativeai, regex

  4. **Run the backend server (runs on port 5000 by default)**:
   ```bash
   python app.py

  5. **Install frontend dependencies**:
   ```bash
   npm install

  6. **Run the frontend server (runs on port 5173 by default)**:
   ```bash
   npm run dev

  7. **Open your web browser and navigate to `http://localhost:5173`**:

  ## Usage
  1.**Personalized Recommendations**:
    Tailors vehicle suggestions based on customer preferences.

  2.**Enhanced Customer Experience**:
    Provides detailed specifications and choices, aiding informed decisions.

  3.**Efficient Visualization**:
    Uses Blender and Three.js for high-quality 3D model viewing.

  4.**Immersive VR Showrooms**:
    Employs Unreal Engine and VR plugins for an interactive experience.

  ## Features
  1.**Advanced Lexical Analysis**: Utilises Gemini API for accurate interpretation and analysis of customer prompt.

  2.**Dynamic Recommendation System**: Adapts according to user preferences which allow further refinement of model generation.

  3.**Detailed Specifications View**: Provides customers with the option to view the internal and external specs of the model as well as its current market price for informed decision-making.

  4.**High-Quality Rendering**: The use of Three.js to render GLB models allows not only realistic visualisation but also maximum optimisation for the models generated.

  ## Components
  1.**Generative AI** - Gemini API is used to perform a descriptive analysis of the customer prompts. This analysis helps in generating various accurate suggestions based on the customer's needs.

  2.**Flask** - Various endpoints are created using Flask in order to make API calls and then  render the models and their specifications onto the frontend.

  3.**Blender** - It is used to initially view and process the vehicle models.

  4.**Three.js** - It is employed to render the models and initialise a scene that defines the viewpoint using a perspective camera.Directional and ambient lighting are used to give depth to the models. GLTFLoader is used to render the GLB models onto the screen. A showroom floor is created using PlaneGeometry and MeshStandardMaterial.
  
  5.**Unreal Engine** - For providing an immersive showroom layout, VR plugins such as SteamVR and OculusVR are used that allows the user to explore the models thoroughly.

