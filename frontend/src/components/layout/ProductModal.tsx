import { useContext } from "react";
import { motion } from "framer-motion";

import { LayoutContext } from "../../context/LayoutContext";
import { TfiClose } from "react-icons/tfi";

const ProductModal = () => {
  const { setShowSearch } = useContext(LayoutContext);

  return (
    <motion.div
      className='w-full h-screen fixed top-0 left-0 bg-white flex flex-col items-center justify-start py-24'
      initial={{ opacity: 0, y: -24 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, y: -24 }}
      transition={{ duration: 0.25 }}
    >
      <button
        className='w-16 h-16 rounded-full border-2 flex items-center justify-center text-3xl mb-12'
        onClick={() => setShowSearch(false)}
      >
        <TfiClose />
      </button>

      <div className='max-w-screen-2xl w-11/12 mx-auto grid grid-cols-4'></div>
    </motion.div>
  );
};

export default ProductModal;
