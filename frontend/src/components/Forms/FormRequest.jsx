import React from "react";
import axios from "axios";

const FormRequest = ({ endpoint, formData, onSuccess, textButton }) => {
  const urlRequest = `${import.meta.env.VITE_BACKEND_URL}${endpoint}`;

  const handleRequest = async () => {
    setLoading(true);
    axios
      .post(urlRequest, formData, {
        headers: { "Content-Type": "application/json" },
      })
      .then((response) => {
        console.log(response.data);
        if (response.status === 201) {
          onSuccess();
        } else if (response.status === 400) {
          console.log(response.data.detail);
        } else if (response.status === 401) {
          console.log(response.data.detail);
        } else if (response.status === 500) {
          console.log(response.data.detail);
        } else {
          console.log(response.data.error);
        }
      })
      .catch((error) => console.log(error));
  };

  return (
    <button
      className="w-full py-2 px-4 bg-[#118A95] hover:bg-[#3bdbe9] rounded-md shadow-lg text-white font-semibold transition duration-200"
      onClick={handleRequest}
    >
      {textButton}
    </button>
  );
};

export default FormRequest;
