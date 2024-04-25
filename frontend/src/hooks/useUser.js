import { useContext, useEffect } from "react"
import { AdminContext } from "../context/admin"

export default function useUser() {
    const { user, setUser, isLogged, logOutAdmin, authenticateUser } = useContext(AdminContext)

    return { user, setUser, isLogged, logOutAdmin, authenticateUser }
}
