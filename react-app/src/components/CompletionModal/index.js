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
    let existing = false
    const deck = useSelector(state => state.decks.detailedDeck)
    const reviews = useSelector(state => state.reviews)
    const reviewIds = Object.keys(reviews || {})
    const user = useSelector(state => state.session.user)

    reviewIds.forEach((reviewId) => {
        const review = reviews[reviewId];
        if (user && review?.user_id === user.id) {
           existing = true
        }
    })

    const handleClick = () => {
        history.push(`/`)
        closeModal()
    }

    const handleClose = () => {
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
                <button className="login-button" onClick={handleClose}>Close</button>
                {!existing && user && user.id !== deck.user_id ? (
                    <div className="com-rev-button">
                    <OpenModalButton
                        buttonText={"Leave a Review"}
                        modalComponent={<AddReview deckId={deckId} />}
                    />
                    </div>
                ) : (
                    <>
                    </>
                )}
            </div>
        </div>
    )

}

export default Completion
