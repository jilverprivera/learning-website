import { useContext } from "react";
import { Link, useLocation } from "react-router-dom";

import { LayoutContext } from "../../context/LayoutContext";

import { navLinkTypes } from "../../types/layout";

const NavLink = ({ route, icon, title, extras, last, first }: navLinkTypes) => {
  const { pathname } = useLocation();
  const {setOpenFlyout} = useContext(LayoutContext);

  return (
    <Link
      to={route}
      onClick={() => setOpenFlyout(false)}
      className={` text-sm flex items-center justify-center
      ${first && "ml-0"}
      ${last ? "mr-0" : "mx-6"} 
      ${pathname === route
          ? "font-medium text-gray-50"
          : "font-normal text-gray-300"
      }`}
    >
      {icon && <span>{icon}</span>}
      <span className='mx-1.5'>{title}</span>
      {extras && <span>{extras}</span>}
    </Link>
  );
};

export default NavLink;
