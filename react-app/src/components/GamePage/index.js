import { useParams, useHistory } from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";
import { useEffect, useState } from "react";
import { useModal, openModal } from "../../context/Modal";
import * as deckActions from "../../store/decks"
import * as questionActions from "../../store/questions"
import shuffle from "../../helpers/shuffle";
import "./GamePage.css"
import OpenModalButton from "../OpenModalButton";
import Completion from "../CompletionModal";
import CorrectAnswer from "../CorrectAnswerModal";
import IncorrectAnswer from "../IncorrectAnswerModal";
import * as sessionActions from "../../store/session";



function GamePage() {
    const { deckId } = useParams();
    const history = useHistory();
    const { setModalContent } = useModal()
    const dispatch = useDispatch();
    const questions = useSelector(questionActions.deckQuestionsSelector)
    const questionIds = Object.keys(questions || {})
    const user = useSelector(state => state.session.user)
    const [right, setRight] = useState(false)
    const [correct, setCorrect] = useState(0)
    const [rightQuest, setRightQuest] = useState(null)
    const [wrongQuest, setWrongQuest] = useState(null)
    const [answerModal, setAnswerModal] = useState(false)
    const [wrong, setWrong] = useState(0)
    const [disable, setDisable] = useState(false)
    const [questionIndex, setquestionIndex] = useState(0);
    let answersArray = []
    let num = Math.floor(Math.random() * 3)

    useEffect(() => {
        dispatch(deckActions.fetchDetails(deckId))
            .then(dispatch(questionActions.fetchDeckQuestions(deckId)))
    }, [dispatch])

    useEffect(() => {
        if(rightQuest){
            dispatch(sessionActions.createCorrectAnswer(user.id, rightQuest))
        }
    }, [rightQuest])

    useEffect(() => {
        if(wrongQuest){
            dispatch(sessionActions.createIncorrectAnswer(user.id, wrongQuest))
        }
    }, [wrongQuest])

    if (questionIds.length) {
        //  Key into the current question
        const currentQuestion = questions[questionIds[questionIndex]]
        // const incorrect = currentQuestion.incorrect_answers.split(', ');
        answersArray = currentQuestion.incorrect_answers.split(', ');

        // Put all answers together and randomize them
        answersArray.splice(num, 0, currentQuestion.correct_answer)
        // answersArray.push(currentQuestion.correct_answer)

        console.log("THIS IS THE CURRENT rightAnswerQuestion", rightQuest)
        console.log("THIS IS THE CURRENT wrongAnswerQuestion", wrongQuest)
        const handleAnswer = async (e, answer) => {
            const clickedButton = e.target
            setDisable(true)
            let tempCorrect = 0
            let tempWrong = 0
            // Compare current question's correct answer with selected answer
            if (currentQuestion.correct_answer === answer) {
                setCorrect(correct + 1)
                setRightQuest(currentQuestion)
                tempCorrect += 1
                clickedButton.classList.add("correct");
                setModalContent(<CorrectAnswer answer={answer} />)
            } else {
                setWrong(wrong + 1)
                setWrongQuest(currentQuestion)
                tempWrong += 1
                clickedButton.classList.add("wrong");
                setModalContent(<IncorrectAnswer answer={answer} />)

            }
            // Move to the next question after timeout
            const timeout = await setTimeout(() => {
                clickedButton.classList.remove("correct", "wrong")
                setDisable(false)
                if (questionIndex < questionIds.length - 1) {
                    setquestionIndex(questionIndex + 1);
                } else {
                    //  When reaching end of questions open completion page
                    setModalContent(<Completion correct={correct + tempCorrect} wrong={wrong + tempWrong} deckId={deckId} />)
                    history.push(`/decks/${deckId}`)
                }
                // return () => clearTimeout(timeout)

            }, 1000)
        };

        if (questionIds.length === 0) {
            return <div>Loading...</div>;
        }

        if (questionIndex <= questionIds.length - 1) {
            return (
                <div className="t-card-container">
                    <div className="trivia-card">
                        <div className="card-top">
                            <h2 className="question-num">Question #{questionIndex + 1}</h2>
                            <h2>Difficulty: {currentQuestion.difficulty}</h2>
                        </div>
                        <h4 className="quest">{currentQuestion.question}</h4>
                        <div className="answers-container">
                            {!answersArray[0] ? (<></>)
                                : (
                                    <button className="answer" disabled={disable} id="answer1" onClick={(e) => handleAnswer(e, answersArray[0])}>
                                        {answersArray[0]}
                                    </button>
                                )}
                            {!answersArray[1] ? (<></>)
                                : (
                                    <button className="answer" disabled={disable} id="answer2" onClick={(e) => handleAnswer(e, answersArray[1])}>
                                        {answersArray[1]}
                                    </button>
                                )}
                            {!answersArray[2] ? (<></>)
                                : (
                                    <button className="answer" disabled={disable} id="answer3" onClick={(e) => handleAnswer(e, answersArray[2])}>
                                        {answersArray[2]}
                                    </button>
                                )}
                            {!answersArray[3] ? (<></>)
                                : (
                                    <button className="answer" disabled={disable} id="answer4" onClick={(e) => handleAnswer(e, answersArray[3])}>
                                        {answersArray[3]}
                                    </button>
                                )}
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


    } else {
        const handleHomeClick = async () => {
            history.push('/')
        }
        const handleDeckClick = async () => {
            history.push(`/decks/${deckId}`)
        }
        return (
            <>
                <h1>This deck has no questions yet!</h1>
                <button className="login-button" onClick={handleHomeClick}>Take Me Home</button>
                <button className="login-button" onClick={handleDeckClick}>Return to Deck</button>
            </>

        )
    }
}

export default GamePage
