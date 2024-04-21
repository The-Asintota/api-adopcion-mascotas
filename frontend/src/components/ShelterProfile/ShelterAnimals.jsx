import React, { useEffect, useState } from "react";
import AdoptionCard from "../AdoptionSection/AdoptionCard";
import petData from '../../petData.json'

const ShelterAnimals = () => {
/*     const [animals, setAnimals] = useState([])

    const token = localStorage.getItem('token')

    useEffect(()=> {

    },[])
 */
  return (
    <div className="mt-4 pt-2 px-3">
      <ul className="grid grid-cols-3 gap-5">
        {petData.perros.map((pet) => (
          <AdoptionCard
            key={pet.id}
            urlImage={pet.imagen}
            petName={pet.nombre}
            age={pet.edad}
            breed={pet.raza}
          />
        ))}
      </ul>
    </div>
  );
};

export default ShelterAnimals;

