
export const SET_DECKS = "decks/SET_DECKS"

export const decksSelector = (state) => {
    return state.decks
}

const setDecks = (decks) => ({
    type: SET_DECKS,
    decks
})



// Fetch all decks
export const fetchDecks = () => async (dispatch) => {
    const res = await fetch("/api/decks/")
    const data = await res.json();
    dispatch(setDecks(data.decks))
    return data
}

// Fectch all decks by category
export const fetchDecksCategory = (cat) => async (dispatch) => {
    const res = await fetch(`/api/decks/deck_category?category=${cat}`)
    const data = await res.json();
    console.log("this is our data from our fetch", data)
    dispatch(setDecks(data.decks))
    return data
}


// const initialState = {
//     decks: null
// }

// reducer
const decksReducer = (state = {}, action) => {
    switch(action.type){
        case SET_DECKS:
            const newState = {}
            action.decks.forEach(deck => newState[deck.id] = deck);
            return newState

        default:
            return state;
    }
}

export default decksReducer;
