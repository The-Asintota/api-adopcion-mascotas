import "./Header.css";
import SignIn from '../Forms/SignIn/SignIn'
import { Link } from "react-router-dom";
import { useState } from "react";

export default function Header() {
    const [showSignIn, setShowSignIn] = useState(false)

    function handleShowSignIn() {
        setShowSignIn(true)
    }
  return (
    <header className="px-8 py-6">
      <img src="/images/logo3.jpg" alt="logo sitio" />
      <nav>
        <Link to="/">Inicio</Link>
        <Link to="/shelters">Protectoras</Link>
        <Link to="/animals-for-adoption">Adopcion</Link>
        <Link to="">¿Quienes Somos?</Link>
      </nav>
      <div className="flex flex-col">
        <Link to="/shelters">
          <button className="flex items-center text-white font-bold pb-2">
            <svg
              className="h-6 w-6 text-white mr-2"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M5.121 17.804A13.937 13.937 0 0112 16c2.5 0 4.847.655 6.879 1.804M15 10a3 3 0 11-6 0 3 3 0 016 0zm6 2a9 9 0 11-18 0 9 9 0 0118 0z"
              />
            </svg>
            Registro
          </button>
        </Link>
        <button className="flex items-center text-white font-bold" onClick={handleShowSignIn}>
          <svg
            className="h-6 w-6 text-white"
            width="24"
            height="24"
            viewBox="0 0 24 24"
            strokeWidth="2"
            stroke="currentColor"
            fill="none"
            strokeLinecap="round"
            strokeLinejoin="round"
          >
            <path d="M14 8v-2a2 2 0 0 0 -2 -2h-7a2 2 0 0 0 -2 2v12a2 2 0 0 0 2 2h7a2 2 0 0 0 2 -2v-2" />
            <path d="M20 12h-13l3 -3m0 6l-3 -3" />
          </svg>
          Iniciar Sesion
        </button>
      </div>
      {showSignIn && <SignIn isActive={showSignIn} onClose={() =>setShowSignIn(false) }/>}
    </header>
  );
}
