import React from "react";
import UploadAnimal from "./Forms/UploadAnimal/UploadAnimal";

const ShelterProfile = () => {
  return (
    <div className="flex flex-row">
      <UploadAnimal/>
      <p>Mis mascotas (aca deben ir la lista de mascotas)</p>
    </div>
  );
};

export default ShelterProfile;
