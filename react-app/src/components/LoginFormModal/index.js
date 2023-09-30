import React, { useState } from "react";
import { login } from "../../store/session";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import "./LoginForm.css";

function LoginFormModal() {
  const dispatch = useDispatch();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState([]);
  const { closeModal } = useModal();

  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data) {
      setErrors(data);
    } else {
        closeModal()
    }
  };

  return (
    <div className="login-container">
      <h1>Log In</h1>
      <form onSubmit={handleSubmit}>
        <ul>
          {errors.map((error, idx) => (
            <li key={idx}>{error}</li>
          ))}
        </ul>


          <h3>Email</h3>
          <input
          className="form-input-login"
            type="text"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        <div>
        <h3>Password</h3>
          <input
          className="form-input-login"
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <div className="login-button-div">
        <button className="login-button" type="submit">Log In</button>
        </div>
      </form>
    </div>
  );
}

export default LoginFormModal;
