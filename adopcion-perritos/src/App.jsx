import './App.css'
import Footer from './Footer'
import Header from './Header'

function App() {

  return (
    <>
      <Header />
      
      <main>
        <section className='inicio'>
          <h1>Adopta un Animalito</h1>
          <div>
            <img src="./public/images/imagen-home.jpg" alt="Imagen con eslogan no compres, adopta" />
            <p>
              En este sitio encontrarás información sobre adopción de perritos.
              Podrás ver información sobre los perritos que están en adopción y
              Ademas si eres una protectora de animales
              puedes publicar información sobre los animales que tienes en adopción.
              Junto a patitas, ayudanos a encontrar un hogar para nuestros amigos peludos 🐾.
            </p>
          </div>
        </section>

        <section className='adoption-section'>
          <h2>Adopción</h2>
          <ul className='animal-list'>
            <li className='animal-card'>
              <img src="https://picsum.photos/id/237/200/300" alt="Imagen random de perrito" />
              <div>
                <h3>Tito</h3>
                <p>Edad: 10 Meses</p>
                <p>Tamaño: Pequeño</p>
                <p>Juguetón y muy cariñoso</p>
                <button>Adoptar</button>
              </div>
            </li>

            <li className='animal-card'>
              <img src="https://picsum.photos/id/237/200/300" alt="Imagen random de perrito" />
              <div>
                <h3>Tito</h3>
                <p>Edad: 10 Meses</p>
                <p>Tamaño: Pequeño</p>
                <p>Juguetón y muy cariñoso</p>
                <button>Adoptar</button>
              </div>
            </li>

            <li className='animal-card'>
              <img src="https://picsum.photos/id/237/200/300" alt="Imagen random de perrito" />
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
      </main>

      <section className='protectoras-section'>
          <h2>Protectoras</h2>

          <ul className='protectoras-list'>
            <li className='protectora-card'>
              <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTpYh91b3d-KwbMR7wSRJQSoZggr30id2dp3Q&usqp=CAU" alt="Protectora de animales globant" />
              <div>
                <h3>Globant</h3>
                <p>Animales en Adopción: 5</p>
                <p>Ubicación: Montevideo, Uruguay</p>
              </div>
            </li>

            <li className='protectora-card'>
              <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTpYh91b3d-KwbMR7wSRJQSoZggr30id2dp3Q&usqp=CAU" alt="Protectora de animales globant" />
              <div>
                <h3>Globant</h3>
                <p>Animales en Adopción: 5</p>
                <p>Ubicación: Montevideo, Uruguay</p>
              </div>
            </li>

            <li className='protectora-card'>
              <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTpYh91b3d-KwbMR7wSRJQSoZggr30id2dp3Q&usqp=CAU" alt="Protectora de animales globant" />
              <div>
                <h3>Globant</h3>
                <p>Animales en Adopción: 5</p>
                <p>Ubicación: Montevideo, Uruguay</p>
              </div>
            </li>
          </ul>
      </section>
      
      <section className='about-section'>
          <h2>¿Quiénes Somos?</h2>
          <p>Somos un sitio web
            que busca ayudar a los perritos a encontrar un hogar.
            Si tienes una protectora de animales y quieres.
          </p>
      </section>
    
      <Footer />
    </>
  )
}

export default App
