import { Navigate } from "react-router-dom";

type Props = {
  component: React.ComponentType;
};

export const PrivateRoute = ({ component: RouteComponent }: Props) => {
  const isLogged = true;
  if (isLogged) {
    return <RouteComponent />;
  }

  if (isLogged) {
    return <div>Don't have permissions</div>;
  }

  return <Navigate to='/sign-in' />;
};
