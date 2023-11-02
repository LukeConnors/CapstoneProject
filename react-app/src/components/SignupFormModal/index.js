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
		picture: "",
		password: ""
	});
	const [confirmPassword, setConfirmPassword] = useState("");
	const [errors, setErrors] = useState([]);
	const { closeModal } = useModal();


	const validateEmail = (email) => {
		// Use a regular expression to validate the email
		return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
	  };


	const handleSubmit = async (e) => {
		e.preventDefault();
		let formErrors = {};

		if(!formData.username){
			formErrors.username = "Username is required"
		}

		if(!formData.description){
			formErrors.description = "Please provide a description about yourself"
		}

		if(!validateEmail(formData.email)){
			formErrors.email = "Please provide a valid email address";
		}
		if(!formData.password){
			formErrors.password = "Password is required"
		}

		if(!formData.picture){
			formErrors.picture = "Please upload a profile picture"
		}

		const formDataToSend = new FormData()

		formDataToSend.append("username", formData.username);
		formDataToSend.append("email", formData.email);
		formDataToSend.append("description", formData.description);
		formDataToSend.append("password", formData.password);

		if (formData.picture) {
			formDataToSend.append("picture", formData.picture);
		}

		if (formData.password === confirmPassword) {
			let data = await dispatch(signUp(formDataToSend));
			if (data) {
				setErrors(data);
			} else {
				closeModal();
			}
		} else {
			formErrors.conPassword = "Confirm Password field must be the same as the Password field"
		}

		if (Object.keys(formErrors).length > 0) {
			setErrors(formErrors);
			return;
		}

	};

	return (
		<div className="signup-container">
			<h1>Sign Up</h1>
			<form onSubmit={handleSubmit}>
				<h3>Email</h3>
				<div className="errors">{errors?.email}</div>
				<input
					type="text"
					className="form-input-signup"
					value={formData.email}
					onChange={(e) => setFormData({ ...formData, email: e.target.value })}
				/>

				<h3>Username</h3>
				<div className="errors">{errors?.username}</div>
				<input
					type="text"
					className="form-input-signup"
					value={formData.username}
					onChange={(e) => setFormData({ ...formData, username: e.target.value })}
				/>
				<h4>Tell us about yourself... Your interests, hobbies, passion for trivia, etc.</h4>
				<div className="errors">{errors?.description}</div>
				<textarea
					className="form-input-signup-des"
					value={formData.description}
					onChange={(e) => setFormData({ ...formData, description: e.target.value })}
				/>

					<h3>Upload a profile picture</h3>
					<div className="errors">{errors?.picture}</div>
					<input
						type="file"
						className="profile-upload"
						accept=".png, .jpeg, .jpg"
						onChange={(e) => setFormData({ ...formData, picture: e.target.files[0] })}
					/>

					<h3>Password</h3>
					<div className="errors">{errors?.password}</div>
					<input
						type="password"
						className="form-input-signup"
						value={formData.password}
						onChange={(e) => setFormData({ ...formData, password: e.target.value })}
					/>
					<h3>Confirm Password</h3>
					<div className="errors">{errors?.conPassword}</div>
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
