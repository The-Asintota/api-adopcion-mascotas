import "./Header.css";
import { Link } from "react-router-dom";

export default function Header() {
  return (
    <header className="px-8 py-6">
      <img src="/images/logo3.jpg" alt="logo sitio" />
      <nav>
        <Link to="/">Inicio</Link>
        <Link to="/shelters">Protectoras</Link>
        <Link to="/animals-for-adoption">Adopcion</Link>
        <Link to="">¿Quienes Somos?</Link>
      </nav>
      <div className="flex items-center">
        <Link to='/shelters'>
            <button className="flex items-center text-white font-bold">
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
            Acceso
            </button>
        </Link>
      </div>
    </header>
  );
}
