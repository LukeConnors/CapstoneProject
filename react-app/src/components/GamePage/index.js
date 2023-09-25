import { useParams, useHistory } from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";
import { useEffect } from "react";
import * as deckActions from "../../store/decks"

function GamePage(){
const {deckId} = useParams();
const dispatch = useDispatch();

useEffect (() => {
    dispatch(deckActions.fetchDeckQuestions(deckId))
}, [dispatch])

}

export default GamePage
