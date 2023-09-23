import React from 'react';
import { NavLink } from 'react-router-dom';
import { useSelector } from 'react-redux';
import ProfileButton from './ProfileButton';
import './Navigation.css';

function Navigation({ isLoaded }){
	const sessionUser = useSelector(state => state.session.user);

	return (
		<div className='nav-bar'>
				<NavLink exact to="/">Home</NavLink>
			{isLoaded && (
					<ProfileButton user={sessionUser} />
			)}
		<div className='new-deck-div'>
		{sessionUser ? (
          <NavLink className="start-deck" exact to="/new_deck">
            Create a deck
          </NavLink>
        ) : (
          <NavLink exact to="/login" className="start-deck">
            Create a deck
          </NavLink>
        )}
		</div>
		</div>
	);
}

export default Navigation;
