import { useState } from "react";
import { mappedAnimals } from "../../utils/animals";

export default function useSearch() {
    const [animals, setAnimals] = useState(mappedAnimals());

    const handleSearch = (e) => {
        e.preventDefault();
        const data = new FormData(e.target);
        const animal = {
            nombre : data.get("nombre"),
            tipo : data.get("tipo"),
            tamaño : data.get("tamaño"),
            edad : data.get("edad")
        }
        const mockData = mappedAnimals()

        const filteredAnimals = mockData.filter((item) => {
            let result = true;

            if(animal.nombre !== "") {
                if(!item.petName.toLowerCase().includes(animal.nombre.toLowerCase())) {
                    result = false; 
                }
            }

            if(animal.tipo !== "Tipo") {
                if(item.type !== animal.tipo) {
                    result = false
                }
            }

            if(animal.tamaño !== "Tamaño") {
                if(item.size !== animal.tamaño) {
                    result = false
                }
            }
            
            if(animal.edad !== "Edad") {
                if(item.age !== animal.edad) {
                    result = false
                }
            }
            
            return result

        })

        setAnimals(filteredAnimals)
    }

    return { animals, handleSearch }
}