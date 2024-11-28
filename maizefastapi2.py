from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf

app = FastAPI()

# Allow frontend to communicate with backend
origins = [
    "http://localhost",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the trained model
MODEL = tf.keras.models.load_model("C:/Users/User/OneDrive/Documents/maize_disease_detection/model/maize_modelv1.0.h5")

# Define class names for maize diseases
CLASS_NAMES = [
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot",
    "Corn_(maize)___Common_rust_",
    "Corn_(maize)___Northern_Leaf_Blight",
    "Corn_(maize)___healthy"

]

# Provide recommendations for each disease class
RECOMMENDATIONS = {
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "solution": "Use fungicides containing Mancozeb or Chlorothalonil.",
        "chemicals": [
            {
                "name": "Mancozeb",
                "dosage": "2.5g per liter of water",
                "procedure": "Spray every 7–10 days during humid conditions.",
                "image_url": "https://example.com/images/mancozeb.jpg"
            }
        ]
    },
    "Corn_(maize)___Common_rust_": {
        "solution": "Apply fungicides containing Azoxystrobin or Tebuconazole.",
        "chemicals": [
            {
                "name": "Azoxystrobin",
                "dosage": "2ml per liter of water",
                "procedure": "Apply at disease onset and repeat every 10–14 days.",
                "image_url": "https://example.com/images/azoxystrobin.jpg"
            }
        ]
    },
    "Corn_(maize)___healthy": {
        "solution": "No action required. Maintain healthy agricultural practices.",
        "chemicals": []
    },
    "Corn_(maize)___Northern_Leaf_Blight": {
        "solution": "Use fungicides containing Propiconazole or Mancozeb.",
        "chemicals": [
            {
                "name": "Propiconazole",
                "dosage": "1ml per liter of water",
                "procedure": "Spray every 7–14 days during disease outbreak.",
                "image_url": "https://example.com/images/propiconazole.jpg"
            }
        ]
    }
}

# Helper function to read and process the uploaded image
def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image

# Prediction endpoint
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image, 0)

    # Perform prediction
    predictions = MODEL.predict(img_batch)
    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])

    # Include recommendations in the response
    recommendations = RECOMMENDATIONS[predicted_class]

    return {
        "class": predicted_class,
        "confidence": float(confidence),
        "recommendation": recommendations
    }

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)
