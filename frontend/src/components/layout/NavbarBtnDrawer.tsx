import { useContext } from "react";
import { LayoutContext } from "../../context/LayoutContext";

const NavbarBtnDrawer = () => {
  const { menuOpen, setMenuOpen } = useContext(LayoutContext);
  return (
    <div
      className='h-9 w-9 rounded-md flex items-center justify-center z-50 cursor-pointer'
      onClick={() => setMenuOpen(!menuOpen)}
    >
      <div
        className={`before:duration-300 after:duration-300 relative w-full h-1 ${
          !menuOpen
            ? "before:content[]  before:absolute before:w-full before:h-0.5 before:bg-zinc-900 before:dark:bg-zinc-900 before:-translate-y-1 after:content[] after:absolute after:right-0 after:w-10/12 after:bg-zinc-900 after:dark:bg-zinc-900 after:h-0.5 after:translate-y-1"
            : "before:content[]  before:absolute before:w-full before:h-0.5 before:bg-zinc-900 before:dark:bg-zinc-900 before:-rotate-45 after:content[] after:absolute after:w-full after:bg-zinc-900 after:dark:bg-zinc-900 after:h-0.5 after:rotate-45"
        }`}
      />
    </div>
  );
};

export default NavbarBtnDrawer;
