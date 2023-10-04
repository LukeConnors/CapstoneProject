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
    const [existing, setExisting] = useState(false)
    console.log("this is the existing status", existing)
    const reviews = useSelector(state => state.reviews)
    const reviewIds = Object.keys(reviews || {})
    const user = useSelector(state => state.session.user)

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
                {reviewIds.map((reviewId) => {
                    const review = reviews[reviewId];
                    if (user && review.userId === user.id) {
                        setExisting(true)
                    }
                })}
                {existing === false && user ? (
                    <OpenModalButton
                        buttonText={"Leave a Review"}
                        modalComponent={<AddReview deckId={deckId} />}
                    />
                ) : (
                    <>
                    </>
                )}
            </div>
        </div>
    )

}

export default Completion
