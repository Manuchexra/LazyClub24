import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Navigation from "./components/navigation";
import Lesson from "./components/Lessons/lesson"; // Lesson komponentini import qilib oling
import { Header } from "./components/header";
import { Features } from "./components/features";
import { About } from "./components/about";
import { Gallery } from "./components/gallery";
import { Testimonials } from "./components/testimonials";
import { Team } from "./components/Team";
import { Contact } from "./components/contact";
import Register from './components/register';
import Login from './components/login';
import ResetPass from './components/resetpass';
import ResetPasswordConfirm from './components/resetpasscon';
import ActivateAccountForm from './components/activation';
import UserPanel from './components/userpanel';
import JsonData from "./data/data.json";
import SmoothScroll from "smooth-scroll";
import Spinner from './components/Spinner';
import Warning from './components/warning';
import "./App.css";

export const scroll = new SmoothScroll('a[href*="#"]', {
  speed: 500,
  speedAsDuration: true,
});

const App = () => {
  const [landingPageData, setLandingPageData] = React.useState({});
  const [loading, setLoading] = React.useState(true); 

  React.useEffect(() => {
    setTimeout(() => {
      setLandingPageData(JsonData);
      setLoading(false);
    }, 2000);
  }, []);

  if (loading) {
    return <Spinner />;
  }

  return (
    <div>
      <Navigation />
      <Routes>
        <Route path="/" element={<Header data={landingPageData.Header} />} />
        <Route path="/features" element={<Features data={landingPageData.Features} />} />
        <Route path="/about" element={<About data={landingPageData.About} />} />
        <Route path="/gallery" element={<Gallery data={landingPageData.Gallery} />} />
        <Route path="/testimonials" element={<Testimonials data={landingPageData.Testimonials} />} />
        <Route path="/team" element={<Team data={landingPageData.Team} />} />
        <Route path="/contact" element={<Contact data={landingPageData.Contact} />} />
        <Route path="/register" element={<Register />} />
        <Route path="/login" element={<Login />} />
        <Route path="/reset-password" element={<ResetPass />} />
        <Route path="/password/reset/confirm/:uid/:token" element={<ResetPasswordConfirm />} />
        <Route path="/auth/activate/:uid/:token" element={<ActivateAccountForm />} />
        <Route path="/user-panel" element={<UserPanel />} />
        <Route path="/checkout" element={<Warning />} />
        <Route path="/lessons" element={<Lesson />} /> {/* Lesson komponentini rota qo'shing */}
      </Routes>
    </div>
  );
};

export default App;
