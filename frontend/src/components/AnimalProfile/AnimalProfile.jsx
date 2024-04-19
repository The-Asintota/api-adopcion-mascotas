import { useParams } from "react-router-dom";
import { mappedAnimals } from "../../../utils/animals";
import "./AnimalProfile.css";
import { useState } from "react";
import PetRequest from "../Forms/PetRequest/PetRequest";
import paw from "../../assets/paw.svg";
import sexIcon from "../../assets/sexIcon.svg";
import ageIcon from "../../assets/ageIcon.svg";
import sizeIcon from "../../assets/sizeIcon.svg";

const AnimalProfile = () => {
  const { id } = useParams();
  const animals = mappedAnimals().filter(
    (animal) => animal.id === parseInt(id)
  );
  const {
    urlImage,
    petName,
    age,
    breed,
    sex,
    size,
    description,
    observations,
  } = animals[0];
  const [showPetRequest, setShowPetRequest] = useState(false);

  function handlePetRequest() {
    setShowPetRequest(true);
  }

  return (
    <main className="animal-main h-fit">
      <h2 className="font-extrabold text-white text-center py-3">{petName}</h2>

      <div className="flex flex-row m-8 px-4">
        <img
          src={urlImage}
          alt={petName}
          className="w-96 rounded-2xl shadow-2xl"
        />
        <div className="flex flex-col justify-start text-white">
          <div className="ml-8 flex flex-row text-white text-xl">
            <p className="relative mb-4 flex">
              <img src={paw} alt="paw" className="w-6 h-6 mr-2" />
              Raza: {breed}
            </p>
            <p className="relative mb-4 flex">
              <img src={ageIcon} alt="ageIcon" className="w-6 h-6 mr-2" />
              Edad: {age}
            </p>

          </div>
          <div className="ml-8 flex flex-row text-white text-xl">

            <p className="relative mb-4 flex">
              <img src={sexIcon} alt="sexIcon" className="w-6 h-6 mr-2" />
              Sexo: {sex}
            </p>
            <p className="relative mb-4 flex">
              <img src={sizeIcon} alt="sizeIcon" className="w-6 h-6 mr-2" />
              Tamaño: {size}
            </p>
          </div>
          <div>
            <p className="ml-8 text-white text-xl">
              Descripcion: {description}
            </p>
            <p className="ml-8 text-white text-xl">
              Observaciones: {observations}
            </p>
            <button className="animal-button ml-11" onClick={handlePetRequest}>
              Adoptar
            </button>
            <PetRequest
              petName={petName}
              isActive={showPetRequest}
              onClose={() => setShowPetRequest(false)}
            />
          </div>
        </div>
      </div>
    </main>
  );
};

export default AnimalProfile;
