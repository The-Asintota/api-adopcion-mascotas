import React, { useState, useEffect } from "react";
import { useForm } from "react-hook-form";
import axios from "axios";
import ErrorMessage from "../ErrorMessage";
import UploadLogo from "./UploadLogo";
import SuccessfulNotification from "../SuccessfulNotification";

const SignUp = ({ link, onClick }) => {
  const {
    register,
    getValues,
    handleSubmit,
    formState: { errors },
  } = useForm({
    defaultValues: {
      name: "",
      responsible: "",
      phone_number: "",
      email: "",
      address: "",
      password: "",
      confirm_password: "",
      logo_url: null,
    },
  });

  const [userCreated, setUserCreated] = useState(false);
  const [logo, setLogo] = useState(null);
  const [showSuccess, setShowSuccess] = useState(true);

  function handleUploadLogo(url) {
    setLogo(url);
  }

  function handleShowSuccess() {
    setShowSuccess(true);
  }

  const urlRequest = `${import.meta.env.VITE_BACKEND_URL}/api/v1/shelter/`

    /* "https://api-adopcion-mascotas-production.up.railway.app/api/v1/shelter/"; */

  const onSubmit = (data) => {
    data.logo_url = logo;
    console.log(data);
    axios
      .post(urlRequest, data, {
        headers: { "Content-Type": "application/json" },
      })
      .then((response) => {
        console.log(response.data);
        if (response.status === 201) {
          setUserCreated(true);
        } else if (response.data === 400) {
          console.log(response.data.error);
        } else {
          console.log(response.data.error);
        }

        /*         response.status === 201
          ? setUserCreated(true)
          : console.log(response.data.error); */
      })
      .catch((error) => console.log(error));
  };

  useEffect(() => {
    if (userCreated) {
      console.log("user created");
      handleShowSuccess();
    }
  }, [userCreated]);

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
            id="name"
            name="name"
            autoComplete="organization"
            {...register("name", {
              required: "Este campo es obligatorio",
            })}
          />
          <label
            className="absolute left-0 -top-3.5 text-gray-200 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-200 peer-placeholder-shown:top-2 peer-focus:-top-3.5 peer-focus:text-blue-500 peer-focus:text-sm"
            htmlFor="name"
          >
            Nombre de la asociacion
          </label>
          <ErrorMessage error={errors.name} />
        </div>
        <div className="relative">
          <input
            placeholder="Pedro Perez"
            className="peer h-10 w-full border-b-2 border-gray-300 text-white bg-transparent placeholder-transparent focus:outline-none focus:border-[#118A95]"
            id="responsible"
            name="responsible"
            autoComplete="name"
            {...register("responsible", {
              required: "Este campo es obligatorio",
              pattern: {
                value: /^([A-Za-z]+\s?)+$/,
                message: "Por favor, introduce solo letras",
              },
            })}
          />
          <label
            className="absolute left-0 -top-3.5 text-gray-200 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-200 peer-placeholder-shown:top-2 peer-focus:-top-3.5 peer-focus:text-blue-500 peer-focus:text-sm"
            htmlFor="responsible"
          >
            Nombre de la persona responsable
          </label>
          <ErrorMessage error={errors.responsible} />
        </div>
        <div className="flex flex-row w-full">
          <div className="relative w-1/2 ">
            <input
              placeholder="Numero de telefono"
              className="peer h-10 w-full border-b-2 border-gray-300 text-white bg-transparent placeholder-transparent focus:outline-none focus:border-[#118A95]"
              id="phone_number"
              name="phone_number"
              autoComplete="tel-country-code"
              {...register("phone_number", {
                required: "Este campo es obligatorio",
                pattern: {
                  value: /^[\d\s+-]+$/,
                  message: "Por favor, introduce un número de teléfono válido",
                },
              })}
            />
            <label
              className="absolute left-0 -top-3.5 text-gray-200 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-200 peer-placeholder-shown:top-2 peer-focus:-top-3.5 peer-focus:text-blue-500 peer-focus:text-sm"
              htmlFor="phone_number"
            >
              Numero de telefono
            </label>
            <ErrorMessage error={errors.phone_number} />
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
                  message: "Por favor, introduce un correo electronico válido",
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
            {...register("address", {
              required: "Este campo es obligatorio",
              pattern: {
                value: /^[A-Za-z0-9\s.,#\-áéíóúÁÉÍÓÚ]+$/,
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
            <ErrorMessage error={errors.password} />
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
                  value === getValues().password || "La contraseña no coincide",
              })}
            />
            <label
              className="absolute pl-2  left-0 -top-3.5 text-gray-200 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-200 peer-placeholder-shown:top-2 peer-focus:-top-3.5 peer-focus:text-blue-500 peer-focus:text-sm"
              htmlFor="password"
            >
              Confirmar password
            </label>
            <ErrorMessage password />
          </div>
        </div>
        <div className="relative">
          <UploadLogo onImageUpload={handleUploadLogo} />
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
      <SuccessfulNotification
        isActive={showSuccess}
        onClick={onClick}
        onClose={() => setShowSuccess(false)}
        text="Registro exitoso."
      />
    </div>
  );
};

export default SignUp;
