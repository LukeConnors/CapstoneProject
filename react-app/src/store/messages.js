export const SET_MESSAGES = "messages/SET_MESSAGES"

export const setUserMessages = (messages) => ({
    type: SET_MESSAGES,
    messages
})

export const getUserMessages = (userId) => async (dispatch) => {
    const res = await fetch(`/api/messages/${userId}`)
    const data = await res.json()
    dispatch(setUserMessages(data.messages))
    return data.messages
}

const messagesReducer = (state = {}, action) => {
    let newState = {}
    switch(action.type) {
        case SET_MESSAGES:
            action.messages.forEach(message => newState[message.id] = message)
            return newState
        default:
            return state
    }
}

export default messagesReducer
