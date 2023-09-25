import React from 'react';
import { NavLink } from 'react-router-dom';
import { useSelector } from 'react-redux';
import ProfileButton from './ProfileButton';
import './Navigation.css';

function Navigation({ isLoaded }){
	const sessionUser = useSelector(state => state.session.user);

	return (
		<div className='nav-bar'>
				{sessionUser ? (
					<>
				  <NavLink className="start-deck" exact to="/new_deck">
					Create a deck
				  </NavLink>
				  <NavLink className="start-question" exact to="new_question">
					Create a question
				  </NavLink>
				  <NavLink className="logo-div" exact to="/">
					<img className='logo' alt='trivia titan' src="https://res.cloudinary.com/dyt7uoeck/image/upload/v1695649988/triviaTitan-removebg_znpboe.png"></img>
				  </NavLink>
				  </>
				) : (
					<>
				  <NavLink exact to="/login" className="start-deck">
					Create a deck
				  </NavLink>
				<NavLink className="start-question" exact to="/login">
				Create a question
				</NavLink>
				<NavLink className="logo-div" exact to="/">
				<img className='logo' alt='trivia titan' src="https://res.cloudinary.com/dyt7uoeck/image/upload/v1695649988/triviaTitan-removebg_znpboe.png"></img>
				</NavLink>
				</>
				)}
				<NavLink className="home-button" exact to="/">Home</NavLink>
			{isLoaded && (
					<ProfileButton user={sessionUser} />
			)}
		</div>
	);
}

export default Navigation;
