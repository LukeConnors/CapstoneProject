import React, { useState, useEffect } from "react";
import { useSelector, useDispatch } from 'react-redux';
import { useHistory } from "react-router-dom";
import EditQuestion from "../EditQuestionModal";
import * as questionActions from "../../store/questions"
import DeleteQuestion from "../DeleteQuestionModal";
import OpenModalButton from "../OpenModalButton";
import "./YourQuestionsPage.css"


function YourQuestionsPage (){
    const history = useHistory();
    const dispatch = useDispatch();
    const questions = useSelector(questionActions.questionsSelector)
    const questionIds = Object.keys(questions || {});

    useEffect(() => {
        dispatch(questionActions.fetchMyQuestions())
    }, [dispatch])


    return (
        <>
        {questionIds.length ? (
            <>
            <button className="return" onClick={() => history.push("/my_profile")}>Return to profile</button>
        <div className="my-q-container">
             {questionIds.map((questionId) => {
                            const question = questions[questionId]

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

                        })}
        </div>
        </>

        ) : (
            <>
            <button className="return" onClick={() => history.push("/my_profile")}>Return to profile</button>
            <div className="no-questions">
                <h1>
                    No questions to display
                </h1>
            </div>
            </>
        )}
        </>
    )
}

export default YourQuestionsPage
