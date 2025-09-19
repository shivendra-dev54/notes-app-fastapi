import { Link } from "react-router";
import { useAuthStore } from "../lib/AuthStore";

export default function Navbar() {

  const { user } = useAuthStore();

  return (
    <nav className="bg-black border-b border-gray-800 text-white">
      <div className="max-w-6xl mx-auto px-6 py-4 flex justify-between items-center">
        <Link to="/" className="text-2xl font-bold">
          NotesApp
        </Link>

        <div className="flex gap-6">

          {(!user) && (
            <>
              <Link to="/sign-in" className="hover:text-gray-400">
                Sign In
              </Link>
              <Link to="/sign-up" className="hover:text-gray-400">
                Sign Up
              </Link>
            </>
          )}

          {(user) && (
            <Link to="/main" className="hover:text-gray-400">
              Main
            </Link>
          )}
        </div>
      </div>
    </nav>
  );
}
