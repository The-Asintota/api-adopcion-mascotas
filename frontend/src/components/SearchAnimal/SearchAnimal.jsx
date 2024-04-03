
export default function SearchAnimal ({ onChange }) {

    return (
        <section className="flex gap-x-10 items-center justify-center mt-10 mb-5">
            <form onSubmit={onChange} className="flex space-x-5"> 
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
                    <option value="1 año">1 año</option>
                    <option value="2 años">2 años</option>
                </select>
                <input className="bg-[var(--green)] cursor-pointer w-full py-2 px-8 rounded-md shadow-lg font-semibold " 
                    type="submit" 
                    value="Buscar" />
            </form>
        </section>
    )
}