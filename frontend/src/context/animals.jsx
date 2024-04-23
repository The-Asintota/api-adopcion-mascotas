import { createContext, useEffect, useRef, useState } from "react";
import { mappedAnimals } from "../../utils/animals";

export const AnimalsContext = createContext()

export const AnimalsProvider = ({ children }) => {
    const [animals, setAnimals] = useState([]);
    const [filters, setFilters] = useState({
        nombre: "",
        tipo: "",
        tamaño: "",
        edad: ""
    })

    const [filterAnimals, setFilterAnimals] = useState([]);

    useEffect(() => {
        fetchAnimals().then(res => {
            const data = mappedAnimals({ animales: res });
            setAnimals(data);
        });
    }, [])

    useEffect(() => {
        if(!animals) return;

        const filter = filteredAnimals();
        setFilterAnimals(filter);
    }, [animals, filters])

    const fetchAnimals = async () => {
        const response = await fetch(import.meta.env.VITE_BACKEND_URL + "/api/v1/pet/",
        {
            method: "GET",
            headers: {
                "Content-Type": "application/json"
            },
        });

        const data = await response.json();
        return data.results;
    }

    const handleSearch = (e) => {
        e.preventDefault();
        const data = new FormData(e.target);
        const animal = {
            nombre : data.get("nombre"),
            tipo : data.get("tipo") === "tipo" ? "" : data.get("tipo"),
            tamaño : data.get("tamaño") === "tamaño" ? "" : data.get("tamaño"),
            edad : data.get("edad") === "edad" ? "" : data.get("edad")
        }

        setFilters(animal);
    }

    const filteredAnimals = () => {
        if(!animals.length) return [];

        const filter = animals?.filter((item) => {
            const defaultFilters = Object.values(filters).every((value) => value === "");
            if(defaultFilters) return true;

            let result = true;

            if(filters.nombre !== "") {
                if(!item.petName.toLowerCase().includes(filters.nombre.toLowerCase())) {
                    result = false; 
                }
            }

            if(filters.tipo !== "Tipo") {
                if(item.type !== filters.tipo) {
                    result = false
                }
            }

            if(filters.tamaño !== "Tamaño") {
                if(item.size !== filters.tamaño) {
                    result = false
                }
            }
            
            if(filters.edad !== "Edad") {
                if(item.age !== filters.edad) {
                    result = false
                }
            }
            
            return result
        })

        return filter; 
    } 

    return (
        <AnimalsContext.Provider value={{ animals: filterAnimals , handleSearch }}>
            {children}
        </AnimalsContext.Provider>
    )
    
}