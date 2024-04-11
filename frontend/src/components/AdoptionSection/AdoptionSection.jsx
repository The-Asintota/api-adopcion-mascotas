import React from "react";
import AdoptionCard from "./AdoptionCard";
import './AdoptionSection.css'
import useSearch from "../../hooks/useSearch";
import SearchAnimal from "../SearchAnimal/SearchAnimal";

const AdoptionSection = () => {
  const { animals, handleSearch } = useSearch()

  function handlePetRequest({ id = 1 }) {
    window.location.href = `/animal/${id}`
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
          />
        )) }

      </ul>

    </section>
  );
};

export default AdoptionSection;
