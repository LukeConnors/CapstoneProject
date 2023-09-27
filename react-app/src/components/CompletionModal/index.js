import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { useHistory } from 'react-router-dom'


function Completion({correct, wrong, deckId}){
    const history = useHistory()
    const {closeModal} = useModal()

   const handleClick = () => {
        history.push(`/decks/${deckId}`)
        closeModal()
    }
return(
    <>
    <h1>COMPLETE!</h1>
    <h1>Correct: {correct}</h1>
    <h1>Incorrect: {wrong}</h1>
    <button onClick={handleClick}>Return to deck</button>
    </>
)

}

export default Completion
