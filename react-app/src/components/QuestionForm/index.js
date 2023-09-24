import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { useHistory } from 'react-router-dom'
import * as deckActions from "../../store/decks"
import * as questionActions from "../../store/questions"

function QuestionForm(){
    const [errors, setErrors] = useState({});
    const dispatch = useDispatch();
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
    "Entertainment: Video Games", "Entertainment: Board Games", "Science & Nature",
    "Science: Computers", "Science: Mathematics", "Mythology", "Sports",
    "Geography", "History", "Politics", "Art", "Celebrities", "Animals"]

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

        const incorrect_answers = [incorrect_answer1, incorrect_answer2, incorrect_answer3].join(', ');

        const finalFormData = {
            ...formData,
            incorrect_answers
        };

        await dispatch(questionActions.createQuestion(finalFormData));
        history.push("/");
    };

    return (
        <form onSubmit={handleSubmit}>
            <div>
                <label htmlFor="question">Question</label>
                <input
                    type="text"
                    id="question"
                    name="question"
                    value={formData.question}
                    onChange={handleChange}
                    required
                />
            </div>
            <div>
                <label htmlFor="correct_answer">Correct Answer</label>
                <input
                    type="text"
                    id="correct_answer"
                    name="correct_answer"
                    value={formData.correct_answer}
                    onChange={handleChange}
                    required
                />
            </div>
            <div>
                <label htmlFor="incorrect_answer1">Incorrect Answer 1</label>
                <input
                    type="text"
                    id="incorrect_answer1"
                    name="incorrect_answer1"
                    value={formData.incorrect_answer1}
                    onChange={handleChange}
                    required
                />
            </div>
            <div>
                <label htmlFor="incorrect_answer2">Incorrect Answer 2</label>
                <input
                    type="text"
                    id="incorrect_answer2"
                    name="incorrect_answer2"
                    value={formData.incorrect_answer2}
                    onChange={handleChange}
                    required
                />
            </div>
            <div>
                <label htmlFor="incorrect_answer3">Incorrect Answer 3</label>
                <input
                    type="text"
                    id="incorrect_answer3"
                    name="incorrect_answer3"
                    value={formData.incorrect_answer3}
                    onChange={handleChange}
                    required
                />
            </div>
            <div>
                <label htmlFor="category">Category</label>
                <select
                    id="category"
                    name="category"
                    value={formData.category}
                    onChange={handleChange}
                    required
                >
                    <option>Select Category</option>
                    {categoryChoices.map((option, index) => (
                        <option key={index} value={option}>
                            {option}
                        </option>
                    ))}
                </select>
            </div>
            <div>
    <label>Type</label>
    <select
        value={formData.type}
        name="type"
        onChange={handleChange}
        required
    >
        <option value="">Select a type...</option>
        <option value="multiple choice">Multiple Choice</option>
        <option value="boolean">True/False</option>
    </select>
</div>
<div>
    <label>Difficulty</label>
    <select
        value={formData.difficulty}
        name="difficulty"
        onChange={handleChange}
        required
    >
        <option value="">Select a difficulty...</option>
        <option value="easy">Easy</option>
        <option value="medium">Medium</option>
        <option value="hard">Hard</option>
    </select>
</div>
            <button type="submit">Submit</button>
        </form>
    );
}

export default QuestionForm;
