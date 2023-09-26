import { useParams, useHistory } from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";
import { useEffect, useState } from "react";
import * as deckActions from "../../store/decks"
import * as questionActions from "../../store/questions"
import shuffle from "../../helpers/shuffle";

function GamePage(){
const {deckId} = useParams();
const history = useHistory();
const dispatch = useDispatch();
const questions = useSelector(deckActions.deckQuestionsSelector)
const questionIds = Object.keys(questions || {})
const [questionIndex, setquestionIndex] = useState(0);

console.log("THESE ARE THE QUESTIONS", questions)
console.log('THESE ARE THE QUESTION IDS', questionIds)

useEffect (() => {
    dispatch(deckActions.fetchDeckQuestions(deckId))
}, [dispatch])


//  Key into the current question
const currentQuestion = questions[questionIds[questionIndex]]
// Put all answers together and randomize them
const incorrect = currentQuestion.incorrect_answers.split(', ');
const answersArray = currentQuestion.incorrect_answers.split(', ');
answersArray.push(currentQuestion.correct_answer)
shuffle(answersArray)

const handleAnswer = (answer) => {
    // Compare current question's correct answer with selected answer
    if(currentQuestion.correct_answer ){}
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

return(
    <div>
        {currentQuestion && (
            <div className="trivia-card">
                <h2>Question #{questionIndex + 1}</h2>
                <h4>{currentQuestion.question}</h4>
                {answersArray[0] === "" ? (<></>)
                : ( <button onClick={handleAnswer}>{answersArray[0]}</button>)}
                {answersArray[1] === "" ? (<></>)
                : ( <button onClick={handleAnswer}>{answersArray[1]}</button>)}
                {answersArray[2] === "" ? (<></>)
                : ( <button onClick={handleAnswer}>{answersArray[2]}</button>)}
                {answersArray[3] === "" ? (<></>)
                : ( <button onClick={handleAnswer}>{answersArray[3]}</button>)}

            </div>
        )}
    </div>
)


}

export default GamePage
