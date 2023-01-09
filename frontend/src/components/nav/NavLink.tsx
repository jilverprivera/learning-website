import { useContext } from 'react';
import { Link } from 'react-router-dom';
import { LayoutContext } from '../../context/LayoutContext';
import { useWindow } from '../../hooks/useWindow';
import { navLinkType } from '../../types/layout';

const NavLink = ({ label, path, first, last }: navLinkType) => {
  const { scrollY } = useWindow();
  const { bannerRef } = useContext(LayoutContext);
  return (
    <Link
      to={path}
      className={`${
        bannerRef && scrollY > bannerRef.current?.clientHeight - 48 ? 'text-zinc-900' : 'text-white'
      } ${last ? 'mr-0' : 'mr-3'} ${first ? 'ml-0' : 'ml-3'} text-sm`}
    >
      {label}
    </Link>
  );
};

export default NavLink;
