import React, { useState, useEffect, useRef } from "react";
import { useDispatch } from "react-redux";
import { useHistory } from 'react-router-dom'
import { logout, login } from "../../store/session";
import OpenModalButton from "../OpenModalButton";
import LoginFormModal from "../LoginFormModal";
import SignupFormModal from "../SignupFormModal";
import "./Navigation.css"

function ProfileButton({ user }) {
  const dispatch = useDispatch();
  const history = useHistory();
  const [showMenu, setShowMenu] = useState(false);
  const ulRef = useRef();

  const handleDemo = () => {
    const email = "demo@aa.io";
    const password = "password";
    dispatch(login(email, password));
    setShowMenu(false);
  };

  const openMenu = () => {
    if (showMenu) return;
    setShowMenu(true);
  };

  useEffect(() => {
    if (!showMenu) return;

    const closeMenu = (e) => {
      if (!ulRef.current.contains(e.target)) {
        setShowMenu(false);
      }
    };

    document.addEventListener("click", closeMenu);

    return () => document.removeEventListener("click", closeMenu);
  }, [showMenu]);

  const handleLogout = (e) => {
    e.preventDefault();
    history.push('/')
    dispatch(logout());
  };

  const handleProfile = (e) => {
    e.preventDefault();
    history.push("/my_profile")
  }

  const ulClassName = "profile-dropdown" + (showMenu ? "" : " hidden");
  const closeMenu = () => setShowMenu(false);

  return (
    <>
      <button onClick={openMenu}>
        <i className="fas fa-user-circle" />
      </button>
      <ul className={ulClassName} ref={ulRef}>
        {user ? (
          <div className="login-signup">
            <li>{user.username}</li>
            <li>{user.email}</li>
              <button onClick={handleProfile}>My Profile</button>
              <button onClick={handleLogout}>Log Out</button>
          </div>
        ) : (
          <>
          <div className="login-signup">
            <OpenModalButton
              className="profile-button"
              buttonText="Log In"
              onItemClick={closeMenu}
              modalComponent={<LoginFormModal />}
            />
            <OpenModalButton
              className="profile-button"
              buttonText="Sign Up"
              onItemClick={closeMenu}
              modalComponent={<SignupFormModal />}
            />

            <button onClick={handleDemo}>Demo User</button>
            </div>
          </>
        )}
      </ul>
    </>
  );
}

export default ProfileButton;
