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


function GamePage() {
    const { deckId } = useParams();
    const history = useHistory();
    const {setModalContent} = useModal()
    const dispatch = useDispatch();
    const questions = useSelector(deckActions.deckQuestionsSelector)
    const questionIds = Object.keys(questions || {})
    const [correct, setCorrect] = useState(0)
    const [wrong, setWrong] = useState(0)
    const [disable, setDisable] = useState(false)
    const [questionIndex, setquestionIndex] = useState(0);



    useEffect(() => {
        dispatch(deckActions.fetchDeckQuestions(deckId))
    }, [dispatch])


    //  Key into the current question
    const currentQuestion = questions[questionIds[questionIndex]]
    // Put all answers together and randomize them
    const incorrect = currentQuestion.incorrect_answers.split(', ');
    const answersArray = currentQuestion.incorrect_answers.split(', ');
    answersArray.push(currentQuestion.correct_answer)

useEffect(() => {
shuffle(answersArray)
}, [questionIndex])


    const handleAnswer = async (e, answer) => {
        const clickedButton = e.target
        setDisable(true)
        let tempCorrect = 0
        let tempWrong = 0
        // Compare current question's correct answer with selected answer
        if (currentQuestion.correct_answer === answer) {
            setCorrect(correct + 1)
            tempCorrect += 1
            clickedButton.classList.add("correct");
        } else {
            setWrong(wrong + 1)
            tempWrong += 1
            clickedButton.classList.add("wrong");
        }
        // Move to the next question after timeout
        const timeout = setTimeout(() => {
            clickedButton.classList.remove("correct", "wrong")
            setDisable(false)
            if (questionIndex < questionIds.length - 1) {
                setquestionIndex(questionIndex + 1);
            } else {
                //  When reaching end of questions open completion page
                console.log("!!!!!!!!!", correct)
                console.log("!!!!!!!!!", wrong)
                setModalContent(<Completion correct={correct + tempCorrect} wrong={wrong + tempWrong} deckId={deckId}/>)
            }
            return () => clearTimeout(timeout)
        }, 3000)
    };

    if (questionIds.length === 0) {
        return <div>Loading...</div>;
    }

    if(questionIndex <= questionIds.length - 1){
        return (
                    <div className="trivia-card">
                        <h2>Question #{questionIndex + 1}</h2>
                        <h4>{currentQuestion.question}</h4>
                        {!answersArray[0] ? (<></>)
                            : (
                            <button disabled={disable} id="answer1" onClick={(e) => handleAnswer(e, answersArray[0])}>
                                {answersArray[0]}
                                </button>
                            )}
                        {!answersArray[1] ? (<></>)
                            : (
                            <button disabled={disable} id="answer2" onClick={(e) => handleAnswer(e, answersArray[1])}>
                                {answersArray[1]}
                                </button>
                            )}
                        {!answersArray[2] ? (<></>)
                            : (
                            <button disabled={disable} id="answer3" onClick={(e) => handleAnswer(e, answersArray[2])}>
                                {answersArray[2]}
                                </button>
                            )}
                        {!answersArray[3] ? (<></>)
                            : (
                            <button disabled={disable} id="answer4" onClick={(e) => handleAnswer(e, answersArray[3])}>
                                {answersArray[3]}
                                </button>
                            )}
            </div>
        )


    } else {
        return (
            <>
            </>
        )
    }


}

export default GamePage
