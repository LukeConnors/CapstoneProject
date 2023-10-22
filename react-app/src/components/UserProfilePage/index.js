import React, { useState, useEffect } from "react";
import { decksSelector } from "../../store/decks";
import { useSelector, useDispatch } from 'react-redux';
import { useHistory, useParams, useLocation } from "react-router-dom";
import * as deckActions from "../../store/decks"
import * as questionActions from "../../store/questions"
import * as userActions from "../../store/session"
import "./UserProfilePage.css"
import ChatModal from "../ChatModal"
import OpenModalButton from "../OpenModalButton";

function UserProfile() {
    const history = useHistory();
    const dispatch = useDispatch();
    const {userId} = useParams()
    const user = useSelector(state => state.session.detailedUser)
    const correctAnswers = useSelector(state => state.session.correct)
    const incorrectAnswers = useSelector(state => state.session.incorrect)


    useEffect(() => {
        dispatch(userActions.getUserDetails(userId))
        dispatch(userActions.fetchCorrectAnswers(userId))
        dispatch(userActions.fetchIncorrectAnswers(userId))
    }, [dispatch])


        if(!user){
            return(
                <>
                <h1>Loading...</h1>
                </>
            )
        }
        return (
            <div className="profile-container">
                <h1>{user.username}</h1>
                <div className="profile-des">
                    <h3>{user.description}</h3>
                    {user.picture ? (
                        <img className="profile-pic" src={user.picture} />
                    ) : (
                        <img className="profile-pic" src="https://res.cloudinary.com/dyt7uoeck/image/upload/v1695947352/noprofile-removebg_r8qryg.png" />
                    )}
                </div>
                <OpenModalButton
                className="chat-button"
                buttonText={"Message"}
                modalComponent={<ChatModal recipientId={user.id} name={user.username}/>} />
            </div>
        )

}

export default UserProfile
