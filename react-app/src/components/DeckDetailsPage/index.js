import { useParams, useHistory } from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";
import { useEffect, useState } from "react";
import * as deckActions from "../../store/decks"
import * as userActions from "../../store/session"
import * as questionActions from "../../store/questions"
import * as reviewActions from "../../store/reviews"
import OpenModalButton from "../OpenModalButton";
import EditDeck from "../EditDeckModal";
import DeleteDeck from "../DeleteDeckModal";
import "./DeckDetails.css"

function DeckDetails() {
    const { deckId } = useParams();
    const history = useHistory();
    const [reviewOwner, setReviewOwner] = useState([]);
    const dispatch = useDispatch();
    const deck = useSelector(deckActions.deckDetailsSelector)
    const deckOwner = useSelector(userActions.userSelector)
    const currentUser = useSelector(state => state.session.user)
    const reviews = useSelector(state => state.reviews)
    const reviewIds = Object.keys(reviews || {});
    useEffect(() => {
        dispatch(deckActions.fetchDetails(deckId))
            .then((data) => dispatch(userActions.getUserDetails(data?.user_id)))
            .then(() => { dispatch(questionActions.fetchDeckQuestions(deckId)) })
            .then(() => { dispatch(reviewActions.fetchReviews(deckId)) })
    }, [dispatch, deckId])


useEffect(() => {
    const fetchReviewOwners = async () => {
        const owners = {};
        for (const reviewId of reviewIds) {
            const review = reviews[reviewId];
            const res = await fetch(`/api/users/${review.user_id}`);
            const data = await res.json();
            owners[reviewId] = data;
        }
        setReviewOwner(owners);
    };

    fetchReviewOwners();
}, [dispatch, deckId]);

    const handleQuestionsClick = async (e) => {
        history.push(`/decks/${deckId}/questions`)
    }
    const handleStartClick = async (e) => {
        history.push(`/decks/${deckId}/play`)
    }
    console.log("this is our review owner", reviewOwner);

    return (
        <div className="details-container">
            <div className="details-title">
                <h1 className="deck-title">{deck?.title}</h1>
                <h4>Created by: {deckOwner?.username}</h4>
            </div>
            <div className="details-des">
                <h3 className="deck-description">{deck?.description}</h3>
            </div>
            {currentUser && deck?.user_id === currentUser.id ? (
                <div className="button-container">
                    <OpenModalButton
                        buttonText={"Edit Deck"}
                        className="edit-button"
                        modalComponent={<EditDeck deck={deck} deckId={deck?.id} />}
                    />
                    <OpenModalButton
                        buttonText={"Delete Deck"}
                        className="delete-button"
                        modalComponent={<DeleteDeck deck={deck} deckId={deck?.id} />}
                    />
                    <button className="view-button" onClick={handleQuestionsClick}>
                        View Deck Questions
                    </button>
                </div>
            ) : (
                <>
                </>
            )}
            <button className="start-button" onClick={handleStartClick}>Start!</button>
            <div className="reviews-container">
            {reviewIds.map((reviewId) => {
                const review = reviews[reviewId];
                const owner = reviewOwner[reviewId];
                return (
                        <div className="review-card">
                            <h4>{review?.description}</h4>
                            {/* <h2>{owner.username}</h2> */}
                        </div>
                )
            })}
            </div>
        </div>
    )
}

export default DeckDetails
