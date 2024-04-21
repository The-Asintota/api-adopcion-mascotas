import { useParams } from "react-router-dom";
import { mappedAnimals } from "../../../utils/animals";
import "./AnimalProfile.css";
import { useState } from "react";
import PetRequest from "../Forms/PetRequest/PetRequest";

const AnimalProfile = () => {
  const { id } = useParams();
  const animals = mappedAnimals().filter(
    (animal) => animal.id === parseInt(id)
  );
  const { urlImage, petName, age, breed, size, description, observations } =
    animals[0];
  const [showPetRequest, setShowPetRequest] = useState(false);

  function handlePetRequest() {
    setShowPetRequest(true);
  }

  return (
    <main className="animal-main h-fit">
      <h2 className="font-extrabold text-white text-center py-0">{petName}</h2>
      <article className="animal w-screen px-10 py-2 content-start">
        <img className="animal-image" src={urlImage} alt={petName} />
        <div className="animal-info text-lg">
          <div>
            <p className="animal-parrafo">
              Tamaño: {size}
            </p>
            <p className="animal-parrafo">Raza: {breed}</p>
            <p className="animal-parrafo">Edad: {age}</p>
            <p className="animal-parrafo">Sexo: ???</p>
          </div>
          <div>Protectora</div>
          {/*           <p className="animal-parrafo">{description}</p>
          <p className="animal-parrafo">Observaciones: {observations}</p> */}
        </div>
        <button className="animal-button" onClick={handlePetRequest}>
          Adoptar
        </button>
        <PetRequest
          petName={petName}
          isActive={showPetRequest}
          onClose={() => setShowPetRequest(false)}
        />
      </article>
    </main>
  );
};

export default AnimalProfile;
