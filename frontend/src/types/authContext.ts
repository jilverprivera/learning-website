import { ProductType } from "./productType";

export type AuthTypes = {
  token: TokenTypes;
  user: UserType | null;
  logged: boolean;
  staff: boolean;
  admin: boolean;
  loading: boolean;
  cartTotal: number;

  setLoading: (arg: boolean) => void;

  addToWishList: (arg: ProductType) => void;
  signInUser: (arg: SignInTypes) => void;
  signOut: () => void;
  
};

export type TokenTypes = {
  access: string | null;
  refresh: string | null;
};

export type SignInTypes = {
  email: string;
  password: string;
};

export type UserType = {
  email: string;
  exp: number;
  first_name: string;
  image: string;
  is_active: boolean;
  is_staff: boolean;
  is_superuser: boolean;
  jti: string;
  last_name: string;
  token_type: string;
  user_id: number;
};
