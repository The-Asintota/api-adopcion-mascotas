import React from "react";
import AdoptionCard from "../AdoptionSection/AdoptionCard";
import useAnimals from "../../hooks/useAnimals";

const ShelterAnimals = () => {
  const { animals } = useAnimals();

  return (
    <div className="mt-4 pt-2 px-3">
      <ul className="grid grid-cols-3 gap-5">
        {animals.map(({ id, urlImage, petName, age, breed }) => (
          <AdoptionCard
            key={id}
            urlImage={urlImage}
            petName={petName}
            age={age}
            breed={breed}
          />
        ))}
      </ul>
    </div>
  );
};

export default ShelterAnimals;

