import { useModal } from "../../context/Modal";
import "./IncorrectAnswerModal.css"


function IncorrectAnswer(){
    const {closeModal} = useModal()
    const nextQueston = async () => {
        closeModal()
    }
return(
    <div className="answer-div">
        <h1 className="incorrect-h1">INCORRECT!</h1>
        <button className="answer-button" onClick={nextQueston}>Next Question</button>
    </div>
)
}

export default IncorrectAnswer
