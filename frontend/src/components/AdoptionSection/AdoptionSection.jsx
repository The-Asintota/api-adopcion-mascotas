import React, { useState } from "react";
import PetRequest from "../Forms/PetRequest/PetRequest";
import AdoptionCard from "./AdoptionCard";
import './AdoptionSection.css'
import useSearch from "../../hooks/useSearch";
import SearchAnimal from "../SearchAnimal/SearchAnimal";

const AdoptionSection = () => {
  const [showPetRequest, setShowPetRequest] = useState(false)
  const { animals, handleSearch } = useSearch()
  function handlePetRequest() {
    setShowPetRequest(true)
  }
  
  return (
    <section className="adoption-section">
      <h2>Adopción</h2>
      <SearchAnimal onChange={handleSearch} />
      <ul className="animal-list">
        {animals.map(({ id, urlImage, petName, age, bread, size, description, observations }) => (
          <AdoptionCard 
            key={id}
            onClick={handlePetRequest}
            urlImage={urlImage}
            petName={petName}
            age={age}
            breed={bread}
            size={size}
            description={description}
            observations={observations}
          />
        )) }

      </ul>

      <PetRequest isActive={showPetRequest} onClose={() => setShowPetRequest(false)}/>
    </section>
  );
};

export default AdoptionSection;
