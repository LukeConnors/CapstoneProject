import React, { useState, useEffect } from "react";
import { decksSelector } from "../../store/decks";
import { useSelector, useDispatch } from 'react-redux';
import * as deckActions from "../../store/decks"
import OpenModalButton from "../OpenModalButton";
import { useHistory, useParams, useLocation } from "react-router-dom";
import EditDeck from "../EditDeckModal";
import DeleteDeck from "../DeleteDeckModal";
import "./YourDecksPage.css"

function YourDecksPage (){
    const history = useHistory();
    const dispatch = useDispatch();
    const decks = useSelector(decksSelector)
    const deckIds = Object.keys(decks || {});

    useEffect(() => {
        dispatch(deckActions.fetchUserDecks())
    }, [dispatch])

    return (
        <div className="deck-page-container">
            <div className="edit-title">
              <h1>Your Decks:</h1>
            </div>
            {deckIds.length ? (
                <>
              <button className="return" onClick={() => history.push("/my_profile")}>Return to profile</button>
              <div className="my-deck-container">
              {deckIds.map((deckId) => {
                  const deck = decks[deckId];
                  const redirectToDeck = async (e) => {
                      history.push(`/decks/${deckId}`)
                  }
                  return (
                      <div className="profile-deck">
                          <h4 className="profile-deck-title" onClick={redirectToDeck}>{deck.title}</h4>
                          <div className="deck-button-cont">
                              <div className="deck-edit-div">
                                  <OpenModalButton
                                      buttonText={"Edit Deck"}
                                      modalComponent={<EditDeck deck={deck} deckId={deck?.id} />}
                                  />
                              </div>
                              <div className="deck-delete-div">
                                  <OpenModalButton
                                      buttonText={"Delete Deck"}
                                      modalComponent={<DeleteDeck deck={deck} deckId={deck?.id} />}
                                  />
                              </div>
                          </div>
                      </div>
                  )
              })}
              </div>
              </>
            ) : (
                <>
              <button className="return" onClick={() => history.push("/my_profile")}>Return to profile</button>
              <div className="no-decks">
                  <h1>
                      No decks to display!
                  </h1>
              </div>
              </>
            )}

        </div>
    )
}

export default YourDecksPage
