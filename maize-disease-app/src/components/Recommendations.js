import React from "react";

const Recommendations = ({ recommendation }) => {
  const { solution, chemicals } = recommendation;

  return (
    <div className="recommendations">
      <h3>Recommended Solution</h3>
      <p>{solution}</p>

      <h3>Chemicals</h3>
      {chemicals.map((chemical, index) => (
        <div key={index} className="chemical-info">
          <p><strong>Name:</strong> {chemical.name}</p>
          <p><strong>Dosage:</strong> {chemical.dosage}</p>
          <p><strong>Procedure:</strong> {chemical.procedure}</p>
          <img
            src={chemical.image_url}
            alt={chemical.name}
            className="chemical-image"
          />
        </div>
      ))}
    </div>
  );
};

export default Recommendations;
