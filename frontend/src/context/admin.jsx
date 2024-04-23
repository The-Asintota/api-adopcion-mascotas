import { createContext, useState } from "react";
import { USERS } from "../../utils/constants";

export const AdminContext = createContext()

export const AdminProvider = ({ children }) => {
    const [user, setUser] = useState(null) 
    
    const authenticateUser = (role) => {
        if (role === USERS.ADMIN || role === USERS.SHELTER) {
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