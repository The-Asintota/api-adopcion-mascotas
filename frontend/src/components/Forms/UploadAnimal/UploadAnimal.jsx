import React, { useState, useEffect } from "react";
import { useForm } from "react-hook-form";
import ErrorMessage from "../ErrorMessage";
import UploadLogo from "../SignUp/UploadLogo";
import FormRequest from "../FormRequest";
import SuccessfulNotification from "../SuccessfulNotification";

const UploadAnimal = () => {
  const {
    register,
    getValues,
    handleSubmit,
    reset,
    formState: { errors },
  } = useForm({
    defaultValues: {
      pet_name: "",
      pet_type: "",
      shelter: "",
      pet_race: "",
      pet_sex: "",
      pet_age: "",
      pet_observations: "",
      pet_description: "",
      pet_image: null,
    },
  });

  const [petType, setPetType] = useState("Perro");
  const [petSex, setPetSex] = useState("Hembra");
  const [showSuccess, setShowSuccess] = useState(false);
  const [petImage, setPetImage] = useState(null)
  const [petCreated, setPetCreated] = useState(false)

  function handlePetType(e) {
    setPetType(e.target.value);
  }

  function handlePetSex(e) {
    setPetSex(e.target.value);
  }

  function handlePetImage(url) {
    setPetImage(url)
  }

  function handleClickButton() {
    setShowSuccess(false);
    reset({
      pet_name: "",
      pet_type: "",
      pet_race: "",
      pet_sex: "",
      pet_age: "",
      pet_observations: "",
      pet_description: "",
      pet_image: null,
    });
  }

  useEffect(() => {
    if (petCreated) {
      setShowSuccess(true);
    }
  }, [petCreated]);


  return (
    <div className="w-1/3 bg-[#4db8c0] rounded-xl shadow-2xl overflow-hidden p-8 space-y-4 md:space-y-8 mt-4 md:mt-6 text-white">
      <h2 className="text-center text-xl md:text-4xl font-extrabold text-white">
        Registra a tu mascota
      </h2>
      <form
        method="POST"
        className="space-y-6"
        onSubmit={handleSubmit(() => {})}
      >
        <div className="relative">
          <input
            placeholder="Nombre del animal"
            className="peer h-10 w-full border-b-2 border-gray-300 text-white bg-transparent placeholder-transparent focus:outline-none focus:border-[#118A95]"
            id="pet_name"
            name="pet_name"
            autoComplete=""
            {...register("pet_name", {
              required: "Este campo es obligatorio",
              pattern: {
                value: /^[\p{L}\s]+$/,
                message: "Por favor, introduce solo letras y espacios",
              },
              maxLength: {
                value: 50,
                message: "El nombre debe tener menos de 50 caracteres",
              }
            })}
          />
          <label
            className="absolute left-0 -top-3.5 text-gray-200 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-200 peer-placeholder-shown:top-2 peer-focus:-top-3.5 peer-focus:text-blue-500 peer-focus:text-sm"
            htmlFor="pet_name"
          >
            Nombre del animal
          </label>
          <ErrorMessage error={errors.pet_name} />
        </div>
        <div className="flex flex-row w-full">
          <div className="relative w-1/2">
            <label htmlFor="pet_type" className="text-gray-200">
              Tipo de mascota:
            </label>
            <select
              id="pet_type"
              value={petType}
              onChange={handlePetType}
              className="peer h-10 w-28 border-gray-300 text-gray-200 bg-transparent placeholder-transparent focus:outline-none focus:border-[#118A95]"
            >
              <option value="Perro">Perro</option>
              <option value="Gato">Gato</option>
            </select>
            <ErrorMessage error={errors.pet_type} />
          </div>
          <div className="relative w-1/2 pl-2 ml-2">
            <label htmlFor="pet_sex" className="text-gray-200">
              Sexo:
            </label>
            <select
              id="pet_sex"
              value={petSex}
              onChange={handlePetSex}
              className="peer h-10 w-28 border-gray-300 text-gray-200 bg-transparent placeholder-transparent focus:outline-none focus:border-[#118A95]"
            >
              <option value="Hembra">Hembra</option>
              <option value="Macho">Macho</option>
            </select>
            <ErrorMessage error={errors.pet_sex} />
          </div>
        </div>
        <div className="flex flex-row w-full">
          <div className="relative w-1/2">
            <input
              placeholder="Raza del animal"
              className="peer h-10 w-full border-b-2 border-gray-300 text-white bg-transparent placeholder-transparent focus:outline-none focus:border-[#118A95]"
              id="pet_race"
              name="pet_race"
              autoComplete=""
              {...register("pet_race", {
                required: "Este campo es obligatorio",
                pattern: {
                  value: /^[\p{L}\s]+$/,
                  message: "Por favor, introduce solo letras y espacios",
                }
              })}
            />
            <label
              className="absolute left-0 -top-3.5 text-gray-200 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-200 peer-placeholder-shown:top-2 peer-focus:-top-3.5 peer-focus:text-blue-500 peer-focus:text-sm"
              htmlFor="pet_race"
            >
              Raza del animal
            </label>
            <ErrorMessage error={errors.pet_race} />
          </div>
          <div className="relative w-1/2 pl-2 ml-2">
            <input
              placeholder="pet_age"
              className="peer h-10 w-full border-b-2 border-gray-300 text-white bg-transparent placeholder-transparent focus:outline-none focus:border-[#118A95]"
              id="pet_age"
              name="pet_age"
              type="pet_age"
              {...register("pet_age", {
                required: "Este campo es obligatorio",
                value: {
                  min: 1,
                  max: 99,
                  message: "La edad debe estar entre 1 y 99",
                },
              })}
            />
            <label
              className="absolute pl-2 left-0 -top-3.5 text-gray-200 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-200 peer-placeholder-shown:top-2 peer-focus:-top-3.5 peer-focus:text-blue-500 peer-focus:text-sm"
              htmlFor="pet_age"
            >
              Edad:
            </label>
            <ErrorMessage error={errors.pet_age} />
          </div>
        </div>
        <div className="relative">
          <input
            placeholder="Descripcion de la mascota"
            className="peer h-10 w-full border-b-2 border-gray-300 text-white bg-transparent placeholder-transparent focus:outline-none focus:border-[#118A95]"
            id="pet_description"
            name="pet_description"
            {...register("pet_description", {
              required: "Este campo es obligatorio",
            })}
          />
          <label
            className="absolute left-0 -top-3.5 text-gray-200 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-200 peer-placeholder-shown:top-2 peer-focus:-top-3.5 peer-focus:text-blue-500 peer-focus:text-sm"
            htmlFor="pet_description"
          >
            Descripcion del animal:
          </label>
          <ErrorMessage error={errors.pet_description} />
        </div>
        <div className="relative">
          <input
            placeholder="Descripcion de la mascota"
            className="peer h-10 w-full border-b-2 border-gray-300 text-white bg-transparent placeholder-transparent focus:outline-none focus:border-[#118A95]"
            id="pet_observations"
            name="pet_observations"
            {...register("pet_observations", {
              required: "Este campo es obligatorio",
            })}
          />
          <label
            className="absolute left-0 -top-3.5 text-gray-200 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-200 peer-placeholder-shown:top-2 peer-focus:-top-3.5 peer-focus:text-blue-500 peer-focus:text-sm"
            htmlFor="pet_observations"
          >
            Observaciones:
          </label>
          <ErrorMessage error={errors.pet_observations} />
        </div>
        <div className="relative">
          <UploadLogo onImageUpload={handlePetImage}/>
        </div>
        <FormRequest
          endpoint="/api/v1/pet/"
          formData={{
            pet_name: getValues("pet_name"),
            pet_type: petType,
            pet_race: getValues("pet_race"),
            pet_sex: petSex,
            pet_age:  getValues("pet_age"),
            pet_observations:  getValues("pet_observations"),
            pet_description: getValues("pet_description"),
            pet_image: petImage,
          }}
          onSuccess={() => setPetCreated(true)}
          textButton="Registro"
        />
      </form>
      <SuccessfulNotification
        isActive={showSuccess}
        onClick={handleClickButton}
        onClose={handleClickButton}
        text="Registro de mascota exitoso"
      />
    </div>
  );
};

export default UploadAnimal;
