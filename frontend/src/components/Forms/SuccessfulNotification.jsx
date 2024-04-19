import React from "react";

const SuccessfulNotification = ({ onClick, onClose, isActive, text }) => {
  return (
    <>
      {isActive && (
        <div className="fixed inset-0 z-50 flex justify-center items-center">
          <div className="fixed inset-0 bg-gray-400 opacity-70"></div>
          <div className="w-80 max-x-md z-10 bg-[#4db8c0] rounded-xl shadow-2xl overflow-hidden p-8 space-x-8">
            <div className="relative flex flex-col items-center">
              <div
                className="absolute top-0 right-0 cursor-pointer"
                onClick={onClose}
              >
                x
              </div>
              <h2 className="py-6">{text}</h2>
              <button
                onClick={onClick}
                className="bg-[#118A95] hover:bg-[#3bdbe9 py-2 px-4 rounded-md shadow-lg text-white font-semibold transition duration-200"
              >
                Siguiente
              </button>
            </div>
          </div>
        </div>
      )}
    </>
  );
};

export default SuccessfulNotification;
