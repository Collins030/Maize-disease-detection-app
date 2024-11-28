import React, { useState } from "react";
import { predictImage } from "../api";

const ImageUploader = ({ onUpload }) => {
  const [selectedImage, setSelectedImage] = useState(null);

  const resizeImage = (file, targetWidth, targetHeight) => {
    return new Promise((resolve) => {
      const img = new Image();
      const reader = new FileReader();

      reader.onload = (e) => {
        img.src = e.target.result;
      };

      img.onload = () => {
        const canvas = document.createElement("canvas");
        const ctx = canvas.getContext("2d");

        let width = img.width;
        let height = img.height;

        // If the image is smaller, scale it up to 256x256
        if (width < targetWidth || height < targetHeight) {
          width = targetWidth;
          height = targetHeight;
        } else {
          // Maintain aspect ratio for larger images
          if (width > height) {
            if (width > targetWidth) {
              height = (height * targetWidth) / width;
              width = targetWidth;
            }
          } else {
            if (height > targetHeight) {
              width = (width * targetHeight) / height;
              height = targetHeight;
            }
          }
        }

        canvas.width = width;
        canvas.height = height;

        ctx.drawImage(img, 0, 0, width, height);

        canvas.toBlob((blob) => {
          resolve(blob);
        }, "image/jpeg", 0.8); // Adjust the quality as needed
      };

      reader.readAsDataURL(file);
    });
  };

  const handleImageChange = (event) => {
    setSelectedImage(event.target.files[0]);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (selectedImage) {
      // Resize the image before sending it to the backend
      const resizedImage = await resizeImage(selectedImage, 256, 256); // Resizes to 256x256 if smaller
      const prediction = await predictImage(resizedImage);
      onUpload(URL.createObjectURL(resizedImage), prediction);
    }
  };

  return (
    <div className="image-uploader">
      <form onSubmit={handleSubmit}>
        <input type="file" accept="image/*" onChange={handleImageChange} />
        <button type="submit">Upload and Predict</button>
      </form>
    </div>
  );
};

export default ImageUploader;
