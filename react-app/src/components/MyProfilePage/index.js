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
    const correctAnswers = useSelector(state => state.session.correct)
    const incorrectAnswers = useSelector(state => state.session.incorrect)
    const correctIds = Object.keys(correctAnswers || {})
    const incorrectIds = Object.keys(incorrectAnswers || {})



    useEffect(() => {
        dispatch(userActions.fetchCorrectAnswers(user.id))
        dispatch(userActions.fetchIncorrectAnswers(user.id))
        dispatch(deckActions.fetchUserDecks())
        dispatch(questionActions.fetchMyQuestions())
    }, [dispatch])

    if (!user) {
        history.push('/login')
    }
// Create object to hold category data
    const correctCategories = {
        "General Knowledge": 0, "Entertainment: Books": 0, "Entertainment: Film": 0,
        "Entertainment: Music": 0, "Entertainment: Musicals & Theatres": 0, "Entertainment: Television": 0,
        "Entertainment: Video Games": 0, "Entertainment: Board Games": 0, "Science & Nature": 0,
        "Science: Computers": 0, "Science: Mathematics": 0, "Mythology": 0, "Sports": 0,
        "Geography": 0, "History": 0, "Politics": 0, "Art": 0, "Celebrities": 0, "Animals": 0
    }
// Create object to hold category data
    const incorrectCategories = {
        "General Knowledge": 0, "Entertainment: Books": 0, "Entertainment: Film": 0,
        "Entertainment: Music": 0, "Entertainment: Musicals & Theatres": 0, "Entertainment: Television": 0,
        "Entertainment: Video Games": 0, "Entertainment: Board Games": 0, "Science & Nature": 0,
        "Science: Computers": 0, "Science: Mathematics": 0, "Mythology": 0, "Sports": 0,
        "Geography": 0, "History": 0, "Politics": 0, "Art": 0, "Celebrities": 0, "Animals": 0
    }


    const correctUnique = []
    const incorrectUnique = []
// Create forEach loop on the IDs to track how many questions were answered correctly and add them to object, also add unique answers to array
    correctIds.forEach(correctId => {
        const correctAnswer = correctAnswers[correctId]
        correctCategories[correctAnswer.question.category] += 1
        if(!correctUnique.includes(correctAnswer.question_id)){
            correctUnique.push(correctAnswer.question_id)
        }
    })
// Create forEach loop on the IDs to track how many questions were answered incorrectly and add them to object, also add unique answers to array
    incorrectIds.forEach(incorrectId => {
        const incorrectAnswer = incorrectAnswers[incorrectId]
        incorrectCategories[incorrectAnswer.question.category] += 1
        if(!incorrectUnique.includes(incorrectAnswer.question_id)){
            incorrectUnique.push(incorrectAnswer.question_id)
        }
    })

// create function to calculate the percentage of correct answers for each category, if it is greater than 0, return the percentage, if not return 0
    function calculateCategoryStats(correctCategories, incorrectCategories, category) {
        const correctCount = correctCategories[category] || 0;
        const incorrectCount = incorrectCategories[category] || 0;
        const total = correctCount + incorrectCount;
        return total > 0 ? ((correctCount / total) * 100).toFixed(2) : 0;
    }

console.log(correctUnique)

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
                <div className="middle-div">
                    <div className="buffer-div">
                        <h1>Your Badges:</h1>
                        <div className="badges-div">
                            {correctCategories["General Knowledge"] >= 5 ? (
                                <div className="badge-div">
                                    <img className="badge" src="https://res.cloudinary.com/dyt7uoeck/image/upload/v1697671493/gen5badge-removebg_lhlffz.png" />
                                    <span className='tool-tip-text'>Answer 5 General Knowledge questions correctly</span>
                                </div>
                            ) : (
                                <></>
                            )}
                        </div>
                    </div>
                    <div className="buffer-div">
                        <h1>Your Stats:</h1>
                        <div className="stats-div">
                        <div className="stat-div">
                                <h3>Total Unique Correct Answers:</h3>
                                <h4>{correctUnique.length}</h4>
                            </div>
                            <div className="stat-div">
                                <h3>Total Unique Incorrect Answers:</h3>
                                <h4>{incorrectUnique.length}</h4>
                            </div>
                            <div className="stat-div">
                                <h3>Total Correct Answers:</h3>
                                <h4>{correctIds.length}</h4>
                            </div>
                            <div className="stat-div">
                                <h3>Total Incorrect Answers:</h3>
                                <h4>{incorrectIds.length}</h4>
                            </div>
                            {/* map the categories and create elements to hold data calculated by the helper function */}
                            {Object.keys(correctCategories).map((category) => {
                                const genStats = calculateCategoryStats(correctCategories, incorrectCategories, category);
                                if (correctCategories[category] && incorrectCategories[category] >= 1) {
                                    return (
                                        <div className="stat-div" key={category}>
                                            <h3>{category}:</h3>
                                            <h4>{`${genStats}% Correct`}</h4>
                                        </div>
                                    );
                                }
                                return null;
                            })}
                        </div>
                    </div>
                </div>
                <div className="questions-div">
                    <h1>Your Questions:</h1>
                    {questionIds.map((questionId) => {
                        const question = questions[questionId]
                        if (question === undefined) {
                            return (
                                <>
                                </>
                            )
                        } else {
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
                        }

                    })}
                </div>
            </div>
        </div>
    )

}

export default MyProfile
