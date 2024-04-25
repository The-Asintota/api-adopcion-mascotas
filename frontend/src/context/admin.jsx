import { createContext, useState } from "react";
import { USERS } from "../../utils/constants";

export const AdminContext = createContext()

export const AdminProvider = ({ children }) => {
    const [user, setUser] = useState(() => {
        const role = sessionStorage.getItem("role")
        const token = sessionStorage.getItem("token")

        return role && token ? { role, token } : null
    }) 

    const authenticateUser = ({ role, token }) => {
        if (role === USERS.ADMIN || role === USERS.SHELTER) {
            setUser({ role, token })
            sessionStorage.setItem("role", role)
            sessionStorage.setItem("token", token)
        } else {
            setUser(null)
        }
    }

    const logOutAdmin = () => {
        setUser({
            role: null,
            token: null
        })

        sessionStorage.removeItem("role")
        sessionStorage.removeItem("token")
    }

    const isLogged = () => {
        return user?.role !== null && user?.token !== null
    }

    return (
        <AdminContext.Provider value={{ user, authenticateUser, logOutAdmin, isLogged }}>
            {children}
        </AdminContext.Provider>
    )
    
}