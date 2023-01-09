import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router-dom";

import reportWebVitals from "./reportWebVitals";
import { LayoutProvider } from "./context/LayoutContext";
import { AuthProvider } from "./context/AuthContext";

import App from "./App";

import "./index.css";

const root = ReactDOM.createRoot(
  document.getElementById("root") as HTMLElement
);
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <AuthProvider>
        <LayoutProvider>
          <App />
        </LayoutProvider>
      </AuthProvider>
    </BrowserRouter>
  </React.StrictMode>
);
reportWebVitals();
