import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { signUp } from "../../store/session";
import "./SignupFormModal.css";

function SignupFormModal() {
	const dispatch = useDispatch();
	const [formData, setFormData] = useState({
		email: "",
		username: "",
		description: "",
		// picture: "",
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
		// formDataToSend.append("picture", formData.picture || "")
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
	console.log("this is our frontend form data!!!!", formData)

	return (
		<div className="signup-container">
			<h1>Sign Up</h1>
			<form onSubmit={handleSubmit}>
				<ul>
					{errors.map((error, idx) => (
						<li key={idx}>{error}</li>
					))}
				</ul>
				<h3>Email</h3>
				<input
					type="text"
					className="form-input-signup"
					value={formData.email}
					onChange={(e) => setFormData({ ...formData, email: e.target.value })}
				/>

				<h3>Username</h3>
				<input
					type="text"
					className="form-input-signup"
					value={formData.username}
					onChange={(e) => setFormData({ ...formData, username: e.target.value })}
				/>
				<h4>Tell us about yourself... Your interests, hobbies, passion for trivia, etc.</h4>
				<textarea
					className="form-input-signup-des"
					value={formData.description}
					onChange={(e) => setFormData({ ...formData, description: e.target.value })}
				/>

					<h3>Upload a profile picture</h3>
					<p>Feature coming soon!</p>
					{/* <input
						type="file"
						className="profile-upload"
						accept=".png, .jpeg, .jpg"
						onChange={(e) => setFormData({ ...formData, picture: e.target.files[0] })}
						required
					/> */}

					<h3>Password</h3>
					<input
						type="password"
						className="form-input-signup"
						value={formData.password}
						onChange={(e) => setFormData({ ...formData, password: e.target.value })}
					/>
					<h3>Confirm Password</h3>
					<input
						type="password"
						className="form-input-signup"
						value={confirmPassword}
						onChange={(e) => setConfirmPassword(e.target.value)}
					/>
					<div className="login-button-div">
				<button className="login-button" type="submit">Sign Up</button>
				</div>
			</form>
		</div>
	);
}

export default SignupFormModal;
