import { useParams, useHistory } from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";
import { useEffect, useState } from "react";
import * as deckActions from "../../store/decks"
import * as questionActions from "../../store/questions"
import shuffle from "../../helpers/shuffle";

function GamePage() {
    const { deckId } = useParams();
    const history = useHistory();
    const dispatch = useDispatch();
    const questions = useSelector(deckActions.deckQuestionsSelector)
    const questionIds = Object.keys(questions || {})
    const [correct, setCorrect] = useState(0)
    const [wrong, setWrong] = useState(0)
    const [questionIndex, setquestionIndex] = useState(0);

    console.log("THESE ARE THE QUESTIONS", questions)
    console.log('THESE ARE THE QUESTION IDS', questionIds)

    useEffect(() => {
        dispatch(deckActions.fetchDeckQuestions(deckId))
    }, [dispatch])


    //  Key into the current question
    const currentQuestion = questions[questionIds[questionIndex]]
    // Put all answers together and randomize them
    const incorrect = currentQuestion.incorrect_answers.split(', ');
    const answersArray = currentQuestion.incorrect_answers.split(', ');
    console.log("THESE ARE THE ANSWERS", answersArray)
    answersArray.push(currentQuestion.correct_answer)
    shuffle(answersArray)

    const handleAnswer = (e, answer) => {
        // Compare current question's correct answer with selected answer
        if (currentQuestion.correct_answer === answer) {
            setCorrect(correct + 1)

        } else {
            setWrong(wrong + 1)
        }
        // Move to the next question
        if (questionIndex < questionIds.length - 1) {
            setquestionIndex(questionIndex + 1);
            //  When reaching end of questions push to completion page
        } else {
            history.push(`/decks/${deckId}/completion_page`)
        }
    };

    if (questionIds.length === 0) {
        return <div>Loading...</div>;
    }

    return (
        <div>
            {currentQuestion && (
                <div className="trivia-card">
                    <h2>Question #{questionIndex + 1}</h2>
                    <h4>{currentQuestion.question}</h4>
                    {!answersArray[0] ? (<></>)
                        : (
                        <button onClick={(e) => handleAnswer(e, answersArray[0])}>
                            {answersArray[0]}
                            </button>
                        )}
                    {!answersArray[1] ? (<></>)
                        : (
                        <button onClick={(e) => handleAnswer(e, answersArray[1])}>
                            {answersArray[1]}
                            </button>
                        )}
                    {!answersArray[2] ? (<></>)
                        : (
                        <button onClick={(e) => handleAnswer(e, answersArray[2])}>
                            {answersArray[2]}
                            </button>
                        )}
                    {!answersArray[3] ? (<></>)
                        : (
                        <button onClick={() => handleAnswer(answersArray[3])}>
                            {answersArray[3]}
                            </button>
                        )}

                </div>
            )}
        </div>
    )


}

export default GamePage
