import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.jsx"
import Shelters from './pages/Shelters'
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import "./index.css";
import Adoption from "./pages/Adoption.jsx";
import Admin from "./pages/Admin.jsx";
import { AdminProvider } from "./context/admin.jsx";
import Shelter from "./pages/Shelter.jsx";
import Page404 from "./pages/404.jsx";
import Animal from "./pages/Animal.jsx";
import ProtectedRoute from "./pages/ProtectedRoute.jsx";

const router = createBrowserRouter([
  {
    path: "/",
    element: <App/>,
  },
  {
    path: "/shelters",
    element: <Shelters/>
  },
  {
    path: "/animals-for-adoption",
    element: <Adoption/>
  },
  {
    path: "/admin",
    element: <AdminProvider> <Admin/> </AdminProvider>
  },
  {
    path: "/shelter",
    element: <AdminProvider><Shelter/></AdminProvider>
  },
  {
    path: "/animal/:id",
    element: <Animal />
  },
  {
    path: "*",
    element: <Page404 />
  }
]);

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <RouterProvider router={router}>
      <App />
    </RouterProvider>
  </React.StrictMode>
);
