import React, { useContext } from "react";
import logOutIcon from "../assets/logOutIcon.svg";
import { useNavigate } from "react-router";
import useUser from "../hooks/useUser";

const LogOut = () => {
  const navigate = useNavigate();
  const { logOutAdmin } = useUser();

  function handleLogOut() {
    logOutAdmin();
    navigate("/");
  }

  return (
    <button className="w-8 self-start mt-4 pt-2" onClick={handleLogOut}>
      <img src={logOutIcon} alt="Imagen de icono para cerrar sesión" />
    </button>
  );
};

export default LogOut;
