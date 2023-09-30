import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { decksSelector } from "../../store/decks";
import { useSelector, useDispatch } from 'react-redux';
import { useHistory, useParams, useLocation } from "react-router-dom";
import * as deckActions from "../../store/decks"
import "./CategoryPage.css"



function Category(){
const history = useHistory();
const location = useLocation();
const category = location.search.split("=")[1]
const dispatch = useDispatch();
const decks = useSelector(decksSelector)
const deckIds = Object.keys(decks || {});

const handleBack = () => {
    history.push(`/`)
}

useEffect(() => {
    dispatch(deckActions.fetchDecksCategory(category))
}, [dispatch])
if(deckIds.length && category === "General%20Knowledge"){
    return(
        <>
            <h1 className="category-title">General Knowledge:</h1>
        <div className="cat-card-container">
           {deckIds.map((deckId) => {
            const deck = decks[deckId];
            const redirectToDeck = async (e) => {
                history.push(`/decks/${deckId}`)
            }
            if (!deck){
                return null
            }
            return(
            <div className="outer" onClick={redirectToDeck}>
            <div className="cat-card">
                <h2>{deck.title}</h2>
            </div>
            </div>
            )

           })}
        </div>
        </>
    )

} else if(deckIds.length) {
    return(
        <>
            <h1 className="category-title">{category}:</h1>
        <div className="cat-card-container">
           {deckIds.map((deckId) => {
            const deck = decks[deckId];
            const redirectToDeck = async (e) => {
                history.push(`/decks/${deckId}`)
            }
            if (!deck){
                return null
            }
            return(
                <div className="outer" onClick={redirectToDeck}>
                <div className="cat-card">
                    <h2>{deck.title}</h2>
                </div>
                </div>
            )

           })}
        </div>
        </>
    )
} else {
    return (
        <>
        <h1>No Decks created for this Category yet!</h1>
        <button className="login-button" onClick={handleBack}>Home</button>
        </>

    )


}
}

export default Category
