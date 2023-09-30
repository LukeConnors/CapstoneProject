import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect } from "react-router-dom";
import { signUp } from "../../store/session";
import './SignupForm.css';

function SignupFormPage() {
  const dispatch = useDispatch();
  const sessionUser = useSelector((state) => state.session.user);
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [description, setDescription] = useState("")
  const [picture, setPicture] = useState("")
  const [confirmPassword, setConfirmPassword] = useState("");
  const [errors, setErrors] = useState([]);

  if (sessionUser) return <Redirect to="/" />;

  const handleSubmit = async (e) => {
    const formData = new FormData()
    formData.append("username", username)
    formData.append("email", email)
    formData.append("description", description)
    formData.append("picture", picture)
    formData.append("password", password)
    e.preventDefault();
    let formErrors = {};
    if(!formData.username){
      formErrors.username = "Username is required"
     }
     if(!formData.description){
      formErrors.description = "Please provide a description about yourself"
     }
     if (Object.keys(formErrors).length > 0){
       setErrors(formErrors);
       return;
   }
    if (password === confirmPassword) {
        const data = await dispatch(signUp(formData.username, formData.email, formData.description, formData.picture, formData.password));
        if (data) {
          setErrors(data)
        }
    } else {
        setErrors(['Confirm Password field must be the same as the Password field']);
    }
  };

  return (
    <>
      <h1>Sign Up</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Email
          <input
            type="text"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </label>

         <h3>Username</h3>
          <div className="errors">{errors?.username}</div>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
        <h3>Tell us about yourself... Your interests, hobbies, passion for trivia, etc.</h3>
          <div className="errors">{errors?.description}</div>
          <input
            type="text"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
          />
        <label>
          Upload a profile picture
          <input
            type="file"
            accept=".png, .jpeg, .jpg"
            onChange={(e) => setPicture(e.target.files[0])}
          />
        </label>
        <label>
          Password
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </label>
        <label>
          Confirm Password
          <input
            type="password"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
          />
        </label>
        <button type="submit">Sign Up</button>
      </form>
    </>
  );
}

export default SignupFormPage;
