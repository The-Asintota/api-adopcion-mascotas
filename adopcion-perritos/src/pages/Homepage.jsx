import React from "react";
import Header from "../components/Header/Header";
import InicioSection from "../components/InicioSection/InicioSection";
import AdoptionSection from "../components/AdoptionSection/AdoptionSection";
import ProtectorasSection from "../components/ProtectorasSection/ProtectorasSection";
import AboutUs from "../components/AboutUs/AboutUs";
import Footer from "../components/Footer/Footer";

const Homepage = () => {
  return (
    <>
      <Header />
      <main>
        <InicioSection />
        <AdoptionSection />
      </main>
      <ProtectorasSection />
      <AboutUs />
      <Footer />
    </>
  );
};

export default Homepage;
