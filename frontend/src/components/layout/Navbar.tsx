import { useContext } from 'react';
import { Link } from 'react-router-dom';
import { LayoutContext } from '../../context/LayoutContext';
import { useWindow } from '../../hooks/useWindow';
import Logo from '../Logo';
import NavLink from '../nav/NavLink';

const Navbar = () => {
  const { scrollY } = useWindow();
  const { bannerRef } = useContext(LayoutContext);

  return (
    <header>
      <nav
        className={` ${
          bannerRef && scrollY > bannerRef.current?.clientHeight - 48
            ? 'bg-white/90 border-gray-200'
            : 'bg-gray-800/90 border-gray-700'
        }
        fixed top-0 left-0 z-50 w-full  backdrop-blur navbar shadow-2xl shadow-gray-700/5 border-b `}
      >
        <div className='max-w-screen-2xl w-full h-20 mx-auto  flex flex-wrap items-center justify-between'>
          <Logo />
          <div className='hidden w-full flex-wrap justify-end items-center mb-16 space-y-8 p-6 border border-gray-100 rounded-3xl shadow-2xl shadow-gray-300/20 bg-white dark:bg-gray-800 lg:space-y-0 lg:p-0 lg:m-0 lg:flex md:flex-nowrap lg:bg-transparent lg:w-7/12 lg:shadow-none dark:shadow-none dark:border-gray-700 lg:border-0'>
            <NavLink
              label='Home'
              path='/'
              first={true}
            />
            <NavLink
              label='features'
              path='/features'
            />
            <NavLink
              label='Contact'
              path='/contact'
              last={true}
            />

            <div className='w-full space-y-2 border-primary/10 dark:border-gray-700 flex-col sm:flex-row lg:space-y-0 md:w-max lg:border-l pl-12 ml-12 flex items-center justify-center'>
              {/* <Link
                to='/login'
                className='relative text-sm font-medium text-white mr-6'
              >
                Sign In
              </Link> */}
              <Link
                to='/register'
                className='relative text-sm font-semibold text-white px-6 py-2 rounded-xl bg-gradient-to-r from-sky-600 to-purple-600 hover:bg-gradient-to-r hover:from-blue-600 hover:to-violet-600 duration-300'
              >
                Get started today
              </Link>
            </div>
          </div>
        </div>
      </nav>
    </header>
  );
};

export default Navbar;
