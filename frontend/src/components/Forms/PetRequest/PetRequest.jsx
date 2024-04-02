import React from "react";

const PetRequest = ({ isActive, onClose }) => {
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
              <form method="POST" action="#" className="space-y-6 pt-4">
                <div className="relative">
                  <input
                    placeholder="john@prueba.com"
                    className="peer h-10 w-full border-b-2 border-gray-300 text-white bg-transparent placeholder-transparent focus:outline-none focus:border-[#118A95]"
                    required
                    id="email"
                    name="email"
                    type="email"
                  />
                  <label
                    className="absolute left-0 -top-3.5 text-gray-200 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-200 peer-placeholder-shown:top-2 peer-focus:-top-3.5 peer-focus:text-blue-500 peer-focus:text-sm"
                    htmlFor="email"
                  >
                    Correo Electronico
                  </label>
                </div>
                <div className="relative">
                  <input
                    placeholder="Numero de telefono"
                    className="peer h-10 w-full border-b-2 border-gray-300 text-white bg-transparent placeholder-transparent focus:outline-none focus:border-[#118A95]"
                    required
                    id="phoneNumber"
                    name="phoneNumber"
                    type="number"
                  />
                  <label
                    className="absolute left-0 -top-3.5 text-gray-200 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-200 peer-placeholder-shown:top-2 peer-focus:-top-3.5 peer-focus:text-blue-500 peer-focus:text-sm"
                    htmlFor="phoneNumber"
                  >
                    Numero de telefono
                  </label>
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
                  />
                  <label
                    className="absolute left-0 -top-3.5 text-gray-200 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-200 peer-placeholder-shown:top-2 peer-focus:-top-3.5 peer-focus:text-blue-500 peer-focus:text-sm"
                    htmlFor="address"
                  >
                    Tu mensaje
                  </label>
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
