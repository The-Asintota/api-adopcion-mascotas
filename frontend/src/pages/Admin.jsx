import React from 'react'
import Header from '../components/Header/Header';
import InicioSection from '../components/InicioSection/InicioSection';
import AdoptionSection from '../components/AdoptionSection/AdoptionSection';
import ProtectorasSection from '../components/ProtectorasSection/ProtectorasSection';
import Footer from '../components/Footer/Footer';
import { AdminProvider } from '../context/admin';

const Admin = () => {
    return (
        <AdminProvider>
            <Header />
            <main>
                <AdoptionSection />
                <ProtectorasSection />
            </main>
            <Footer />
        </AdminProvider>
    );
}

export default Admin;