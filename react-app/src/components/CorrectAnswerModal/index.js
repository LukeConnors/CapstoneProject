import { useModal } from "../../context/Modal";
import "./CorrectAnswerModal.css"

function CorrectAnswer(answer){
const {closeModal} = useModal()
    const nextQueston = async () => {
        closeModal()
    }
return(
    <div className="answer-div">
        <h1 className="correct-h1">CORRECT!</h1>
        {/* <h2>You answered : {answer}</h2> */}
        <button className="answer-button" onClick={nextQueston}>Next Question</button>
    </div>
)
}

export default CorrectAnswer
