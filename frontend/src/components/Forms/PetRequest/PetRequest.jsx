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
      pet_name: "",
      shelter_uuid: "",
      user_email: "",
      user_name: "",
      user_phone: "",
      message: "",
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
                      id="user_name"
                      name="user_name"
                      {...register("user_name", {
                        required: "Este campo es obligatorio",
                      })}
                    />
                    <label
                      className="absolute left-0 -top-3.5 text-gray-200 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-200 peer-placeholder-shown:top-2 peer-focus:-top-3.5 peer-focus:text-blue-500 peer-focus:text-sm"
                      htmlFor="user_name"
                    >
                    Nombre
                  </label>
                </div>

                <div className="relative">
                  <input
                    placeholder="john@prueba.com"
                    className="peer h-10 w-full border-b-2 border-gray-300 text-white bg-transparent placeholder-transparent focus:outline-none focus:border-[#118A95]"
                    id="user_email"
                    name="user_email"
                    type="email"
                    {...register("user_email", {
                      required: "Este campo es obligatorio",
                      pattern: {
                        value: /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/,
                        message: "Por favor, introduce un correo electronico válido"
                      },
                    })}
                  />
                  <label
                    className="absolute left-0 -top-3.5 text-gray-200 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-200 peer-placeholder-shown:top-2 peer-focus:-top-3.5 peer-focus:text-blue-500 peer-focus:text-sm"
                    htmlFor="user_email"
                  >
                    Correo Electronico
                  </label>
                  <ErrorMessage error={errors.user_email} />
                </div>
                <div className="relative">
                  <input
                    placeholder="Numero de telefono"
                    className="peer h-10 w-full border-b-2 border-gray-300 text-white bg-transparent placeholder-transparent focus:outline-none focus:border-[#118A95]"
                    id="user_phone"
                    name="user_phone"
                    type="tel"
                    autoComplete="tel-country-code"
                    {...register("user_phone", {
                      required: "Este campo es obligatorio",
                      pattern: {
                        value: /^[\d\s+-]+$/,
                        message: "Por favor, introduce un número de teléfono válido",
                      },
                    })}
                  />
                  <label
                    className="absolute left-0 -top-3.5 text-gray-200 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-200 peer-placeholder-shown:top-2 peer-focus:-top-3.5 peer-focus:text-blue-500 peer-focus:text-sm"
                    htmlFor="user_phone"
                  >
                    Numero de telefono
                  </label>
                  <ErrorMessage error={errors.user_phone} />
                </div>

                <div className="relative">
                  <textarea
                    placeholder="Tu mensaje"
                    className="peer w-full border-b-2 border-gray-300 text-white bg-transparent placeholder-transparent focus:outline-none focus:border-[#118A95]"
                    required
                    id="message"
                    name="message"
                    type="text"
                    rows="6"
                    {...register("message", {
                      required: "Este campo es obligatorio"
                    })}
                  />
                  <label
                    className="absolute left-0 -top-3.5 text-gray-200 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-200 peer-placeholder-shown:top-2 peer-focus:-top-3.5 peer-focus:text-blue-500 peer-focus:text-sm"
                    htmlFor="message"
                  >
                    Tu mensaje
                  </label>
                  <ErrorMessage error={errors.message} />
                </div>
                <FormRequest
                  endpoint="/api/v1/email/adoption/"
                  formData={{
                    pet_name: petName,
                    shelter_uuid: shelterId,
                    user_email: getValues("user_email"),
                    user_name: getValues("user_name"),
                    user_phone: `+${getValues("user_phone")}`,
                    message: getValues("message"),
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
