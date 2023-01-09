export const checkToken = () => {
  const token = localStorage.getItem("token") || "";
  return JSON.parse(token);
};
