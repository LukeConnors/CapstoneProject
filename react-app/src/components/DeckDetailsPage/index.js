import { useParams } from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";
import { useEffect } from "react";
import * as deckActions from "../../store/decks"
import * as userActions from "../../store/session"
import OpenModalButton from "../OpenModalButton";
import EditDeck from "../EditDeckModal";
import DeleteDeck from "../DeleteDeckModal";

function DeckDetails(){
    const { deckId } = useParams();
    const dispatch = useDispatch();
    const deck = useSelector(deckActions.deckDetailsSelector)
    const deckOwner = useSelector(userActions.userSelector)
    const currentUser = useSelector(state => state.session.user)

    useEffect(() => {
        dispatch(deckActions.fetchDetails(deckId))
        dispatch(userActions.getUserDetails(deck?.user_id))
    }, [dispatch, deckId, deck?.user_id])

    return (
        <div className="details-container">
            <div className="details-title">
            <h1>{deck?.title}</h1>
            </div>
            <div className="details-des">
            <h3>{deck?.description}</h3>
            </div>
            <div>
            <h4>Created by: {deckOwner?.username}</h4>
            </div>
            {currentUser && deck?.user_id === currentUser.id ? (
                <>
                <OpenModalButton
                buttonText={"Edit Deck"}
                modalComponent={<EditDeck deck={deck} deckId={deck?.id}/>}
                 />
                 <OpenModalButton
                 buttonText={"Delete Deck"}
                 modalComponent={<DeleteDeck deck={deck} deckId={deck?.id}/>}
                  />
                  </>
            ) : (
                <>
                </>
            )}
            <button>Start</button>
        </div>
    )
}

export default DeckDetails
