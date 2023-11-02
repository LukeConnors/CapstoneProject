import React, { useState, useEffect } from "react";
import { decksSelector } from "../../store/decks";
import { useSelector, useDispatch } from 'react-redux';
import { useHistory, useParams, useLocation } from "react-router-dom";
import * as deckActions from "../../store/decks"
import * as questionActions from "../../store/questions"
import * as userActions from "../../store/session"
import "./MyProfile.css"

function MyProfile() {
    const history = useHistory();
    const dispatch = useDispatch();
    const user = useSelector(state => state.session.user)
    const correctAnswers = useSelector(state => state.session.correct)
    const incorrectAnswers = useSelector(state => state.session.incorrect)
    const correctIds = Object.keys(correctAnswers || {})
    const incorrectIds = Object.keys(incorrectAnswers || {})

    if (user === null) {
        history.push('/login')
    }

    useEffect(() => {
        dispatch(userActions.fetchCorrectAnswers(user.id))
        dispatch(userActions.fetchIncorrectAnswers(user.id))
        dispatch(deckActions.fetchUserDecks())
        dispatch(questionActions.fetchMyQuestions())
    }, [dispatch])

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
        if (!correctUnique.includes(correctAnswer.question_id)) {
            correctUnique.push(correctAnswer.question_id)
        }
    })
    // Create forEach loop on the IDs to track how many questions were answered incorrectly and add them to object, also add unique answers to array
    incorrectIds.forEach(incorrectId => {
        const incorrectAnswer = incorrectAnswers[incorrectId]
        incorrectCategories[incorrectAnswer.question.category] += 1
        if (!incorrectUnique.includes(incorrectAnswer.question_id)) {
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

    if (user !== null) {
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
                        <button className="deck-button" onClick={() => history.push('/my_profile/my_decks')}>Your Decks</button>
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
                                    <div>
                                        <h2>None</h2>
                                    </div>
                                )}
                            </div>
                        </div>
                        <div className="buffer-div">
                            <h1>Your Stats:</h1>
                            <div className="stats-div">
                                <div className="answer-stat-div">
                                    <div className="stat-div">
                                        <h3>Total Unique Correct Answers:</h3>
                                        <h4 className="answer-num-correct">
                                            {correctUnique.length}
                                        </h4>
                                    </div>
                                    <div className="stat-div">
                                        <h3>Total Unique Incorrect Answers:</h3>
                                        <h4 className="answer-num-incorrect">
                                            {incorrectUnique.length}
                                        </h4>
                                    </div>
                                    <div className="stat-div">
                                        <h3>Total Correct Answers:</h3>
                                        <h4 className="answer-num-correct">
                                            {correctIds.length}
                                        </h4>
                                    </div>
                                    <div className="stat-div">
                                        <h3>Total Incorrect Answers:</h3>
                                        <h4 className="answer-num-incorrect">
                                            {incorrectIds.length}
                                        </h4>
                                    </div>
                                </div>
                                <div className="cat-stat-div">
                                    {Object.keys(correctCategories).map((category) => {
                                        const genStats = calculateCategoryStats(correctCategories, incorrectCategories, category);
                                        if (correctCategories[category] && incorrectCategories[category] >= 1) {
                                            return (
                                                <div className="stat-div" key={category}>
                                                    <h3>{category}:</h3>
                                                    <h4>{`${genStats}% Correct`}</h4>
                                                    <progress className="bar" value={genStats} max={100}></progress>
                                                </div>
                                            );
                                        }
                                        return null;
                                    })}
                                </div>
                            </div>
                        </div>
                    </div>
                    <div className="questions-div">
                        <button className="question-button" onClick={() => history.push('/my_profile/my_questions')}>Your Questions</button>
                        <img />
                    </div>
                </div>
            </div>
        )
    } else {
        return (
            <>
            </>
        )
    }

}

export default MyProfile
