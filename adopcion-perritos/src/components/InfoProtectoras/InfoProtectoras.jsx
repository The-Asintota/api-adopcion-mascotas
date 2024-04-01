import React, { useState } from "react";
import SignIn from "../Forms/SignIn/SignIn";
import SignUp from "../Forms/SignUp/SignUp";
import "./InfoProtectoras.css";

const InfoProtectoras = () => {
  const [showSignIn, setShowSignIn] = useState(false)

  function handleShowSignIn() {
    setShowSignIn(true)
  }


  return (
    <section className="info-protectoras-section">
      <h2>¿Eres una asociación o protectora de animales?</h2>
      <p>
        Bienvenido a nuestra plataforma dedicada a la adopción de animales,
        donde conectamos a protectoras, asociaciones de animales y otras
        entidades colaboradoras con personas interesadas en agregar un nuevo
        miembro a su familia. Nuestro objetivo es ayudar a que los animales que
        han pasado por momentos difíciles encuentren un hogar definitivo y lleno
        de amor.
      </p>
      <p>
        Para registrarte en nuestra plataforma y publicar animales en adopción,
        es necesario que tu asociación esté legalmente constituida como
        protectora de animales.
      </p>
      <p>El proceso para unirse a nuestra plataforma es muy sencillo:</p>
      <ol className="list-decimal pl-12">
        <li>
          Regístrate haciendo clic en el enlace de "Registro", donde deberás
          ingresar la dirección de correo electrónico de tu asociación
          protectora de animales y una contraseña.
        </li>
        <li>
          Una vez registrado, podrás comenzar a publicar en la web de inmediato.
        </li>
      </ol>
      <p>
        Si estás interesado en adoptar un animal que has visto en nuestra
        plataforma, simplemente sigue estos pasos:
      </p>
      <ol className="list-decimal pl-12">
        <li>
          Haz clic en el botón “Quiero adoptarlo” en el anuncio del animal que
          te interese.
        </li>
        <li>
          Rellena el formulario con tus datos y un mensaje para la protectora
          que publicó al animal.
        </li>
      </ol>

      <p>
        Estamos aquí para ayudarte en tu proceso de adopción y para facilitar la
        conexión entre los animales que necesitan un hogar y las personas que
        desean brindarles uno. ¡Gracias por unirte a nuestra comunidad de
        amantes de los animales!
      </p>
      <div className="flex items-center justify-center">
        <SignUp onClick={handleShowSignIn}/>
      </div>
      <SignIn isActive={showSignIn} onClose={() => setShowSignIn(false)}/>
    </section>
  );
};

export default InfoProtectoras;
