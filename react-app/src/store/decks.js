
export const SET_DECKS = "decks/SET_DECKS"
export const SET_DECK_DETAILS = "decks/SET_DECK_DETAILS"
export const ADD_DECK = "decks/ADD_DECK"
export const UPDATE_DECK = "decks/UPDATE_DECK"
export const DELETE_DECK = "decks/DELETE_DECK"


export const decksSelector = (state) => {
    return state.decks
}

export const deckDetailsSelector = (state) => {
    return state.decks.detailedDeck
}


const setDecks = (decks) => ({
    type: SET_DECKS,
    decks
})

const setDeckDetails = (deck) => ({
    type: SET_DECK_DETAILS,
    deck
})


const addDeck = (deck) => ({
    type: ADD_DECK,
    payload: deck
})


const updateDeck = (deck) => ({
    type: UPDATE_DECK,
    payload: deck
})

const deleteDeck = (deckId) => ({
    type: DELETE_DECK,
    payload: deckId
})


// Fetch all decks
export const fetchDecks = () => async (dispatch) => {
    const res = await fetch("/api/decks/")
    const data = await res.json();
    dispatch(setDecks(data.decks))
    return data
}

// Fetch all decks owned by the current user
export const fetchUserDecks = () => async (dispatch) => {
    const res = await fetch("/api/decks/my_decks")
    const data = await res.json();
    dispatch(setDecks(data.decks))
    return data
}

// Fetch deck details
export const fetchDetails = (deckId) => async (dispatch) => {
    const res = await fetch(`/api/decks/${deckId}`);
    const data = await res.json();
    dispatch(setDeckDetails(data))
    return data
}


// Fetch all decks by category
export const fetchDecksCategory = (cat) => async (dispatch) => {
    const res = await fetch(`/api/decks/deck_category?category=${cat}`)
    const data = await res.json();
    dispatch(setDecks(data.decks))
    return data
}

// Create a new deck under the logged in user
export const createDeck = (payload) => async (dispatch) => {
    try {
        const res = await fetch("/api/decks/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(payload)
        })
        if(res.ok){
            const newDeck = await res.json()
            dispatch(addDeck(newDeck))
            return newDeck
        }
    } catch(e) {
        return e
    }
}


// Edit a deck with deckId
export const editDeck = (deckId, payload) => async (dispatch) => {
    try{
        const res = await fetch(`/api/decks/${deckId}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(payload)
        });
        if(res.ok){
            const editedDeck = await res.json();
            dispatch(updateDeck(editedDeck))
            return editedDeck
        }
    } catch(e){
        return e
    }

}

// Delete a deck owned by the logged in user
export const removeDeck = (deckId) => async (dispatch) => {
    const res = await fetch(`/api/decks/${deckId}`, {
        method: "DELETE"
    });
    if(res.ok){
        // const message = await res.json();
        dispatch(deleteDeck(deckId))
        // return message
    }
}



// reducer
const decksReducer = (state = {}, action) => {
    let newState = {}
    switch(action.type){
        case SET_DECKS:
            action.decks.forEach(deck => newState[deck.id] = deck);
            return newState

        case SET_DECK_DETAILS:
            return {
                ...state,
                detailedDeck: action.deck
            }
        case ADD_DECK:
            const newDeck = action.payload
            newState = {...state}
            newState[newDeck.id] = newDeck
            return newState
        case UPDATE_DECK:
            const deckId = action.payload.id
            newState[deckId] = {...state[deckId], ...action.payload}
            newState.detailedDeck = {...state.detailedDeck, ...action.payload}
            return newState
        case DELETE_DECK:
            const d_id = action.payload
            newState = {
                ...state
            }
            delete newState[d_id]
            return newState
        default:
            return state;
    }
}

export default decksReducer;
