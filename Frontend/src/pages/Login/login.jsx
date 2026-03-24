import { useState } from "react";
import {useNavigate} from "react-router-dom";
import "./login.css";


function Login() {

    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError]=useState("");
    const navigate=useNavigate();

    const handleLogin = async () => {
        try {
            const response = await fetch("http://127.0.0.1:8000/auth/login", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    email,
                    password
                }),
            });
            const data = await response.json();
            console.log("Login Response:", data);
            if (data.access_token) {
                localStorage.setItem("token", data.access_token);
                navigate("/home");
            }
            else {
                setError("Invalid Credentials")
            }
        } catch (error) {
            setError("Something went Wrong")
        }
    };
    return (
        

        <div className="login-container">
            
            <div className="login-card">
                <div classname="error-card">{error}</div>
                <h1 className="login-main-title">AI-RESUME-ANALYZER</h1>
                <h2 className="login-title">Login</h2>
                <div className="login-form-group">
                    <label>Email:</label>
                    <input
                        placeholder="Email"
                        autoComplete="new-email"
                        onChange={(e) => setEmail(e.target.value)}
                    />
                </div>
                <div className="login-form-group">
                    <label>Password:</label>
                    <input
                        type="password"
                        placeholder="password"
                        autoComplete="new-password"
                        onChange={(e) => setPassword(e.target.value)}
                    />
                </div>
                <button className="login-btn" onClick={handleLogin}>Login</button>
                <p className="login-footer-text">Don't have a Account? 
                    <span className="signup-link" onClick={()=>navigate("/signup")}>Signup</span></p>
            </div>
        </div>
    );
}

export default Login;