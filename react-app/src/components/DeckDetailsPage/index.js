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
import EditReview from "../EditReviewModal";
import DeleteReview from "../DeleteReviewModal";

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

    const handleProfileClick = (userId) => {
        history.push(`/users/${userId}`)
    }

    if (currentUser === null) {
        history.push('/login')
    }
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
                    const stars = [];
                    const review = reviews[reviewId];
                    for (let i = 0; i < review.stars; i++) {
                        stars.push(<i class="fa-solid fa-star"></i>)
                    }
                    return (
                        <div className="review-card">
                            <div className="review-head-div">
                                <div className="stars-div">
                                    {stars}
                                </div>
                                {review.user.picture && review.user.id !== currentUser.id ? (
                                    <img onClick={() => handleProfileClick(review.user.id)} className="review-pic" src={review.user.picture} />
                                ) : (
                                    <></>
                                )}
                                {!review.user.picture && review.user.id !== currentUser.id ? (
                                    <img onClick={() => handleProfileClick(review.user.id)} className="review-pic" src="https://res.cloudinary.com/dyt7uoeck/image/upload/v1695947352/noprofile-removebg_r8qryg.png" />
                                ) : (
                                    <></>
                                )}
                                {review.user.picture && review.user.id === currentUser.id ? (
                                    <img className="my-pic" src={review.user.picture} />
                                ) : (
                                    <></>
                                )}
                                {!review.user.picture && review.user.id === currentUser.id ? (
                                    <img className="review-pic" src="https://res.cloudinary.com/dyt7uoeck/image/upload/v1695947352/noprofile-removebg_r8qryg.png" />
                                ) : (
                                    <></>
                                )}
                            </div>

                            <h4>{review?.description}</h4>
                            <h3> - {review.user.username}</h3>
                            {currentUser && currentUser.id === review.user_id ? (
                                <div className="rev-button-container">
                                    <OpenModalButton
                                        buttonText="Edit Review"
                                        modalComponent={<EditReview review={review} reviewId={review?.id} />}
                                    />
                                    <OpenModalButton
                                        buttonText="Delete Review"
                                        modalComponent={<DeleteReview review={review} reviewId={review?.id} />}
                                    />
                                </div>
                            ) : (
                                <></>
                            )}
                        </div>
                    )
                })}
            </div>
        </div>
    )
}

export default DeckDetails
