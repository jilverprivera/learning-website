import { useLocation } from "react-router";

import AppRouter from "./routes/AppRouter";
import Footer from "./components/layout/Footer";
import Navbar from "./components/layout/Navbar";

const App = () => {
  const { pathname } = useLocation();
  return (
    <>
      {!pathname.includes("sign-in") && !pathname.includes("sign-up") && (
        <Navbar />
      )}
      <main className='w-full bg-white'>
        <AppRouter />
      </main>
      {/* {!pathname.includes("sign-in") && !pathname.includes("sign-up") && (
        <Footer />
      )} */}
    </>
  );
};

export default App;
