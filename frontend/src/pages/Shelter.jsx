import React, { useContext } from "react";
import Header from "../components/Header/Header";
import ShelterProfile from "../components/ShelterProfile/ShelterProfile";
import Footer from "../components/Footer/Footer";
import { Link } from "react-router-dom";
import useUser from "../hooks/useUser";

const Shelter = () => {
  const { isLogged } = useUser();
  return (
    <>
      <Header />

      {isLogged() ? (
        <main className="bg-[#118A95]">
          <ShelterProfile />
        </main>
      ) : (
        <main className="bg-[#118A95] text-white text-center h-[44rem] flex flex-col justify-center items-center">
          <h2>Debes estar autenticado</h2>
          <Link to="/">Volver a la página principal</Link>
        </main>
      )}
      <Footer />
    </>
  );
};

export default Shelter;
