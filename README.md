
# 🌽 Maize Disease Detection App

Welcome to the **Maize Disease Detection App**, a machine learning-powered application designed to identify diseases in maize crops. Simply upload an image of a maize leaf, and the app provides accurate predictions and actionable solutions to help farmers address crop diseases effectively.

## 🚀 Features
- **Disease Detection**: Upload an image of a maize leaf to identify common diseases.
- **Detailed Recommendations**: Get actionable solutions and recommended treatments.
- **Confidence Score**: View how confident the model is about its prediction.
- **User-Friendly**: Simple interface with API integration support.

## 📸 Supported Maize Diseases
- **Cercospora Leaf Spot / Gray Leaf Spot**
  - 🛠 Solution: Use Mancozeb or Chlorothalonil-based fungicides.
- **Common Rust**
  - 🛠 Solution: Apply Azoxystrobin or Tebuconazole fungicides.
- **Northern Leaf Blight**
  - 🛠 Solution: Use Propiconazole or Mancozeb fungicides.
- **Healthy Maize**
  - 🌱 Solution: No action needed. Your maize is healthy!

## 🛠 Tech Stack
- **Backend**: FastAPI
- **Frontend**: Compatible with web apps or tools supporting API integration
- **Machine Learning**: TensorFlow for image classification
- **Deployment**: Run locally with uvicorn

## 🛠 Installation and Setup
1. **Clone the Repository**
   ```bash
   git clone https://github.com/Collins030/Maize-disease-detection-app.git
   cd Maize-disease-detection-app
   ```

2. **Install Dependencies**
   Ensure you have Python 3.8 or above installed. Then, install the required packages:
   ```bash
   pip install fastapi uvicorn tensorflow pillow numpy
   ```

3. **Download the Model**
   Place your trained model (`maize_model.h5`) in the following directory:
   ```
   C:/Users/User/OneDrive/Documents/maize_disease_detection/model/
   ```

4. **Run the Application**
   Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

5. **Test the API**
   Visit [http://localhost:8000/docs](http://localhost:8000/docs) to interact with the API using FastAPI's interactive documentation.

## 🔗 API Endpoints
### 1. Predict Disease
- **Endpoint**: `/predict`
- **Method**: `POST`
- **Parameters**: UploadFile (image)
- **Response Example**:
  ```json
  {
    "class": "Corn_(maize)___Common_rust_",
    "confidence": 0.97,
    "recommendation": {
      "solution": "Apply fungicides containing Azoxystrobin or Tebuconazole.",
      "chemicals": [
        {
          "name": "Azoxystrobin",
          "dosage": "2ml per liter of water",
          "procedure": "Apply at disease onset and repeat every 10–14 days.",
          "image_url": "https://example.com/images/azoxystrobin.jpg"
        }
      ]
    }
  }
  ```

## 🌱 How It Works
1. Upload a clear image of a maize leaf showing symptoms (if any).
2. The machine learning model analyzes the image and predicts the disease.
3. Receive actionable solutions and recommended treatments.

## 🤝 Related Projects
Check out the **[Tomato Disease Detection App](https://github.com/Collins030/Tomato-disease-detection-app)** for identifying tomato crop diseases using a similar structure.

## 🧑‍💻 Contribution Guidelines
Contributions are welcome! Feel free to fork the repository, create a new branch, and submit a pull request.

## 📧 Contact
For any questions, suggestions, or support, reach out via the contact details in the profile.

## 🏆 Acknowledgments
Special thanks to:
- Farmers for their resilience.
- The open-source community for providing incredible tools and frameworks.

🌟 If you find this project helpful, please give it a star! 🌟

