import React from "react";
import { useForm } from "react-hook-form";
import ErrorMessage from "../ErrorMessage";

const SignUp = ({ link, onClick }) => {
  const {
    register,
    getValues,
    handleSubmit,
    formState: { errors },
  } = useForm();

  const onSubmit = (data) => console.log(data);

  return (
    <div className="w-full bg-[#4db8c0] rounded-xl shadow-2xl overflow-hidden p-8 space-y-8 mt-6">
      <h2 className="text-center text-4xl font-extrabold text-white">
        Registra a tu asociacion
      </h2>
      <form
        method="POST"
        className="space-y-6"
        onSubmit={handleSubmit(onSubmit)}
      >
        <div className="relative">
          <input
            placeholder="Nombre de tu asociacion"
            className="peer h-10 w-full border-b-2 border-gray-300 text-white bg-transparent placeholder-transparent focus:outline-none focus:border-[#118A95]"
            id="asociationName"
            name="asociationName"
            autoComplete="organization"
            {...register("asociationName", {
              required: "Este campo es obligatorio",
            })}
          />
          <label
            className="absolute left-0 -top-3.5 text-gray-200 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-200 peer-placeholder-shown:top-2 peer-focus:-top-3.5 peer-focus:text-blue-500 peer-focus:text-sm"
            htmlFor="asociationName"
          >
            Nombre de la asociacion
          </label>
          <ErrorMessage error={errors.asociationName} />
        </div>
        <div className="relative">
          <input
            placeholder="Pedro Perez"
            className="peer h-10 w-full border-b-2 border-gray-300 text-white bg-transparent placeholder-transparent focus:outline-none focus:border-[#118A95]"
            id="responsibleName"
            name="responsibleName"
            autoComplete="name"
            {...register("responsibleName", {
              required: "Este campo es obligatorio",
              pattern: {
                value: /^([A-Za-z]+\s?)+$/,
                message: "Por favor, introduce solo letras",
              },
            })}
          />
          <label
            className="absolute left-0 -top-3.5 text-gray-200 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-200 peer-placeholder-shown:top-2 peer-focus:-top-3.5 peer-focus:text-blue-500 peer-focus:text-sm"
            htmlFor="responsibleName"
          >
            Nombre de la persona responsable
          </label>
          <ErrorMessage error={errors.responsibleName} />
        </div>
        <div className="flex flex-row w-full">
          <div className="relative w-1/2 ">
            <input
              placeholder="Numero de telefono"
              className="peer h-10 w-full border-b-2 border-gray-300 text-white bg-transparent placeholder-transparent focus:outline-none focus:border-[#118A95]"
              id="phoneNumber"
              name="phoneNumber"
              autoComplete="tel-country-code"
              {...register("phoneNumber", {
                required: "Este campo es obligatorio",
                pattern: {
                  value: /^[\d\s+-]+$/,
                  message: "Por favor, introduce un número de teléfono válido",
                },
              })}
            />
            <label
              className="absolute left-0 -top-3.5 text-gray-200 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-200 peer-placeholder-shown:top-2 peer-focus:-top-3.5 peer-focus:text-blue-500 peer-focus:text-sm"
              htmlFor="phoneNumber"
            >
              Numero de telefono
            </label>
            <ErrorMessage error={errors.phoneNumber} />
          </div>
          <div className="relative w-1/2 pl-2 ml-2">
            <input
              placeholder="john@prueba.com"
              className="peer h-10 w-full border-b-2 border-gray-300 text-white bg-transparent placeholder-transparent focus:outline-none focus:border-[#118A95]"
              id="email"
              name="email"
              type="email"
              {...register("email", {
                required: "Este campo es obligatorio",
                pattern: {
                  value: /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/,
                  message: "Por favor, introduce un correo electronico válido"
                },
              })}
            />
            <label
              className="absolute pl-2 left-0 -top-3.5 text-gray-200 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-200 peer-placeholder-shown:top-2 peer-focus:-top-3.5 peer-focus:text-blue-500 peer-focus:text-sm"
              htmlFor="email"
            >
              Correo Electronico
            </label>
            <ErrorMessage error={errors.email} />
          </div>
        </div>
        <div className="relative">
          <input
            placeholder="Direccion de la asociacion"
            className="peer h-10 w-full border-b-2 border-gray-300 text-white bg-transparent placeholder-transparent focus:outline-none focus:border-[#118A95]"
            id="address"
            name="address"
            autoComplete="street-address"
            {...register("address", {
              required: "Este campo es obligatorio",
              pattern: {
                value: /^[A-Za-z0-9\s.,#-]+$/,
                message: "Por favor, introduce una dirección válida",
              },
            })}
          />
          <label
            className="absolute left-0 -top-3.5 text-gray-200 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-200 peer-placeholder-shown:top-2 peer-focus:-top-3.5 peer-focus:text-blue-500 peer-focus:text-sm"
            htmlFor="address"
          >
            Dirección de la asociación
          </label>
          <ErrorMessage error={errors.address} />
        </div>
        <div className="flex flex-row w-full">
          <div className="relative w-1/2">
            <input
              placeholder="Password"
              className="peer h-10 w-full border-b-2 border-gray-200 text-white bg-transparent placeholder-transparent focus:outline-none focus:border-blue-500"
              id="password"
              name="password"
              type="password"
              autoComplete="new-password"
              {...register("password", {
                required: "Este campo es obligatorio",
                minLength: {
                  value: 8,
                  message: "Debe tener al menos 8 caracteres",
                },
              })}
            />
            <label
              className="absolute left-0 -top-3.5 text-gray-200 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-200 peer-placeholder-shown:top-2 peer-focus:-top-3.5 peer-focus:text-blue-500 peer-focus:text-sm"
              htmlFor="password"
            >
              Contraseña
            </label>
            <ErrorMessage error={errors.password}/>
          </div>
          <div className="relative w-1/2 pl-2 ml-2">
            <input
              placeholder="Confirmar password"
              className="peer h-10 w-full border-b-2 border-gray-200 text-white bg-transparent placeholder-transparent focus:outline-none focus:border-blue-500"
              id="confirm_password"
              name="confirm_password"
              type="password"
              autoComplete="new-password"
              {...register("confirm_password", {
                required: "Password is required",
                validate: (value) =>
                  value === getValues().password ||
                  "La contraseña no coincide",
              })}
            />
            <label
              className="absolute pl-2  left-0 -top-3.5 text-gray-200 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-200 peer-placeholder-shown:top-2 peer-focus:-top-3.5 peer-focus:text-blue-500 peer-focus:text-sm"
              htmlFor="password"
            >
              Confirmar password
            </label>
            <ErrorMessage password/>
          </div>
        </div>
        <div className="flex items-center justify-between">
          <label className="flex items-center text-sm text-gray-200">
            <input
              className="form-checkbox h-4 w-4 text-[#118A95] bg-gray-800 border-gray-300 rounded"
              type="checkbox"
            />
            <span className="ml-2">Remember me</span>
          </label>
        </div>
        <button
          className="w-full py-2 px-4 bg-[#118A95] hover:bg-[#3bdbe9] rounded-md shadow-lg text-white font-semibold transition duration-200"
          type="submit"
        >
          Registro
        </button>
      </form>
      <div className="text-center text-gray-300">
        Ya estas registrado?
        <a
          className="text-[#118A95] hover:underline cursor-pointer"
          href={link}
          onClick={onClick}
        >
          Sign in
        </a>
      </div>
    </div>
  );
};

export default SignUp;
