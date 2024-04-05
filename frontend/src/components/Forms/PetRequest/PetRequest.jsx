import React from "react";
import { useForm } from "react-hook-form";
import ErrorMessage from "../ErrorMessage";

const PetRequest = ({ isActive, onClose }) => {
  const {
    register,
    getValues,
    handleSubmit,
    formState: { errors },
  } = useForm();

  const onSubmit = (data) => console.log(data);

  return (
    <>
      {isActive && (
        <div className="fixed inset-0 z-50 flex justify-center items-center">
          <div className="fixed inset-0 bg-gray-400 opacity-70"></div>
          <div className="w-full max-w-3xl z-10 bg-[#4db8c0] rounded-xl shadow-2xl overflow-hidden p-8 space-y-8">
            <div className="relative">
              <div
                className="absolute top-0 right-0 cursor-pointer"
                onClick={onClose}
              >
                x
              </div>
              <h2 className="text-center text-4xl font-extrabold text-white">
                ¿Cómo adoptar a NOMBRE MASCOTA PROP?
              </h2>
              <p>¡Gracias por darle una nueva oportunidad a un animal!</p>
              <p>
                Ahora solo necesitas comunicarte con la persona que registró a
                NOMBRE MASCOTA PROP.
              </p>
              <form
                method="POST"
                onSubmit={handleSubmit(onSubmit)}
                className="space-y-6 pt-4"
              >
                <div className="relative">
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
                    className="absolute left-0 -top-3.5 text-gray-200 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-200 peer-placeholder-shown:top-2 peer-focus:-top-3.5 peer-focus:text-blue-500 peer-focus:text-sm"
                    htmlFor="email"
                  >
                    Correo Electronico
                  </label>
                  <ErrorMessage error={errors.email} />
                </div>
                <div className="relative">
                  <input
                    placeholder="Numero de telefono"
                    className="peer h-10 w-full border-b-2 border-gray-300 text-white bg-transparent placeholder-transparent focus:outline-none focus:border-[#118A95]"
                    id="phoneNumber"
                    name="phoneNumber"
                    type="number"
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

                <div className="relative">
                  <textarea
                    placeholder="Tu mensaje"
                    className="peer w-full border-b-2 border-gray-300 text-white bg-transparent placeholder-transparent focus:outline-none focus:border-[#118A95]"
                    required
                    id="address"
                    name="address"
                    type="text"
                    rows="6"
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
                    Tu mensaje
                  </label>
                  <ErrorMessage error={errors.address} />
                </div>
                <button
                  className="w-full py-2 px-4 bg-[#118A95] hover:bg-[#3bdbe9] rounded-md shadow-lg text-white font-semibold transition duration-200"
                  type="submit"
                >
                  Enviar Mensaje
                </button>
              </form>
            </div>
          </div>
        </div>
      )}
    </>
  );
};

export default PetRequest;
