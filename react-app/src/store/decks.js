
export const SET_DECKS = "decks/SET_DECKS"
export const SET_DECK_DETAILS = "decks/SET_DECK_DETAILS"
export const SET_DECK_QUESTIONS = "decks/SET_DECK_QUESTIONS"
export const ADD_DECK = "decks/ADD_DECK"
export const ADD_DECK_QUESTION = "decks/ADD_DECK_QUESTION"
export const UPDATE_DECK = "decks/UPDATE_DECK"
export const DELETE_DECK = "decks/DELETE_DECK"

export const decksSelector = (state) => {
    return state.decks
}

export const deckDetailsSelector = (state) => {
    return state.decks.detailedDeck
}

export const deckQuestionsSelector = (state) => {
    return state.decks.deckQuestions
}

const setDecks = (decks) => ({
    type: SET_DECKS,
    decks
})

const setDeckDetails = (deck) => ({
    type: SET_DECK_DETAILS,
    deck
})

const setDeckQuestions = (deck_questions) => ({
    type: SET_DECK_QUESTIONS,
    deck_questions
})

const addDeck = (deck) => ({
    type: ADD_DECK,
    payload: deck
})

const addDeckQuestion = (question) => ({
    type: ADD_DECK_QUESTION,
    payload: question
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

export const fetchDeckQuestions = (deckId) => async (dispatch) => {
    const res = await fetch(`/api/decks/${deckId}/questions`);
    const data = await res.json();
    console.log('FETCH DECK QUESTION DATA', data)
    dispatch(setDeckQuestions(data.deck_questions))
    return data
}

// Fetch all decks by category
export const fetchDecksCategory = (cat) => async (dispatch) => {
    const res = await fetch(`/api/decks/deck_category?category=${cat}`)
    const data = await res.json();
    console.log("this is our data from our fetch", data)
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

// Add a questions to a deck with the deckId
export const createDeckQuestion = (deckId, payload) => async (dispatch) => {
    try {
        const res = await fetch(`/api/decks/${deckId}/questions`, {
            method: ["POST"],
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(payload)
        })
        if(res.ok){
            const deckQuestion = await res.json()
            dispatch(addDeckQuestion(deckQuestion))
            return deckQuestion
        }
    } catch(e){
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
    const res = fetch(`/api/decks/${deckId}`, {
        method: "DELETE"
    });
    if(res.ok){
        const message = await res.json();
        dispatch(deleteDeck(deckId))
        return message
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

        case SET_DECK_QUESTIONS:
            // console.log('ACTION DECK_QUESTIONS', action.deck_questions)
            newState = {
                ...state,
                deckQuestions: {}
            }
            action.deck_questions.forEach(deck_question => newState.deckQuestions[deck_question.id] = deck_question)
            return newState
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
        default:
            return state;
    }
}

export default decksReducer;
