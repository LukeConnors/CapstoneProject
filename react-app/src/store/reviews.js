export const SET_REVIEWS = "reviews/SET_REVIEWS"
export const ADD_REVIEW = "reviews/ADD_REVIEW"
export const UPDATE_REVIEW = "reviews/UPDATE_REVIEW"
export const DELETE_REVIEW = "reviews/DELETE_REVIEW"




const setReviews = (reviews) => ({
    type: SET_REVIEWS,
    reviews
})

const addReview = (deckId, review) => ({
    type: ADD_REVIEW,
    payload: review
})

const updateReview = (review) => ({
    type: UPDATE_REVIEW,
    payload: review
})

const deleteReview = (reviewId) => ({
    type: DELETE_REVIEW,
    payload: reviewId
})


export const fetchReviews = (deckId) => async (dispatch) => {
    try{
        const res = await fetch(`/api/decks/${deckId}/reviews`)
        const data = await res.json();
        dispatch(setReviews(data.reviews))
        return data
    } catch(e){
        console.log("THIS IS OUR ERROR", e)
        throw e
    }
}

const reviewsReducer = (state = {}, action) => {
    let newState = {}
    switch (action.type){
        case SET_REVIEWS:
                action.reviews.forEach(review => newState[review.id] = review);
            return newState
        default:
            return state
    }
}


export default reviewsReducer;
