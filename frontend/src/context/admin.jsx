import { createContext, useState } from "react";

export const AdminContext = createContext()

export const AdminProvider = ({ children }) => {
    const [user, setUser] = useState(null) // admin, shelter or null

    return (
        <AdminContext.Provider value={{ user, setUser }}>
            {children}
        </AdminContext.Provider>
    )
    
}