import React, { useState } from "react";
import ImageUploader from "./components/ImageUploader";
import PredictionResult from "./components/PredictionResult";
import "./App.css";

function App() {
  const [prediction, setPrediction] = useState(null);
  const [uploadedImage, setUploadedImage] = useState(null);

  const handleImageUpload = (image, predictionData) => {
    setUploadedImage(image);
    setPrediction(predictionData);
  };

  return (
    <div className="App">
      <h1>maize Disease Detection</h1>
      <ImageUploader onUpload={handleImageUpload} />
      {prediction && (
        <PredictionResult
          prediction={prediction}
          uploadedImage={uploadedImage}
        />
      )}
    </div>
  );
}

export default App;
