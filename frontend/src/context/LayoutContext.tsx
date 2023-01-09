import { createContext, useState, useRef } from 'react';
import { childrenProps } from '../types/layout';
import { LayoutContextTypes } from '../types/layoutContext';

export const LayoutContext = createContext({} as LayoutContextTypes);

export const LayoutProvider = ({ children }: childrenProps) => {
  const bannerRef = useRef<any>(null);
  const [showSearch, setShowSearch] = useState<boolean>(false);
  const [menuOpen, setMenuOpen] = useState<boolean>(false);
  const [openFlyout, setOpenFlyout] = useState<boolean>(false);

  const [categorySearch, setCategorySearch] = useState<string | null>(null);
  const [productSelected, setProductSelected] = useState<number | null>(null);

  const state = {
    bannerRef,
    openFlyout,
    showSearch,
    menuOpen,
    categorySearch,
    productSelected,

    setShowSearch,
    setOpenFlyout,
    setMenuOpen,
    setCategorySearch,
    setProductSelected,
  };
  return <LayoutContext.Provider value={state}>{children}</LayoutContext.Provider>;
};
