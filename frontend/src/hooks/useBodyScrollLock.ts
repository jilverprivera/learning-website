import { useState, useEffect } from "react";

export const useBodyScrollLock = () => {
  const bodyStyle = document.body.style;

  const [isLocked, setIsLocked] = useState(bodyStyle.overflowY === "hidden");

  useEffect(() => {
    bodyStyle.overflowY = isLocked ? "hidden" : "auto";
  }, [isLocked, bodyStyle]);

  const toggle = () => setIsLocked(!isLocked);

  return { isLocked, toggle };
};
