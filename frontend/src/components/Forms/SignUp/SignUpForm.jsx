import React, { useState, useEffect } from "react";
import { useForm } from "react-hook-form";
import FormRequest from "../FormRequest";
import ErrorMessage from "../ErrorMessage";
import UploadLogo from "./UploadLogo";
import SuccessfulNotification from "../SuccessfulNotification";

const SignUpForm = ({ link, onClick }) => {
  const {
    register,
    getValues,
    handleSubmit,
    formState: { errors },
  } = useForm({
    defaultValues: {
      shelter_name: "",
      shelter_responsible: "",
      shelter_phone_number: "",
      email: "",
      shelter_address: "",
      password: "",
      confirm_password: "",
      shelter_logo: null,
    },
  });

  const [logo, setLogo] = useState(null);
  const [userCreated, setUserCreated] = useState(false);
  const [showSuccess, setShowSuccess] = useState(false);
  const [showPassword, setShowPassword] = useState(false);

  function handleUploadLogo(url) {
    setLogo(url);
  }

  function handleShowSuccess() {
    setShowSuccess(true);
  }

  function handleShowPassword() {
    setShowPassword((prevShowPassword) => !prevShowPassword);
  }

  const openEye = (
    <button onClick={handleShowPassword}>
      <svg
        className="h-4 w-4 text-white place-self-center"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
      >
        <path
          strokeLinecap="round"
          strokeLinejoin="round"
          strokeWidth="2"
          d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
        />
        <path
          strokeLinecap="round"
          strokeLinejoin="round"
          strokeWidth="2"
          d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"
        />
      </svg>
    </button>
  );

  const closeEye = (
    <button onClick={handleShowPassword}>
      <svg
        className="h-4 w-4 text-white"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
      >
        <path
          strokeLinecap="round"
          strokeLinejoin="round"
          strokeWidth="2"
          d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.88 9.88l-3.29-3.29m7.532 7.532l3.29 3.29M3 3l3.59 3.59m0 0A9.953 9.953 0 0112 5c4.478 0 8.268 2.943 9.543 7a10.025 10.025 0 01-4.132 5.411m0 0L21 21"
        />
      </svg>
    </button>
  );

  useEffect(() => {
    if (userCreated) {
      console.log("user created");
      handleShowSuccess();
    }
  }, [userCreated]);

  return (
    <div className="w-full bg-[#4db8c0] rounded-xl shadow-2xl overflow-hidden p-8 space-y-4 md:space-y-8 mt-4 md:mt-6">
      <h2 className="text-center text-xl md:text-4xl font-extrabold text-white">
        Registra a tu asociacion
      </h2>
      <form
        method="POST"
        className="space-y-6"
        onSubmit={handleSubmit(() => {})}
      >
        <div className="relative">
          <input
            placeholder="Nombre de tu asociacion"
            className="peer h-10 w-full border-b-2 border-gray-300 text-white bg-transparent placeholder-transparent focus:outline-none focus:border-[#118A95]"
            id="shelter_name"
            name="shelter_name"
            autoComplete="organization"
            {...register("shelter_name", {
              required: "Este campo es obligatorio",
            })}
          />
          <label
            className="absolute left-0 -top-3.5 text-gray-200 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-200 peer-placeholder-shown:top-2 peer-focus:-top-3.5 peer-focus:text-blue-500 peer-focus:text-sm"
            htmlFor="shelter_name"
          >
            Nombre de la asociacion
          </label>
          <ErrorMessage error={errors.shelter_name} />
        </div>
        <div className="relative">
          <input
            placeholder="Pedro Perez"
            className="peer h-10 w-full border-b-2 border-gray-300 text-white bg-transparent placeholder-transparent focus:outline-none focus:border-[#118A95]"
            id="shelter_responsible"
            name="shelter_responsible"
            autoComplete="name"
            {...register("shelter_responsible", {
              required: "Este campo es obligatorio",
              pattern: {
                value: /^([A-Za-z]+\s?)+$/,
                message: "Por favor, introduce solo letras",
              },
            })}
          />
          <label
            className="absolute left-0 -top-3.5 text-gray-200 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-200 peer-placeholder-shown:top-2 peer-focus:-top-3.5 peer-focus:text-blue-500 peer-focus:text-sm"
            htmlFor="shelter_responsible"
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
              id="shelter_phone_number"
              name="shelter_phone_number"
              autoComplete="tel-country-code"
              {...register("shelter_phone_number", {
                required: "Este campo es obligatorio",
                pattern: {
                  value: /^[\d\s+-]+$/,
                  message: "Por favor, introduce un número de teléfono válido",
                },
              })}
            />
            <label
              className="absolute left-0 -top-3.5 text-gray-200 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-200 peer-placeholder-shown:top-2 peer-focus:-top-3.5 peer-focus:text-blue-500 peer-focus:text-sm"
              htmlFor="shelter_phone_number"
            >
              Numero de telefono
            </label>
            <ErrorMessage error={errors.shelter_phone_number} />
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
            id="shelter_address"
            name="shelter_address"
            {...register("shelter_address", {
              required: "Este campo es obligatorio",
              pattern: {
                value: /^[A-Za-z0-9\s.,#\-áéíóúÁÉÍÓÚ]+$/,
                message: "Por favor, introduce una dirección válida",
              },
            })}
          />
          <label
            className="absolute left-0 -top-3.5 text-gray-200 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-200 peer-placeholder-shown:top-2 peer-focus:-top-3.5 peer-focus:text-blue-500 peer-focus:text-sm"
            htmlFor="shelter_address"
          >
            Dirección de la asociación
          </label>
          <ErrorMessage error={errors.shelter_address} />
        </div>
        <div className="flex flex-row w-full">
          <div className="relative w-1/2 flex">
            <input
              placeholder="Password"
              className="peer h-10 w-full border-b-2 border-gray-200 text-white bg-transparent placeholder-transparent focus:outline-none focus:border-blue-500"
              id="password"
              name="password"
              type={showPassword ? "text" : "password"}
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
            {showPassword ? openEye : closeEye}
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

            <ErrorMessage error={errors.password} />
          </div>
        </div>
        <div className="relative">
          <UploadLogo onImageUpload={handleUploadLogo} />
        </div>
        <FormRequest
          endpoint="/api/v1/shelter/"
          formData={{
            shelter_name: getValues("shelter_name"),
            shelter_responsible: getValues("shelter_responsible"),
            shelter_phone_number: getValues("shelter_phone_number"),
            email: getValues("email"),
            shelter_address: getValues("shelter_address"),
            password: getValues("password"),
            confirm_password: getValues("confirm_password"),
            shelter_logo: logo,
          }}
          onSuccess={() => setUserCreated(true)}
          textButton="Registro"
        />
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

export default SignUpForm;
