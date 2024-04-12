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
  const isAdmin = useContext(AdminContext);

  function Controls() {
    if (!isAdmin) {
      return <button onClick={onClick}>Adoptar</button>;
    }

    if (isAdmin.user === "admin") {
      return (
        <button style={{ backgroundColor: "#DC2626" }} onClick={onClick}>
          Eliminar
        </button>
      );
    } else if (isAdmin.user === "shelter") {
      return (
        <>
          <button style={{ backgroundColor: "#DC2626" }} onClick={onClick}>
            Eliminar
          </button>
          <button style={{ backgroundColor: "#2563EB" }} onClick={onClick}>
            Editar
          </button>
        </>
      );
    }
  }

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
        <Controls />
      </div>
    </li>
  );
};

export default AdoptionCard;
