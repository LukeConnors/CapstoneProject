import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { signUp } from "../../store/session";
import "./SignupForm.css";

function SignupFormModal() {
	const dispatch = useDispatch();
	const [formData, setFormData] = useState({
		email: "",
		username: "",
		description: "",
		picture: "",
		password: ""
	  });
	const [confirmPassword, setConfirmPassword] = useState("");
	const [errors, setErrors] = useState([]);
	const { closeModal } = useModal();

	const handleSubmit = async (e) => {
		const formDataToSend = new FormData()
		formDataToSend.append("username", formData.username)
		formDataToSend.append("email", formData.email)
		formDataToSend.append("description", formData.description)
		formDataToSend.append("picture", formData.picture)
		formDataToSend.append("password", formData.password)
		e.preventDefault();
		if (formData.password === confirmPassword) {
			const data = await dispatch(signUp(formData));
			if (data) {
				setErrors(data);
			} else {
				closeModal();
			}
		} else {
			setErrors([
				"Confirm Password field must be the same as the Password field",
			]);
		}
	};

	console.log("!!!!!!!!!!!", formData)
	return (
		<>
			<h1>Sign Up</h1>
			<form onSubmit={handleSubmit}>
				<ul>
					{errors.map((error, idx) => (
						<li key={idx}>{error}</li>
					))}
				</ul>
				<label>
					Email
					<input
						type="text"
						value={formData.email}
						onChange={(e) => setFormData({...formData, email: e.target.value})}
						required
					/>
				</label>
				<label>
					Username
					<input
						type="text"
						value={formData.username}
						onChange={(e) => setFormData({...formData, username: e.target.value})}
						required
					/>
				</label>
				<label>
          Tell us about yourself... Your interests, hobbies, passion for trivia, etc.
          <input
            type="text"
            value={formData.description}
            onChange={(e) => setFormData({...formData, description: e.target.value})}
            required
          />
        </label>
        <label>
          Upload a profile picture
          <input
            type="file"
            accept=".png, .jpeg, .jpg"
            onChange={(e) => setFormData({...formData, picture: e.target.files[0]})}
            required
          />
        </label>
				<label>
					Password
					<input
						type="password"
						value={formData.password}
						onChange={(e) => setFormData({...formData, password: e.target.value})}
						required
					/>
				</label>
				<label>
					Confirm Password
					<input
						type="password"
						value={confirmPassword}
						onChange={(e) => setConfirmPassword(e.target.value)}
						required
					/>
				</label>
				<button type="submit">Sign Up</button>
			</form>
		</>
	);
}

export default SignupFormModal;
