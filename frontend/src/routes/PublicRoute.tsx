import { useContext } from "react";
import { Navigate } from "react-router-dom";
import AuthContext from "../context/AuthContext";

type Props = {
  component: React.ComponentType;
  path?: string;
  roles?: Array<string>;
};

const PublicRoute = ({ component: RouteComponent }: Props) => {
  const { logged } = useContext(AuthContext);

  const isLogged = false;
  if (!logged) {
    return <RouteComponent />;
  }

  if (isLogged) {
    return <div>Don't have permissions</div>;
  }

  return <Navigate to='/' />;
};

export default PublicRoute;
