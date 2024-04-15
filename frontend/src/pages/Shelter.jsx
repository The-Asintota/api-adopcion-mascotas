// Shelter.js

import React from "react";
import Header from "../components/Header/Header";
import ShelterProfile from "../components/ShelterProfile";
import Footer from "../components/Footer/Footer";
import { USERS } from "../../utils/constants";
import useUser from "../hooks/useUser";

const Shelter = () => {
  const { user } = useUser({ userType: USERS.SHELTER });
/*   const token = localStorage.getItem("token"); */

/*   const renderShelterProfile = () => {
    if (token) {
      return <ShelterProfile />;
    } else {
      return <p>No hay token</p>;
    }
  }; */

  return (
    <>
      <Header />
      {/* <main>{renderShelterProfile()}</main> */}
      <main>
        <ShelterProfile/>
      </main>
      <Footer />
    </>
  );
};

export default Shelter;
