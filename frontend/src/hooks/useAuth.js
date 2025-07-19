import { useState, useEffect } from "react";

export function useAuth() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    const token = localStorage.getItem("access_token");
    if (token) {
      // Decode JWT to get user info (role, id, etc.)
      const payload = JSON.parse(atob(token.split(".")[1]));
      setUser({ id: payload.sub, role: payload.role });
    }
  }, []);

  const login = (token) => {
    localStorage.setItem("access_token", token);
    const payload = JSON.parse(atob(token.split(".")[1]));
    setUser({ id: payload.sub, role: payload.role });
  };

  const logout = () => {
    localStorage.removeItem("access_token");
    setUser(null);
  };

  return { user, login, logout };
}
