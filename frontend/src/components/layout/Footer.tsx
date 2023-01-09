import React from "react";

const Footer = () => {
  return (
    <footer className='w-full bg-zinc-800'>
      <div className='w-11/12 mx-auto grid grid-cols-4 py-16'>
        <div className='col-span-2 flex flex-col- items-start justify-start'>
          <p className='text-zinc-50 font-medium text-3xl'>LOGO</p>
        </div>
        <div className='aspect-square flex flex-col- items-start justify-center'>
          <p className='text-zinc-50 font-medium text-lg'>Information</p>
        </div>
        <div className=''>
          <p className='text-zinc-50 font-medium text-lg'>Customer service</p>
        </div>
      </div>
      <div className='w-full mx-auto flex items-center justify-between border-t-2 border-zinc-700 py-12'></div>
    </footer>
  );
};

export default Footer;
