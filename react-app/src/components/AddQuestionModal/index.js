import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useModal } from "../../context/Modal";
import { useHistory, useParams } from 'react-router-dom'
import * as questionActions from "../../store/questions"
import * as deckActions from "../../store/decks"
import * as userActions from "../../store/session"
import "./AddQuestionModal.css"


function AddQuestion({ deckId }) {
    const dispatch = useDispatch();
    const [buttonDis, setButtonDis] = useState(false)
    const [buttonText, setButtonText] = useState("Add to Deck")
    const [added, setAdded] = useState(0)
    const deckOwner = useSelector(userActions.userSelector)
    const questions = useSelector(questionActions.questionsSelector)
    const deckQuestions = useSelector(state => state.questions.deckQuestions)
    const deckQuestionIds = Object.keys(deckQuestions || {})
    const questionIds = Object.keys(questions || {})
    useEffect(() => {
        dispatch(questionActions.fetchQuestions())
        .then(dispatch(questionActions.fetchDeckQuestions(deckId)))
    }, [dispatch])

    useEffect(() => {
        dispatch(questionActions.fetchDeckQuestions(deckId))
    }, [dispatch, added])

    deckQuestionIds.forEach(id => {
        if (questionIds.includes(id)) {
            questionIds.splice(questionIds.indexOf(id), 1)
        }
    });
    return (
        <>
            <div className="add-q-title">
                <h1>Add a question to your Deck:</h1>
            </div>
            <div className="q-card-container">
                {questionIds.map((questionId) => {
                    const question = questions[questionId]
                    const handleAddClick = async (e) => {
                        setAdded(added + 1)
                        await dispatch(questionActions.createDeckQuestion(deckId, question))
                    }
                    if (question.question) {
                        return (
                            <div className="add-q-card">
                                <h3>{question.question}</h3>
                                <p>Difficulty: {question.difficulty}</p>
                                <p>Answers: {question.correct_answer}, {question.incorrect_answers}</p>
                                <p>Category: {question.category}</p>
                                <button className="login-button" disabled={buttonDis} onClick={handleAddClick}>{buttonText}</button>
                            </div>
                        )
                    }
                })}

            </div>
        </>
    )

}

export default AddQuestion;
