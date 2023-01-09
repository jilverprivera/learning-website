export type LayoutContextTypes = {
  bannerRef : any
  // currentBanner: HTMLElement | null;
  openFlyout: boolean;
  showSearch: boolean;
  menuOpen: boolean;
  categorySearch: string | null;
  productSelected: number | null;

  setOpenFlyout: (arg: boolean) => void;
  setShowSearch: (arg: boolean) => void;
  setMenuOpen: (arg: boolean) => void;
  setCategorySearch: (arg: string) => void;
  setProductSelected: (arg: number | null) => void;
};
