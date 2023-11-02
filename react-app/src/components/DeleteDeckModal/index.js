import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { useHistory } from 'react-router-dom'
import * as deckActions from "../../store/decks"
import "./DeleteDeck.css"



function DeleteDeck({deck, deckId}){
    const {closeModal} = useModal();
    const [deleted, setDeleted] = useState(false);
    const dispatch = useDispatch();
    const history = useHistory();

    const handleCancel = () => {
        closeModal()
    }

    const handleDelete = async (e) => {
        await dispatch(deckActions.removeDeck(deckId))
        setDeleted(true)
    }

    useEffect(() => {
        if (deleted) {
          const timeout = setTimeout(() => {
            history.push(`/my_profile/my_decks`)
            closeModal();
          }, 1500);

          return () => clearTimeout(timeout);
        }
      }, [deleted, closeModal]);

    return (
        <div className="delete-modal">
            {deleted ? (
                <>
                <h1>Deleted Successfully!</h1>
                </>
            ) : (
            <>
            <h1>Are you sure you want to delete your Deck?</h1>
            <div className="delete-deck-btn">
                <button className="cancel-btn" onClick={handleCancel}>Cancel</button>
                <button className="delete-btn" onClick={handleDelete}>
                    Delete
                </button>

            </div>
            </>
            )}
        </div>
    )

}

export default DeleteDeck;
