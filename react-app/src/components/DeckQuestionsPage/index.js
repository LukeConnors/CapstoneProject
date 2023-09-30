import { useParams, useHistory } from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";
import { useEffect, useState } from "react";
import * as deckActions from "../../store/decks"
import * as userActions from "../../store/session"
import * as questionActions from "../../store/questions"
import OpenModalButton from "../OpenModalButton";
import AddQuestion from "../AddQuestionModal";
import "./DeckQuestions.css"


function DeckQuestionsPage() {
    const { deckId } = useParams();
    const history = useHistory();
    const dispatch = useDispatch();
    const deckOwner = useSelector(userActions.userSelector)
    const currentUser = useSelector(state => state.session.user)
    const deckQuestions = useSelector(questionActions.deckQuestionsSelector)
    const dqIds = Object.keys(deckQuestions || {});

    useEffect(() => {
        dispatch(questionActions.fetchDeckQuestions(deckId))
    }, [dispatch])

    const handleReturnClick = () => {
        history.push(`/decks/${deckId}`)
    }

    return (
        <div className="question-card-container">
            <button onClick={handleReturnClick}>Return to deck</button>
            {dqIds.map((dqId) => {
                const deckQuestion = deckQuestions[dqId]
                console.log("deck question!!!!!!!", deckQuestion)
                const handleRemoveClick = async () => {
                   await dispatch(questionActions.removeDeckQuestion(deckId, deckQuestion?.id))
                }
                if (!deckQuestion) {
                    return (
                        null
                    )
                } else {
                    return (
                        <div className="question-card">
                            <h3>{deckQuestion.question}</h3>
                            <p>Question difficulty: {deckQuestion.difficulty}</p>
                            <div className="c-answer-container">
                                <h4>Correct answer:</h4>
                                <p>{deckQuestion.correct_answer}</p>
                            </div>
                            <div className="i-answer-container">
                                <h4>Incorrect answer(s):</h4>
                                <p>{deckQuestion.incorrect_answers}</p>
                            </div>
                            <button onClick={handleRemoveClick}>Remove question</button>

                        </div>
                    )
                }
            })}
            <h3>Add a Question</h3>
            <OpenModalButton
                buttonText={"+"}
                modalComponent={<AddQuestion deckId={deckId} />}
            />
        </div>

    )


}


export default DeckQuestionsPage
