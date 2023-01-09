import { Routes, Route, useLocation } from "react-router-dom";

import Home from "../pages/Home";

const AppRouter = () => {
  const location = useLocation();

  return (
    <Routes location={location} key={location.pathname}>
      <Route path='/' element={<Home />} />
    </Routes>
  );
};

export default AppRouter;
