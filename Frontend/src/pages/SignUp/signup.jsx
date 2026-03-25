import {useState} from "react";
import {useNavigate} from "react-router-dom";
import "./signup.css";

function Signup(){
    const[username,setUsername]=useState("");
    const[email,setEmail]=useState("");
    const[password,setPassword]=useState("");
    const navigate=useNavigate();
    const API_URL=import.meta.env.VITE_API_URL;

    const handleSignup = async () => {
        try{
            const response= await fetch(`${API_URL}/auth/signup`,{
                method:"POST",
                headers:{
                    "Content-Type":"application/json"
                },
                body: JSON.stringify({
                    username,
                    email,
                    password
                }),
            });
            const data = await response.json();
            console.log("Signup Response:",data);
            alert("SignUp Sucessfully");
        }catch(error){
            console.error("Error:",error);
        }
    };
    return(
        
        <div className="signup-container">
            <div className="signup-card">
                <h2 className="signup-main-title">AI-RESUME-ANALYZER</h2>
            <h1 className="signup-title">SignUp</h1>

            <div className='signup-form-group'>
                <label>Username:</label>
                <input
                placeholder="Username"
                autoComplete="new-username"
                onChange={(e)=>setUsername(e.target.value)}
                />
            </div>

            <div className='signup-form-group'>
                <label>Email:</label>
                <input
                placeholder="Email"
                autoComplete="new-email"
                onChange={(e)=>setEmail(e.target.value)}
                />
            </div>
            <div className='signup-form-group'>
                <label>Password:</label>
                <input
                placeholder="Password"
                type="password"
                autoComplete="new-password"
                onChange={(e)=>setPassword(e.target.value)}
                />
            </div>
            <button className="signup-btn" onClick={handleSignup}>Signup</button>
            <p className="signup-footer-text">Already have a Account?<span className="login-link" onClick={()=>navigate("/")}>Login</span></p>
        </div>
        </div>
        
    );
}
export default Signup;