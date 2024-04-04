import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.jsx"
import Shelters from './pages/Shelters'
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import "./index.css";
import Adoption from "./pages/Adoption.jsx";
import Admin from "./pages/Admin.jsx";

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
    element: <Admin/>
  }
]);

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <RouterProvider router={router}>
      <App />
    </RouterProvider>
  </React.StrictMode>
);
