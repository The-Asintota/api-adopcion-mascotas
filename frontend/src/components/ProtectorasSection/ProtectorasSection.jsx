import React from "react";
import './ProtectorasSection.css'
import ProtectoraCard from "./ProtectoraCard";
import { shelters } from "../../shelterData.json";

const ProtectorasSection = () => {
  return (
    <section className="protectoras-section">
      <h2>Protectoras</h2>

      <ul className="protectoras-list">
        {shelters.map((shelter) => (
          <ProtectoraCard
            key={shelter.id}
            name={shelter.name}
            animals={shelter.animalsCount}
            location={shelter.location}
          />
        ))}
      </ul>
    </section>
  );
};

export default ProtectorasSection;
