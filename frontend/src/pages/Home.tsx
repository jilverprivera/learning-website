import { useContext } from 'react';
import Container from '../components/layout/Container';
import { LayoutContext } from '../context/LayoutContext';
import PersonStudy from '../assets/person_study.svg';

const Home = () => {
  const { bannerRef } = useContext(LayoutContext);

  return (
    <Container title='Homepage - Jilver Pacheco'>
      <section
        ref={bannerRef}
        className='w-full bg-gray-800 h-screen flex items-center justify-center relative'
      >
        <div className='max-w-screen-2xl w-11/12 mx-auto py-24 relative'>
          <h1 className='sm:mx-auto sm:w-10/12 md:w-2/3 font-black text-blue-900 text-4xl text-center sm:text-5xl md:text-6xl lg:w-auto lg:text-left xl:text-7xl dark:text-white leading-relaxed'>
            Run successful remote and
            <br className='lg:block hidden' />
            <span className='relative text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-cyan-500 dark:from-blue-400 dark:to-cyan-300'>
              Hybrid teams
            </span>
            .
          </h1>
          <img
            src={PersonStudy}
            alt=''
            className=' absolute top-2/4 right-0 w-3/6 -translate-y-2/4 aspect-square'
          />
        </div>
      </section>

      <section className='w-full bg-white '>
        <div className='max-w-screen-2xl w-11/12 mx-auto py-48 flex items-center justify-center flex-col'>
          <h2 className='text-4xl font-semibold'>Now is the time to build your portfolio.</h2>
          <p className='w-2/4 text-center leading-relaxed text-lg mt-6 mb-12'>
            With typical market returns, you have to start young to secure your future. With Pocket, it’s never too late
            to build your nest egg.
          </p>
          <div className='max-w-screen-xl w-full grid grid-cols-3 gap-6'>
            <div className='border w-full h-64 rounded-lg p-6'></div>
            <div className='border w-full h-64 rounded-lg p-6'></div>
            <div className='border w-full h-64 rounded-lg p-6'></div>
            <div className='border w-full h-64 rounded-lg p-6'></div>
            <div className='border w-full h-64 rounded-lg p-6'></div>
            <div className='border w-full h-64 rounded-lg p-6'></div>
          </div>
        </div>
      </section>

      <section className='w-full bg-gray-400 py-24'>
        <div className='max-w-screen-2xl mx-auto grid grid-cols-4'>
          <div>
            <h3>Total cursos</h3>
          </div>
          <div>
            <h3>Total estudiantes</h3>
          </div>
          <div>
            <h3>Total </h3>
          </div>
        </div>
      </section>
    </Container>
  );
};

export default Home;
