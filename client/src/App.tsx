import { Routes, Route } from "react-router";
import Navbar from "./components/Navbar";
import SignUpPage from "./pages/SignUpPage";
import SignInPage from "./pages/SignInPage";
import MainPage from "./pages/MainPage";
import HomePage from "./pages/Homepage";

function App() {
  return (
      <div className="flex flex-col min-h-screen bg-black">
        <Navbar />
        <main className="flex-grow">
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/sign-up" element={<SignUpPage />} />
            <Route path="/sign-in" element={<SignInPage />} />
            <Route path="/main" element={<MainPage />} />
          </Routes>
        </main>
      </div>
  );
}

export default App;
