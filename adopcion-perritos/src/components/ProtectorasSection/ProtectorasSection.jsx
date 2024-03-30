import React from "react";
import './ProtectorasSection.css'

const ProtectorasSection = () => {
  return (
    <section className="protectoras-section">
      <h2>Protectoras</h2>

      <ul className="protectoras-list">
        <li className="protectora-card">
          <img
            src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTpYh91b3d-KwbMR7wSRJQSoZggr30id2dp3Q&usqp=CAU"
            alt="Protectora de animales globant"
          />
          <div>
            <h3>Globant</h3>
            <p>Animales en Adopción: 5</p>
            <p>Ubicación: Montevideo, Uruguay</p>
          </div>
        </li>

        <li className="protectora-card">
          <img
            src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTpYh91b3d-KwbMR7wSRJQSoZggr30id2dp3Q&usqp=CAU"
            alt="Protectora de animales globant"
          />
          <div>
            <h3>Globant</h3>
            <p>Animales en Adopción: 5</p>
            <p>Ubicación: Montevideo, Uruguay</p>
          </div>
        </li>

        <li className="protectora-card">
          <img
            src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTpYh91b3d-KwbMR7wSRJQSoZggr30id2dp3Q&usqp=CAU"
            alt="Protectora de animales globant"
          />
          <div>
            <h3>Globant</h3>
            <p>Animales en Adopción: 5</p>
            <p>Ubicación: Montevideo, Uruguay</p>
          </div>
        </li>
      </ul>
    </section>
  );
};

export default ProtectorasSection;
