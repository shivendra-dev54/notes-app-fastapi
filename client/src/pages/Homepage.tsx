import { useCallback, useEffect } from "react";
import { Link, useNavigate } from "react-router";
import { useAuthStore } from "../lib/AuthStore";

export default function HomePage() {

  const { user } = useAuthStore();
  const navigate = useNavigate();

  const check_user_status = useCallback(async () => {
      if (user){
        navigate('/main');
      }
    }, [ navigate, user]);
  
    useEffect(() => {
      check_user_status();
    }, [check_user_status]);


  return (
    <div className="flex flex-col items-center justify-center bg-black text-white px-6">
      <div className="mt-40 text-center">
        <h1 className="text-6xl font-extrabold mb-6">NotesApp</h1>
        <p className="text-lg text-gray-400 mb-10">
          Simple. Secure. Black as void.
        </p>

        <div className="flex gap-6 justify-center">
          <Link
            to="/sign-up"
            className="px-6 py-3 bg-gray-900 border border-gray-700 rounded-lg hover:bg-gray-800 transition-colors"
          >
            Get Started
          </Link>
          <Link
            to="/sign-in"
            className="px-6 py-3 bg-gray-900 border border-gray-700 rounded-lg hover:bg-gray-800 transition-colors"
          >
            Sign In
          </Link>
        </div>
      </div>
    </div>
  );
}
