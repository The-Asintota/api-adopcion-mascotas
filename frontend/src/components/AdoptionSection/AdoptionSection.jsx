import React, { useState } from "react";
import PetRequest from "../Forms/PetRequest/PetRequest";
import AdoptionCard from "./AdoptionCard";
import './AdoptionSection.css'

const AdoptionSection = () => {
  const [showPetRequest, setShowPetRequest] = useState(false)

  function handlePetRequest() {
    setShowPetRequest(true)
  }

  return (
    <section className="adoption-section">
      <h2>Adopción</h2>
      <ul className="animal-list">
        <AdoptionCard 
        onClick={handlePetRequest}
        urlImage="https://images.unsplash.com/photo-1541364983171-a8ba01e95cfc?q=80&w=3387&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
        petName="Tito"
        age="10 Meses"
        breed="De la vida"
        size="Pequeño"
        description="Juguetón y muy cariñoso"
        observations="Vacunas al dia"
        />
      </ul>

      <PetRequest isActive={showPetRequest} onClose={() => setShowPetRequest(false)}/>
    </section>
  );
};

export default AdoptionSection;
