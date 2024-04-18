import React, { useContext } from "react";
import Header from "../components/Header/Header";
import ShelterProfile from "../components/ShelterProfile";
import Footer from "../components/Footer/Footer";
import { AdminContext } from "../context/admin";
import { Link } from "react-router-dom";

const Shelter = () => {
  const { user } = useContext(AdminContext);

  return (
    <>
      <Header />

      {user ? (
        <main>
          <p>Usuario autenticado como {user.role}</p>
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
