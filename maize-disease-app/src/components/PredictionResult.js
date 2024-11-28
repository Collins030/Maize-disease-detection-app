import React from "react";
import Recommendations from "./Recommendations";

const PredictionResult = ({ prediction, uploadedImage }) => {
  return (
    <div className="prediction-result">
      <h2>Prediction Result</h2>
      <div className="result-container">
        {/* Display Uploaded Image */}
        <div>
          <img src={uploadedImage} alt="Uploaded" className="uploaded-image" />
          <p><strong>Uploaded Image</strong></p>
        </div>

        {/* Display Prediction Info */}
        <div>
          <p><strong>Disease:</strong> {prediction.class}</p>
          <p><strong>Confidence:</strong> {(prediction.confidence * 100).toFixed(2)}%</p>
        </div>
      </div>

      {/* Recommendations Section */}
      {prediction.recommendation && (
        <Recommendations recommendation={prediction.recommendation} />
      )}
    </div>
  );
};

export default PredictionResult;
