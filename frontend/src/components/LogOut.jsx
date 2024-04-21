import React from "react";
import logOutIcon from "../assets/logOutIcon.svg";
import { useNavigate } from "react-router";

const LogOut = () => {
  const navigate = useNavigate();

  function handleLogOut() {
    const token = localStorage.getItem("token");
    localStorage.removeItem(token);
    navigate("/");
  }

  return (
    <button className="w-8 self-start mt-4 pt-2" onClick={handleLogOut}>
      <img src={logOutIcon} alt="" />
    </button>
  );
};

export default LogOut;
