import React, { useContext } from "react";
import "./AdoptionCard.css";
import { AdminContext } from "../../context/admin";

const AdoptionCard = ({
  urlImage,
  petName,
  age,
  breed,
  size,
  description,
  observations,
  onClick,
}) => {

  return (
    <li className="animal-card">
      <img src={urlImage} alt="Imagen random de perrito" />
      
      <div className="flex flex-col">
        <p className="text-center text-xl font-semibold py-0">{petName}</p>
        <div className="flex flex-row w-full justify-around items-center">
          <p>Edad: {age}</p>
          <p>{breed}</p>
          {size && <p>Tamaño: {description}</p>}
          {description && <p>{description}</p>}
          {observations && <p>{observations}</p>}
        </div>
        <button onClick={onClick}>Adoptar</button>
      </div>
    </li>
  );
};

export default AdoptionCard;
