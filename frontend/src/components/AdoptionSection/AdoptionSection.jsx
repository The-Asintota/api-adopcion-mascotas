import React from "react";
import AdoptionCard from "./AdoptionCard";
import './AdoptionSection.css'
import SearchAnimal from "../SearchAnimal/SearchAnimal";
import useAnimals from "../../hooks/useAnimals";

const AdoptionSection = () => {
  const { animals } = useAnimals()

  function handlePetRequest({ id }) {
    window.location.href = `/animal/${id}`
  }
  
  return (
    <section className="adoption-section w-sceen">
      <h2>Adopción</h2>
      <SearchAnimal />
      <ul className="animal-list">
        {animals && animals.map(({ id, urlImage, petName, age, bread, size, description, observations }) => (
          <AdoptionCard 
            key={id}
            onClick={() => handlePetRequest({ id })}
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
