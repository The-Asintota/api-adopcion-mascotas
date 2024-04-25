import React from "react";
import { useForm } from "react-hook-form";
import ErrorMessage from "../ErrorMessage";
import FormRequest from "../FormRequest";

const PetRequest = ({ isActive, onClose, petName, shelterId }) => {
  const {
    register,
    getValues,
    handleSubmit,
    formState: { errors },
  } = useForm({
    defaultValues: {
      userName: "",
      email: "",
      phoneNumber: "",
      address: "",
    },
  });

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
                ¿Cómo adoptar a {petName}?
              </h2>
              <p>¡Gracias por darle una nueva oportunidad a un animal!</p>
              <p>
                Ahora solo necesitas comunicarte con la persona que registró a 
                {petName}.
              </p>
              <form
                method="POST"
                onSubmit={handleSubmit(() => {})}
                className="space-y-6 pt-4"
              >
                  <div className="relative">
                    <input
                      placeholder="Nombre de usuario"
                      className="peer h-10 w-full border-b-2 border-gray-300 text-white bg-transparent placeholder-transparent focus:outline-none focus:border-[#118A95]"
                      id="userName"
                      name="userName"
                      {...register("userName", {
                        required: "Este campo es obligatorio",
                      })}
                    />
                    <label
                      className="absolute left-0 -top-3.5 text-gray-200 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-200 peer-placeholder-shown:top-2 peer-focus:-top-3.5 peer-focus:text-blue-500 peer-focus:text-sm"
                      htmlFor="userName"
                    >
                    Nombre
                  </label>
                </div>

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
                <FormRequest
                  endpoint="/api/v1/email/adoption/"
                  formData={{
                    pet_name: petName,
                    shelter_uuid: shelterId,
                    user_email: getValues("email"),
                    user_name: getValues("userName"),
                    user_phone: `+${getValues("phoneNumber")}`,
                    message: getValues("address"),
                  }}
                  onSuccess={onClose}
                  textButton="Enviar"
                />
              </form>
            </div>
          </div>
        </div>
      )}
    </>
  );
};

export default PetRequest;
