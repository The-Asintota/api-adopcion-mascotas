import { useContext } from "react";
import { AdminContext } from "../../context/admin";

export default function ProtectoraCard({ name, animals, location }) {
    const isAdmin = useContext(AdminContext)

    function Controls() {
        if(!isAdmin) return; 
    
        if(isAdmin.user === "admin") {
          return (
            <button style={{ backgroundColor: "#DC2626", padding: "10px 20px", margin: "0 auto"}} >Eliminar</button>
          )
        }
      }

    return (
        <li className="protectora-card">
        <img
          src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTpYh91b3d-KwbMR7wSRJQSoZggr30id2dp3Q&usqp=CAU"
          alt={`Protectora de animales globant ${name}`}
        />
        <div style={{ display: "flex", flexDirection: "column", alignItems: "start"}}>
          <h3>{name}</h3>
          <p>Animales en Adopción: {animals}</p>
          <p>Ubicación: {location}</p>
          <Controls />
        </div>
      </li>
    );
}