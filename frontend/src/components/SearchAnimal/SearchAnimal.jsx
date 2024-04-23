import useAnimals from "../../hooks/useAnimals";
import "./SearchAnimal.css";

export default function SearchAnimal () {
    const { handleSearch } = useAnimals();

    return (
        <section className="flex items-center justify-center mt-10 mb-5">
            <form onSubmit={handleSearch} className="search-animal flex gap-5 "> 
                <input name="nombre" id="nombre" className="rounded-md text-gray-950 px-6" type="text" placeholder="Firulais" />
                <select className="rounded-md bg-[var(--green)] px-2" name="tipo" id="tipo">
                    <option value="Tipo">Tipo</option>
                    <option value="Gato">Gato</option>
                    <option value="Perro">Perro</option>
                </select>
                <select className="rounded-md bg-[var(--green)] px-2" name="tamaño" id="tamaño">
                    <option value="Tamaño">Tamaño</option>
                    <option value="Grande">Grande</option>
                    <option value="Mediano">Mediano</option>
                    <option value="Pequeño">Pequeño</option>
                </select>
                <select className="rounded-md bg-[var(--green)] px-2" name="edad" id="edad">
                    <option value="Edad">Edad</option>
                    <option value="1">1 año</option>
                    <option value="2">2 años</option>
                </select>
                <input className="bg-[var(--green)] cursor-pointer w-full py-2 px-8 rounded-md shadow-lg font-semibold " 
                    type="submit" 
                    value="Buscar" />
            </form>
        </section>
    )
}