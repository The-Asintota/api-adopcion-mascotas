import "./Header.css";
import SignIn from "../Forms/SignIn/SignIn";
import { Link } from "react-router-dom";
import { useState } from "react";

export default function Header() {
  const [showSignIn, setShowSignIn] = useState(false);

  function handleShowSignIn() {
    setShowSignIn(true);
  }
<<<<<<< HEAD
  function handleShowSignIn() {
    setShowSignIn(true);
  }
=======

>>>>>>> feature/update-shelter-profile
  return (
    <header className="px-8 py-6 text-xs md:text-base">
      <img src="/images/logo3.jpg" alt="logo sitio" className="w-28 md:w-32" />
      <nav>
        <Link to="/">Inicio</Link>
        <Link to="/shelters">Protectoras</Link>
        <Link to="/animals-for-adoption">Adopcion</Link>
        <Link to="">¿Quienes Somos?</Link>
      </nav>
      <div className="flex flex-row">
        <button
          className="flex items-center text-white font-bold pr-4"
          onClick={handleShowSignIn}
        >
          Acceder
        </button>
        <Link to="/shelters">
          <button className="flex items-center text-white font-bold bg-[#118A95] hover:bg-[#3bdbe9 py-2 px-4 rounded-md shadow-lg text-white font-semibold transition duration-200">
            Registrarse
          </button>
        </Link>
      </div>
      {showSignIn && (
        <SignIn isActive={showSignIn} onClose={() => setShowSignIn(false)} />
      )}
    </header>
  );
}
