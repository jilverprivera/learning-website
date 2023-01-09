import { AnimatePresence, motion } from "framer-motion";
import { layout } from "../../types/layout";

const Container = ({ children, title }: layout) => {
  document.title = title;

  return (
    <AnimatePresence mode='wait' initial={false}>
      <motion.main
        initial={{ opacity: 0, y: 10 }}
        animate={{ opacity: 1, y: 0 }}
        exit={{ opacity: 0, y: 10 }}
        transition={{ duration: 0.25 }}
        className='mx-auto w-full'
      >
        {children}
      </motion.main>
    </AnimatePresence>
  );
};

export default Container;
