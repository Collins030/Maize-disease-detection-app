import axios from 'axios';

const API_URL = "http://localhost:8000";

export const predictImage = async (image) => {
  const formData = new FormData();
  formData.append("file", image);

  const response = await axios.post(`${API_URL}/predict`, formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });

  return response.data;
};
