import React, { useState, useEffect } from "react";
import { decksSelector } from "../../store/decks";
import { useSelector, useDispatch } from 'react-redux';
import { useHistory, useParams, useLocation } from "react-router-dom";
import * as deckActions from "../../store/decks"
import * as questionActions from "../../store/questions"
import * as userActions from "../../store/session"
import OpenModalButton from "../OpenModalButton";
import EditDeck from "../EditDeckModal";
import EditQuestion from "../EditQuestionModal";
import DeleteDeck from "../DeleteDeckModal";
import DeleteQuestion from "../DeleteQuestionModal";
import "./MyProfile.css"

function MyProfile() {
    const history = useHistory();
    const dispatch = useDispatch();
    const decks = useSelector(decksSelector)
    const questions = useSelector(questionActions.questionsSelector)
    const deckIds = Object.keys(decks || {});
    const questionIds = Object.keys(questions || {});
    const user = useSelector(state => state.session.user)
    useEffect(() => {
        dispatch(deckActions.fetchUserDecks())
        dispatch(questionActions.fetchMyQuestions())
    }, [dispatch])


    if (deckIds.length) {
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
                <div className="data-container">
                    <div className="decks-div">
                        <h1>Your decks:</h1>
                        {deckIds.map((deckId) => {
                            const deck = decks[deckId];
                            const redirectToDeck = async (e) => {
                                history.push(`/decks/${deckId}`)
                            }
                            return (
                                <div className="profile-deck">
                                    <h4 className="profile-deck-title" onClick={redirectToDeck}>{deck.title}</h4>
                                    <div className="deck-buttons-div">
                                    <OpenModalButton
                                        buttonText={"Edit Deck"}
                                        modalComponent={<EditDeck deck={deck} deckId={deck?.id} />}
                                    />
                                    <OpenModalButton
                                        buttonText={"Delete Deck"}
                                        modalComponent={<DeleteDeck deck={deck} deckId={deck?.id} />}
                                    />
                                    </div>
                                </div>
                            )
                        })}
                    </div>
                    <div className="questions-div">
                        <h1>Your Questions:</h1>
                        {questionIds.map((questionId) => {
                            const question = questions[questionId]
                            if (question !== undefined) {
                                return (
                                    <div className="profile-question">
                                        <h4>{question.question}</h4>
                                        <div className="question-buttons-div">
                                        <OpenModalButton
                                            buttonText={"Edit Question"}
                                            modalComponent={<EditQuestion question={question} questionId={question?.id} />}
                                        />
                                        <OpenModalButton
                                            buttonText={"Delete Question"}
                                            modalComponent={<DeleteQuestion question={question} questionId={question?.id} />}
                                        />
                                        </div>
                                    </div>
                                )
                            } else {
                                return (
                                    <>
                                    </>
                                )
                            }

                        })}
                    </div>
                </div>
            </div>
        )
    } else {
        return (
            <div className="profile-container">
                <h1>{user.username}</h1>
                <h3>{user.description}</h3>
                <h1>Your Questions:</h1>
                {questionIds.map((questionId) => {
                    const question = questions[questionId]
                    if (question !== undefined) {
                        return (
                            <div className="profile-question">
                                <h4>{question.question}</h4>
                                <OpenModalButton
                                    buttonText={"Edit Question"}
                                    modalComponent={<EditQuestion question={question} questionId={question?.id} />}
                                />
                                <OpenModalButton
                                    buttonText={"Delete Question"}
                                    modalComponent={<DeleteQuestion question={question} questionId={question?.id} />}
                                />
                            </div>
                        )
                    } else {
                        return (
                            <>
                            </>
                        )
                    }

                })}
            </div>

        )

    }

}

export default MyProfile
