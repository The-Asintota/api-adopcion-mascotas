import { useContext, useEffect } from "react"
import { AdminContext } from "../context/admin"

export default function useUser({ userType }) {
    const { user, setUser } = useContext(AdminContext)

    useEffect(() => {
        setUser(userType)
    }, [])

    return { user, setUser }
}
