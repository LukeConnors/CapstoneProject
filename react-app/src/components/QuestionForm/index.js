import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from 'react-router-dom'
import * as deckActions from "../../store/decks"
import * as questionActions from "../../store/questions"
import "./QuestionForm.css"

function QuestionForm() {
    const [errors, setErrors] = useState({});
    const dispatch = useDispatch();
    const user = useSelector(state => state.session.user)
    const history = useHistory();
    const [formData, setFormData] = useState({
        category: "",
        type: "",
        difficulty: "",
        question: "",
        correct_answer: "",
        incorrect_answer1: "",
        incorrect_answer2: "",
        incorrect_answer3: ""
    });

    const categoryChoices = ["General Knowledge", "Entertainment: Books", "Entertainment: Film",
    "Entertainment: Music", "Entertainment: Musicals & Theatres", "Entertainment: Television",
    "Entertainment: Video Games", "Entertainment: Japanese Anime & Manga", "Entertainment: Board Games", "Science & Nature",
    "Science: Computers", "Science: Mathematics", "Mythology", "Sports",
    "Geography", "History", "Politics", "Art", "Celebrities", "Animals", "Vehicles",
    "Entertainment: Comics", "Science: Gadgets", "Entertainment: Cartoon & Animations"]

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: value
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        const { incorrect_answer1, incorrect_answer2, incorrect_answer3 } = formData;
        let formErrors = {};
        if (!formData.question) {
            formErrors.question = "Question is required"
        }
        if (!formData.correct_answer) {
            formErrors.correct_answer = "Correct answer is required";
        }
        if (!formData.difficulty) {
            formErrors.difficulty = "Please select a question difficulty"
        }
        if (!formData.type) {
            formErrors.type = "Please select a question type"
        }
        if (!formData.category) {
            formErrors.category = "Please select a question category"
        }
        if (formData.type === "boolean" && !formData.incorrect_answer1) {
            formErrors.incorrect_answer1 = "True/False types require an incorrect answer of True or False"
        }
        if (formData.type === "boolean" && formData.incorrect_answer1 !== "True" && formData.incorrect_answer1 !== "False") {
            formErrors.incorrect_answer1 = "True/False types require an incorrect answer of True or False"
        }
        if (formData.type === "boolean" && formData.correct_answer !== "True" && formData.correct_answer !== "False") {
            formErrors.correct_answer = "True/False types require a correct answer of True or False"
        }
        if (formData.type === "boolean" && formData.correct_answer === "True" && formData.incorrect_answer1 === "True") {
            formErrors.incorrect_answer1 = "Your incorrect answer cannot be the same as the correct answer!"
        }
        if (formData.type === "boolean" && formData.correct_answer === "False" && formData.incorrect_answer1 === "False") {
            formErrors.incorrect_answer1 = "Your incorrect answer cannot be the same as the correct answer!"
        }
        if (formData.type === "boolean" && formData.incorrect_answer2) {
            formErrors.incorrect_answer2 = "True/False questions should only have one incorrect answer, fill this out in Incorrect Answer 1!"
        }
        if (formData.type === "boolean" && formData.incorrect_answer3) {
            formErrors.incorrect_answer3 = "True/False questions should only have one incorrect answer, fill this out in Incorrect Answer 1!"
        }
        if (formData.type === "multiple" && !formData.incorrect_answer1) {
            formErrors.incorrect_answer1 = "Multiple choice types require 3 incorrect answers"
        }
        if (formData.type === "multiple" && !formData.incorrect_answer2) {
            formErrors.incorrect_answer2 = "Multiple choice types require 3 incorrect answers"
        }
        if (formData.type === "multiple" && !formData.incorrect_answer3) {
            formErrors.incorrect_answer3 = "Multiple choice types require 3 incorrect answers"
        }

        if (Object.keys(formErrors).length > 0) {
            setErrors(formErrors);
            return;
        }

        const incorrect_answers = [incorrect_answer1, incorrect_answer2, incorrect_answer3].join(', ');

        const finalFormData = {
            ...formData,
            incorrect_answers
        };

        await dispatch(questionActions.createQuestion(finalFormData));
        history.push("/");
    };


    if (user === null) {
        history.push("/login")
    }
    return (
        <div className="question-form-container">
            <h1>Create Your Question:</h1>
            <form onSubmit={handleSubmit}>
                <h3>Question</h3>
                <div className="errors">{errors?.question}</div>
                <textarea
                    id="question"
                    name="question"
                    className="form-input"
                    value={formData.question}
                    onChange={handleChange}
                />
                <h3>Correct Answer</h3>
                <div className="errors">{errors?.correct_answer}</div>
                <input
                    type="text"
                    id="correct_answer"
                    className="form-input"
                    name="correct_answer"
                    value={formData.correct_answer}
                    onChange={handleChange}
                />
                <h3>Incorrect Answer #1</h3>
                <div className="errors">{errors?.incorrect_answer1}</div>
                <input
                    type="text"
                    id="incorrect_answer1"
                    className="form-input"
                    name="incorrect_answer1"
                    value={formData.incorrect_answer1}
                    onChange={handleChange}
                />
                <h3>Incorrect Answer #2</h3>
                <div className="errors">{errors?.incorrect_answer2}</div>
                <input
                    type="text"
                    id="incorrect_answer2"
                    name="incorrect_answer2"
                    className="form-input"
                    value={formData.incorrect_answer2}
                    onChange={handleChange}
                />
                <h3>Incorrect Answer #3</h3>
                <div className="errors">{errors?.incorrect_answer3}</div>
                <input
                    type="text"
                    id="incorrect_answer3"
                    className="form-input"
                    name="incorrect_answer3"
                    value={formData.incorrect_answer3}
                    onChange={handleChange}
                />
                <h3>Category</h3>
                <div className="errors">{errors?.category}</div>
                <select
                    id="category"
                    name="category"
                    className="form-input"
                    value={formData.category}
                    onChange={handleChange}
                >
                    <option>Select Category</option>
                    {categoryChoices.map((option, index) => (
                        <option key={index} value={option}>
                            {option}
                        </option>
                    ))}
                </select>
                <h3>Type</h3>
                <div className="errors">{errors?.type}</div>
                <select
                    className="form-input"
                    value={formData.type}
                    name="type"
                    onChange={handleChange}
                >
                    <option>Select a type...</option>
                    <option value="multiple">Multiple Choice</option>
                    <option value="boolean">True/False</option>
                </select>
                <h3>Difficulty</h3>
                <div className="errors">{errors?.difficulty}</div>
                <select
                    className="form-input"
                    value={formData.difficulty}
                    name="difficulty"
                    onChange={handleChange}
                >
                    <option value="">Select a difficulty...</option>
                    <option value="easy">Easy</option>
                    <option value="medium">Medium</option>
                    <option value="hard">Hard</option>
                </select>
                <div className="deck-form-button-div">
                    <button className="deck-sub-button" type="submit">Submit</button>
                </div>
            </form>
        </div>
    );
}

export default QuestionForm;
