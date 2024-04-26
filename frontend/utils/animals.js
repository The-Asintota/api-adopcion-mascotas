
export const mappedAnimals = ({ animales }) => {
    // Evitamos seguir el contrato de la API
    // y cambiamos el nombre de las propiedades
    // para que sea global y no dependa de la API
    // aumenta la reutilización del componente
    const mapped = animales.map(item => {
      return {
        id : item.pet_uuid,
        urlImage : item.image,
        petName : item.pet_name,
        age : item.pet_age,
        breed : item.pet_race,
        sex : item.pet_sex,
        description : item.pet_description,
        observations : item.pet_observations,
        type: item.pet_type,
        shelter_uuid: item.shelter.uuid
      }
    })
    
    return mapped 
}