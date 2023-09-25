import { UPDATE_DECK } from "./decks"

export const SET_QUESTIONS = "questions/SET_QUESTIONS"
export const SET_QUESTION_DETAILS = "questions/SET_QUESTION_DETAILS"
export const ADD_QUESTION = "questions/ADD_QUESTION"
export const UPDATE_QUESTION = "questions/UPDATE_QUESTION"
export const DELETE_QUESTION = "questions/DELETE_QUESTION"


export const questionsSelector = (state) => {
    return state.questions
}

const setQuestions = (questions) => ({
    type: SET_QUESTIONS,
    questions
})

const setQuestionDetails = (question) => ({
    type: SET_QUESTION_DETAILS,
    question
})

const addQuestion = (question) => ({
    type: ADD_QUESTION,
    payload: question
})

const updateQuestion = (question) => ({
    type: UPDATE_QUESTION,
    payload: question
})

const deleteQuestion = (questionId) => ({
    type: DELETE_QUESTION,
    payload: questionId
})

export const fetchQuestions = () => async (dispatch) => {
    const res = await fetch("/api/questions/")
    const data = await res.json();
    dispatch(setQuestions(data.questions))
    return data
}

export const fetchMyQuestions = () => async (dispatch) => {
    const res = await fetch("/api/questions/my_questions")
    const data = await res.json();
    dispatch(setQuestions(data.questions))
    return data
}

export const fetchQuestionDetails = (questionId) => async (dispatch) => {
    const res = await fetch(`/api/questions/${questionId}`);
    const data = await res.json();
    dispatch(setQuestionDetails(data))
    return data
}

export const createQuestion = (payload) => async (dispatch) => {
    try {
        const res = await fetch("/api/questions/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(payload)
        })
        if(res.ok){
            const newQuestion = await res.json()
            dispatch(addQuestion(newQuestion))
            return newQuestion
        }
    } catch(e){
        return e
    }
}

export const editQuestion = (questionId, payload) => async (dispatch) => {
    try {
        const res = await fetch(`/api/questions/${questionId}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(payload)
        });
        if(res.ok){
            const editedQuestion = await res.json();
            dispatch(updateQuestion(editedQuestion))
            return editedQuestion
        }
    } catch(e){
        return e
    }
}

export const removeQuestion = (questionId) => async (dispatch) => {
    const res = fetch(`/api/questions/${questionId}`, {
        method: "DELETE"
    });
    if(res.ok){
        const message = await res.json();
        dispatch(deleteQuestion(questionId))
        return message
    }
}

const questionsReducer = (state = {}, action) => {
    let newState = {}
    switch(action.type){
        case SET_QUESTIONS:
            action.questions.forEach(question => newState[question.id] = question);
            return newState

        case SET_QUESTION_DETAILS:
            return {
                ...newState,
                detailedQuestion: action.question
            }
        case ADD_QUESTION:
            const newQuestion = action.payload
            newState = {...state}
            newState[newQuestion.id] = newQuestion
            return newState
        case UPDATE_QUESTION:
            const questionId = action.payload.id
            newState[questionId] = {...state[questionId], ...action.payload}
            return newState

        default:
            return state;
        }
}

export default questionsReducer;
