import React from "react";
import { useForm } from "react-hook-form";
import ErrorMessage from "../ErrorMessage";


const SignIn = ({ isActive, onClose }) => {
   const {
    register,
    getValues,
    handleSubmit,
    formState: { errors },
  } = useForm();

  const onSubmit = (data) => console.log(data)

  return (
    <>
      {isActive && (
        <div className="fixed inset-0 z-50 flex justify-center items-center">
          <div className="fixed inset-0 bg-gray-400 opacity-70"></div>
          <div className="w-full max-w-md z-10 bg-[#4db8c0] rounded-xl shadow-2xl overflow-hidden p-8 space-y-8">
            <div className="relative">
              <div className="absolute top-0 right-0 cursor-pointer" onClick={onClose}>
                x
              </div>
              <h2 className="text-center text-4xl font-extrabold text-white">
                Iniciar Sesion
              </h2>
              <form method="POST" onSubmit={handleSubmit(onSubmit)} className="space-y-6">
                <div className="relative">
                  <input
                    placeholder="john@prueba.com"
                    className="peer h-10 w-full border-b-2 border-gray-300 text-white bg-transparent placeholder-transparent focus:outline-none focus:border-[#118A95]"
                    id="email"
                    name="email"
                    {...register("email", {
                      required: "Este campo es obligatorio",
                      pattern: {
                        value: /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/,
                        message: "Por favor, introduce un correo electronico válido"
                      },
                    })}
                  />
                  <label
                    className="absolute left-0 -top-3.5 text-gray-200 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-200 peer-placeholder-shown:top-2 peer-focus:-top-3.5 peer-focus:text-blue-500 peer-focus:text-sm"
                    htmlFor="email"
                  >
                    Correo Electronico
                  </label>
                  <ErrorMessage error={errors.email} />
                </div>
                <div className="relative">
                  <input
                    placeholder="Password"
                    className="peer h-10 w-full border-b-2 border-gray-200 text-white bg-transparent placeholder-transparent focus:outline-none focus:border-blue-500"
                    required
                    id="password"
                    name="password"
                    type="password"
                  />
                  <label
                    className="absolute left-0 -top-3.5 text-gray-200 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-200 peer-placeholder-shown:top-2 peer-focus:-top-3.5 peer-focus:text-blue-500 peer-focus:text-sm"
                    htmlFor="password"
                  >
                    Contraseña
                  </label>
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
                  Iniciar sesion
                </button>
              </form>
            </div>
          </div>
        </div>
      )}
    </>
  );
};

export default SignIn;
