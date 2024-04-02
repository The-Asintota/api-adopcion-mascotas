import React from "react";
import './AdoptionCard.css'

const AdoptionCard = ({urlImage, petName,age, breed, size, description, observations, onClick}) => {
  return (
    <li className="animal-card">
      <img
        src={urlImage}
        alt="Imagen random de perrito"
      />
      <div>
        <h3>{petName}</h3>
        <p>Edad: {age}</p>
        <p>{breed}</p>
        <p>Tamaño: {size}</p>
        <p>Juguetón y muy cariñoso{description}</p>
        <p>{observations}</p>
        <button onClick={onClick}>Adoptar</button>
      </div>
    </li>
  );
};

export default AdoptionCard;
