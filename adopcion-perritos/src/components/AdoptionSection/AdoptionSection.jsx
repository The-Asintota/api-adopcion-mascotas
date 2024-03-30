import React from "react";
import './AdoptionSection.css'

const AdoptionSection = () => {
  return (
    <section className="adoption-section">
      <h2>Adopción</h2>
      <ul className="animal-list">
        <li className="animal-card">
          <img
            src="https://picsum.photos/id/237/200/300"
            alt="Imagen random de perrito"
          />
          <div>
            <h3>Tito</h3>
            <p>Edad: 10 Meses</p>
            <p>Tamaño: Pequeño</p>
            <p>Juguetón y muy cariñoso</p>
            <button>Adoptar</button>
          </div>
        </li>

        <li className="animal-card">
          <img
            src="https://picsum.photos/id/237/200/300"
            alt="Imagen random de perrito"
          />
          <div>
            <h3>Tito</h3>
            <p>Edad: 10 Meses</p>
            <p>Tamaño: Pequeño</p>
            <p>Juguetón y muy cariñoso</p>
            <button>Adoptar</button>
          </div>
        </li>

        <li className="animal-card">
          <img
            src="https://picsum.photos/id/237/200/300"
            alt="Imagen random de perrito"
          />
          <div>
            <h3>Tito</h3>
            <p>Edad: 10 Meses</p>
            <p>Tamaño: Pequeño</p>
            <p>Juguetón y muy cariñoso</p>
            <button>Adoptar</button>
          </div>
        </li>
      </ul>
    </section>
  );
};

export default AdoptionSection;
