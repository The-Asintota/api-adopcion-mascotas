import "./Header.css"
import { Link } from "react-router-dom"

export default function Header() {
    return (
      <header>
        <img src="./public/images/logo3.jpg" alt="logo sitio" />
        <nav>
            <Link to="/">Inicio</Link>
            <Link to="/shelters">Protectoras</Link>
            <Link to="/animals-for-adoption">Adopcion</Link>
            <Link to="">¿Quienes Somos?</Link>
        </nav>
    </header>
    )
}