import { Navigate } from "react-router-dom";
import { useAuth } from "../hooks/useAuth";

export default function ProtectedRoute({ children, allowedRoles }) {
  const { user } = useAuth();
  if (!user || !allowedRoles.includes(user.role)) {
    return <Navigate to="/login" />;
  }
  return children;
}
