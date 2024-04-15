import React from "react";
import { useForm } from "react-hook-form";
import ErrorMessage from "../ErrorMessage";

const UploadAnimal = () => {
  const {
    register,
    getValues,
    handleSubmit,
    formState: { errors },
  } = useForm({
    defaultValues: {
        "name": "",
        "pet_type": "",
        "shelter": "",
        "race": "",
        "pet_sex": "",
        "age": "",
        "observations": "",
        "description": "",
        "image": null
    },
  });

  return (
    <div className='"w-full bg-[#4db8c0] rounded-xl shadow-2xl overflow-hidden p-8 space-y-4 md:space-y-8 mt-4 md:mt-6'>
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
        placeholder="Nombre de la mascota"
        className="peer h-10 w-full border-b-2 border-gray-300 text-white bg-transparent placeholder-transparent focus:outline-none focus:border-[#118A95]"
        id="name"
        name="name"
        {...register("name", {
            required:"Este campo es obligatorio"
        })}
        />
        <label
            className="absolute left-0 -top-3.5 text-gray-200 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-200 peer-placeholder-shown:top-2 peer-focus:-top-3.5 peer-focus:text-blue-500 peer-focus:text-sm"
            htmlFor="name"
          >
            Nombre de la mascota
          </label>
          <ErrorMessage error={errors.name}/>
        </div>
      </form>
    </div>
  );
};

export default UploadAnimal;
