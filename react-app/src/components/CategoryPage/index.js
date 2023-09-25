import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { decksSelector } from "../../store/decks";
import { useSelector, useDispatch } from 'react-redux';
import { useHistory, useParams, useLocation } from "react-router-dom";
import * as deckActions from "../../store/decks"



function Category(){
const history = useHistory();
const location = useLocation();
const category = location.search.split("=")[1]
const dispatch = useDispatch();
const decks = useSelector(decksSelector)
const deckIds = Object.keys(decks || {});

useEffect(() => {
    dispatch(deckActions.fetchDecksCategory(category))
}, [dispatch])
if(deckIds.length){
    return(
        <div className="card-container">
           {deckIds.map((deckId) => {
            const deck = decks[deckId];
            const redirectToDeck = async (e) => {
                history.push(`/decks/${deckId}`)
            }
            if (!deck){
                return null
            }
            return(
            <div className="cat-card">
                <h1 onClick={redirectToDeck}>{deck.title}</h1>
            </div>
            )

           })}
        </div>
    )

} else {
    return (
        <>
        <h1>No Decks created for this Category yet!</h1>
        </>

    )


}
}

export default Category
