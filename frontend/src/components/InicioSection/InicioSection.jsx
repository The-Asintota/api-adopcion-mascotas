import React from "react";
import './InicioSection.css'

const InicioSection = () => {
  return (
    <section className="inicio">
      <h1>Adopta un Animalito</h1>
      <div>
        <img
          src="/images/imagen-home.jpg"
          alt="Imagen con eslogan no compres, adopta"
        />
        <p>
          En este sitio encontrarás información sobre adopción de perritos.
          Podrás ver información sobre los perritos que están en adopción y
          Ademas si eres una protectora de animales puedes publicar información
          sobre los animales que tienes en adopción. Junto a patitas, ayudanos a
          encontrar un hogar para nuestros amigos peludos 🐾.
        </p>
      </div>
    </section>
  );
};

export default InicioSection;
