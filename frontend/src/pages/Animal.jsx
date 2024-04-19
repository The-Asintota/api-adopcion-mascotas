import { useParams } from "react-router-dom";
import { mappedAnimals } from "../../utils/animals";
import './Animal.css';
import { useState } from "react";
import PetRequest from "../components/Forms/PetRequest/PetRequest";

const Animal = () => {
    const { id } = useParams();
    const animals = mappedAnimals().filter(animal => animal.id === parseInt(id));
    const { urlImage, petName, age, breed, size, description, observations } = animals[0];
    const [showPetRequest, setShowPetRequest] = useState(false)
    
    function handlePetRequest() {
        setShowPetRequest(true)
    }

    return (
        <main className="animal-main">
            <article className="animal">
                <img className="animal-image" src={urlImage} alt={petName} />
                <div className="animal-info">
                    <h2>{petName}</h2>
                    <p className="animal-parrafo">{description}</p>
                    <p className="animal-parrafo">Edad: {age}</p>
                    <p className="animal-parrafo">Raza: {breed}</p>
                    <p className="animal-parrafo">Tamaño: {size}</p>
                    <p className="animal-parrafo">Observaciones: {observations}</p>
                    <button className="animal-button" onClick={handlePetRequest}>Adoptar</button>
                </div>
        
              <PetRequest isActive={showPetRequest} onClose={() => setShowPetRequest(false)}/>

            </article>
        </main>
    )
}

export default Animal;
