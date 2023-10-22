// constants
const SET_USER = "session/SET_USER";
const REMOVE_USER = "session/REMOVE_USER";
const GET_USER = "session/GET_USER";
const GET_INCORRECT = "session/GET_INCORRECT"
const GET_CORRECT = "session/GET_CORRECT"
const ADD_CORRECT = "session/ADD_CORRECT"
const ADD_INCORRECT = "session/ADD_INCORRECT"


export const userSelector = (state) => {
	return state.session.detailedUser
}

const setUser = (user) => ({
	type: SET_USER,
	payload: user,
});

const getIncorrect = (incorrect_answers) => ({
	type: GET_INCORRECT,
	incorrect_answers
})

const getCorrect = (correct_answers) => ({
	type: GET_CORRECT,
	correct_answers
})

const addCorrect = (question) => ({
	type: ADD_CORRECT,
	payload: question
})

const addIncorrect = (question) => ({
	type: ADD_INCORRECT,
	payload: question
})

const getUser = (user) => ({
	type: GET_USER,
	user
})

const removeUser = () => ({
	type: REMOVE_USER,
});


export const authenticate = () => async (dispatch) => {
	const response = await fetch("/api/auth/", {
		headers: {
			"Content-Type": "application/json",
		},
	});
	if (response.ok) {
		const data = await response.json();
		if (data.errors) {
			return;
		}

		dispatch(setUser(data));
	}
};

export const getUserDetails = (userId) => async (dispatch) => {
	const res = await fetch(`/api/users/${userId}`)
	const data = await res.json();
	dispatch(getUser(data))
	return data
}

export const fetchIncorrectAnswers = (userId) => async (dispatch) => {
	const res = await fetch(`/api/users/${userId}/incorrect`)
	const data = await res.json();
	dispatch(getIncorrect(data.incorrect_answers))
	return data
}

export const fetchCorrectAnswers = (userId) => async (dispatch) => {
	const res = await fetch(`/api/users/${userId}/correct`)
	const data = await res.json();
	dispatch(getCorrect(data.correct_answers))
	return data
}

export const login = (email, password) => async (dispatch) => {
	const response = await fetch("/api/auth/login", {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify({
			email,
			password,
		}),
	});

	if (response.ok) {
		const data = await response.json();
		dispatch(setUser(data));
		return null;
	} else if (response.status < 500) {
		const data = await response.json();
		if (data.errors) {
			return data.errors;
		}
	} else {
		return ["An error occurred. Please try again."];
	}
};

export const logout = () => async (dispatch) => {
	const response = await fetch("/api/auth/logout", {
		headers: {
			"Content-Type": "application/json",
		},
	});

	if (response.ok) {
		dispatch(removeUser());
	}
};

export const signUp = (data) => async (dispatch) => {
	const response = await fetch("/api/auth/signup", {
		method: "POST",
		// headers: {
		// 	"Content-Type": "application/x-www-form-urlencoded",
		// },
		body: data
	});

	if (response.ok) {
		const data = await response.json();
		dispatch(setUser(data));
		return null;
	} else if (response.status < 500) {
		const data = await response.json();
		if (data.errors) {
			return data.errors;
		}
	} else {
		return ["An error occurred. Please try again."];
	}
};


export const createCorrectAnswer = (userId, payload) => async (dispatch) => {
	const res = await fetch(`/api/users/${userId}/correct`, {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify(payload)
	})
	if (res.ok) {
		const newCorrectAnswer = await res.json()
		dispatch(addCorrect(newCorrectAnswer))
		return newCorrectAnswer
	}

}

export const createIncorrectAnswer = (userId, payload) => async (dispatch) => {
	const res = await fetch(`/api/users/${userId}/incorrect`, {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify(payload)
	})
	if (res.ok) {
		const newIncorrectAnswer = await res.json()
		dispatch(addIncorrect(newIncorrectAnswer))
		return newIncorrectAnswer
	}

}
// const initialState = { user: null };

export default function reducer(state = {}, action) {
	let newState = {}
	switch (action.type) {
		case SET_USER:
			return {
				...state,
				user: action.payload
			};
		case REMOVE_USER:
			return {
				user: null
			};
		case GET_USER:
			return {
				...state,
				user: { ...state.user },
				detailedUser: action.user
			}
		case GET_INCORRECT:
			newState = {
				...state,
				incorrect: {},
				correct: { ...state.correct }
			}
			action.incorrect_answers.forEach(incorrect_answer => newState.incorrect[incorrect_answer.id] = incorrect_answer)
			return newState
		case GET_CORRECT:
			newState = {
				...state,
				incorrect: { ...state.incorrect },
				correct: {}
			}
			action.correct_answers.forEach(correct_answer => newState.correct[correct_answer.id] = correct_answer)
			return newState
		case ADD_CORRECT:
			const newCorrect = action.payload
			newState = {
				...state,
				incorrect: { ...state.incorrect },
				correct: { ...state.correct }
			}
			newState.correct[newCorrect.id] = newCorrect
			return newState

		case ADD_INCORRECT:
			const newIncorrect = action.payload
			newState = {
				...state,
				incorrect: { ...state.incorrect },
				correct: { ...state.correct }
			}
			newState.incorrect[newIncorrect.id] = newIncorrect
			return newState
		default:
			return state;
	}
}
