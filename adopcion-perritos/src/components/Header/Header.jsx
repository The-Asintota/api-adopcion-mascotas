import "./Header.css"

export default function Header() {
    return (
      <header>
        <img src="./public/images/logo3.jpg" alt="logo sitio" />
        <nav>
            <a href="/">Inicio</a>
            <a href="/shelters">Protectoras</a>
            <a href="/animals-for-adoption">Adopcion</a>
            <a href="">¿Quienes Somos?</a>
        </nav>
    </header>
    )
}