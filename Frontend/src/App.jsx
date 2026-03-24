import { Routes,Route } from "react-router-dom";
import Login from "./pages/Login/login";
import Signup from "./pages/SignUp/signup";
import Home from "./pages/Home/home";
function App(){
  return(
    <Routes>
      <Route path="/" element={<Login />}/>
      <Route path="/signup" element={<Signup />}/>
      <Route path="/home" element={<Home />}/>
    </Routes>
  );
}

export default App;