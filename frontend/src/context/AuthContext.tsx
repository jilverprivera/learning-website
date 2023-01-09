import { createContext, useEffect, useState } from "react";
import jwt_decode from "jwt-decode";

import type {
  AuthTypes,
  SignInTypes,
  TokenTypes,
  UserType,
} from "../types/authContext";
import type { childrenProps } from "../types/layout";
import { checkToken } from "../helpers/checkToken";
import { ProductType } from "../types/productType";

const AuthContext = createContext({} as AuthTypes);

export const AuthProvider = ({ children }: childrenProps) => {
  const [token, setToken] = useState<TokenTypes>({
    access: null,
    refresh: null,
  });
  const [user, setUser] = useState<UserType | null>(null);
  const [loading, setLoading] = useState<boolean>(false);
  const [logged, setLogged] = useState<boolean>(false);
  const [staff, setStaff] = useState<boolean>(false);
  const [admin, setAdmin] = useState<boolean>(false);
  const [cart, setCart] = useState<any[]>([]);
  const [cartTotal, setCartTotal] = useState<number>(0);
  const [wishList, setWishList] = useState<any[]>([]);

  useEffect(() => {
    const authToken: TokenTypes = checkToken();
    if (authToken) {
      setToken({ access: authToken.access, refresh: authToken.refresh });
    }
  }, []);

  useEffect(() => {
    if (token.access) {
      const data: UserType = jwt_decode(token.access);
      data.is_staff && data.is_superuser ? setAdmin(true) : setAdmin(false);
      data.is_staff ? setStaff(true) : setStaff(false);
      setUser(data);
      setLogged(true);
    } else {
      setUser(null);
      setStaff(false);
      setAdmin(false);
      setLogged(false);
    }
  }, [token]);

  const signInUser = async (values: SignInTypes) => {
    setLoading(true);
    await fetch("http://127.0.0.1:8000/auth/token/", {
      method: "POST",
      body: JSON.stringify({ ...values }),
      headers: { "Content-type": "application/json; charset=UTF-8" },
    })
      .then((resp): Promise<TokenTypes> => resp.json())
      .then((data) => {
        setToken({ access: data.access, refresh: data.refresh });
        localStorage.setItem("token", JSON.stringify(data));
        if (token.access) {
          const userData: UserType = jwt_decode(token.access);
          userData.is_staff ? setStaff(true) : setStaff(false);
          userData.is_staff && userData.is_superuser
            ? setAdmin(true)
            : setAdmin(false);
          setUser(userData);
          setLogged(true);
        } else {
          setUser(null);
          setStaff(false);
          setAdmin(false);
          setLogged(false);
        }
      });
    setLoading(false);
  };

  const signOut = () => {
    localStorage.removeItem("token");
    setUser(null);
    setToken({
      access: null,
      refresh: null,
    });
    setCart([]);
    setWishList([]);
    setCartTotal(0);
    setStaff(false)
    setAdmin(false);
    setLogged(false);
  };

  const addToWishList = async (product: ProductType) => {
    if (logged && !admin) {
      const checkWishList = wishList?.every((item: ProductType) => {
        return item.uuid !== product.uuid;
      });
      if (checkWishList) {
        setWishList([...wishList, { ...product }]);
        //TODO: change fetch request url
        await fetch("/api/users/wish_list", {
          method: "PATCH",
          headers: { "Content-type": "application/json; charset=UTF-8" },
          body: JSON.stringify({ wishlist: [...wishList, { ...product }] }),
        });
      }
    }
  };

  useEffect(() => {
    const getTotal = () => {
      const total = cart.reduce((total, el) => {
        return total + el.price * el.quantity;
      }, 0);
      setCartTotal(total);
    };
    getTotal();
  }, [cart]);

  const state = {
    token,
    user,
    logged,
    staff,
    admin,
    loading,
    cartTotal,

    setLoading,

    addToWishList,
    signInUser,
    signOut,
  };
  return <AuthContext.Provider value={state}>{children}</AuthContext.Provider>;
};

export default AuthContext;
