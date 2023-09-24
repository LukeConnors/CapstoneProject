import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useModal } from "../../context/Modal";
import { useHistory, useParams } from 'react-router-dom'
import * as questionActions from "../../store/questions"
import * as deckActions from "../../store/decks"
import * as userActions from "../../store/session"


function AddQuestion({deckId}){
const dispatch = useDispatch();
const [buttonDis, setButtonDis] = useState(false)
const [buttonText, setButtonText] = useState("Add to Deck")
const deckOwner = useSelector(userActions.userSelector)
const questions = useSelector(questionActions.questionsSelector)
const questionIds = Object.keys(questions || {})
useEffect(() => {
    dispatch(questionActions.fetchQuestions())
}, [dispatch])


return (
    <div>
    {questionIds.map((questionId) => {
        const question = questions[questionId]
        const handleAddClick = async (e) => {
            await dispatch(deckActions.createDeckQuestion(deckId, question))
            await dispatch(deckActions.fetchDeckQuestions(deckId))
        }
        return (
            <div className="add-q-card">
                <h3>{question.question}</h3>
                <p>Difficulty: {question.difficulty}</p>
                <p>Answers: {question.correct_answer}, {question.incorrect_answers}</p>
                <button disabled={buttonDis} onClick={handleAddClick}>{buttonText}</button>
            </div>
        )
    })}

    </div>
)

}

export default AddQuestion;
