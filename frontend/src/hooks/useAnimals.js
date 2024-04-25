import { useContext } from "react";
import { AnimalsContext } from "../context/animals";

export default function useAnimals() {
    const { animals, handleSearch, filterAnimals } = useContext(AnimalsContext);

    const getAnimalById = ({ id }) => {
        const animal = animals?.find(animal => animal.id === id);
        return animal;
    }

    return { animals, getAnimalById, handleSearch, filterAnimals }
}