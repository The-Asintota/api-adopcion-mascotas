import React from "react";
import UploadAnimal from "../Forms/UploadAnimal/UploadAnimal";
import ShelterAnimals from "./ShelterAnimals";
import LogOut from "../LogOut";

const ShelterProfile = () => {
  return (
    <div className="flex flex-row">
      <UploadAnimal />
      <ShelterAnimals />
      <LogOut/>
    </div>
  );
};

export default ShelterProfile;
