import { createContext, useState } from "react";

export const AdminContext = createContext()

export const AdminProvider = ({ children }) => {
    const [user, setUser] = useState(null) 
    
    const authenticateUser = (role) => {
        if (role === "admin" || role === "shelter") {
            setUser({role})
        } else {
            setUser(null)
        }
    }

    return (
        <AdminContext.Provider value={{ user, authenticateUser }}>
            {children}
        </AdminContext.Provider>
    )
    
}