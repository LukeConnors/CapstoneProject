import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { useHistory } from 'react-router-dom'
import "./Completion.css"


function Completion({ correct, wrong, deckId }) {
    const history = useHistory()
    const { closeModal } = useModal()

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
            <button className="login-button" onClick={handleClick}>Return Home</button>
        </div>
    )

}

export default Completion
