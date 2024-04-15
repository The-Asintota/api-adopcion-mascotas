import React from "react";
import { Route, Navigate } from "react-router-dom";

const ProtectedRoute = ({ element, ...rest }) => {
  const token = localStorage.getItem('token'); // Obtiene el estado de inicio de sesión del localStorage
    console.log(token);
  // Si el usuario está autenticado (si isLogged es true), muestra el elemento de la ruta, de lo contrario, redirige a otra página (por ejemplo, página de inicio de sesión)
  return token ? <Route {...rest} element={element} /> : <Navigate to="/" replace />;
};

export default ProtectedRoute;
