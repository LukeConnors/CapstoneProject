import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useModal } from "../../context/Modal";
import { useHistory } from 'react-router-dom'
import "./Completion.css"
import OpenModalButton from "../OpenModalButton";
import AddReview from "../AddReviewModal";


function Completion({ correct, wrong, deckId }) {
    const history = useHistory()
    const { closeModal } = useModal()
    const user = useSelector(state => state.session.user)

    const handleClick = () => {
        history.push(`/`)
        closeModal()
    }
    return (
        <div className="com-answers-container">
            <h1>COMPLETE!</h1>
            <div className="com-correct-answers">
                <h1 className="com-title">Correct:</h1>
                <div className="com-right-answer-num">
                    <h1>{correct}</h1>
                </div>
            </div>
            <div className="com-incorrect-answers">
                <h1 className="com-title">Incorrect:</h1>
                <div className="com-wrong-answer-num">
                    <h1>{wrong}</h1>
                </div>
            </div>
            <div className="completion-buttons-div">
                <button className="login-button" onClick={handleClick}>Return Home</button>
                {user ? (
                    <OpenModalButton
                        buttonText={"Leave a Review"}
                        modalComponent={<AddReview />}
                    />
                ) : (
                    <></>
                )}
            </div>
        </div>
    )

}

export default Completion
