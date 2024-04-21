import mockUpJson from "../src/petData.json";

export const mappedAnimals = () => {
    // Evitamos seguir el contrato de la API
    // y cambiamos el nombre de las propiedades
    // para que sea global y no dependa de la API
    // aumenta la reutilización del componente
    const animales = Object.values(mockUpJson).flatMap(item => item);
    const mapped = animales.map(item => {
      return {
        id : item.id,
        urlImage : item.imagen,
        petName : item.nombre,
        age : item.edad,
        breed : item.raza,
        sex : item.sexo,
        size : item.tamaño,
        description : item.descripcion,
        observations : item.observaciones
      }
    })
    
    return mapped 
}