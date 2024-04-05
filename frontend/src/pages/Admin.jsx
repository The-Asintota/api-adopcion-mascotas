import React, { useContext, useEffect } from 'react'
import Header from '../components/Header/Header';
import AdoptionSection from '../components/AdoptionSection/AdoptionSection';
import ProtectorasSection from '../components/ProtectorasSection/ProtectorasSection';
import Footer from '../components/Footer/Footer';
import { AdminContext } from '../context/admin';

const Admin = () => {
    const { user, setUser } = useContext(AdminContext)
    
    useEffect(() => {
        setUser("admin")
    }, [])
    
    return (
        <>
            <Header />
            <main>
                <AdoptionSection />
                <ProtectorasSection />
            </main>
            <Footer />
        </>

    );
}

export default Admin;