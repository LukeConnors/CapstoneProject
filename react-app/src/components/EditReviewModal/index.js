import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { useHistory } from 'react-router-dom'
import * as reviewActions from "../../store/reviews"
import {FaStar} from "react-icons/fa"
import "./EditReviewModal.css"



function EditReview({review, reviewId}){
    const {closeModal} = useModal();
    const dispatch = useDispatch();
    const [reviewStars, setReviewStars] = useState(review.stars)
    const [hover, setHover] = useState(null)
    const [errors, setErrors] = useState({})
    const [formData, setFormData] = useState({
        stars: review.stars,
        description: review.description
    })

    const handleSubmit = async (e) => {
        e.preventDefault();
        let formErrors = {};
        if (!formData.stars) {
            formErrors.stars = "Please provide a star rating"
        }
        if (!formData.description) {
            formErrors.description = "Please provide a review description"
        }
        if (formData.description.length < 25) {
            formErrors.description = "Description needs to be 25 or more characters";
        }
        if (Object.keys(formErrors).length > 0) {
            setErrors(formErrors);
            return;
        }

        let editedReview = await dispatch(reviewActions.editReview(reviewId, formData))
        if(editedReview && editedReview?.id){
            closeModal()
        } else {
            return editedReview
        }
    }
    return(
        <div>
            <div className="form-container">
                <h1>Edit your Review</h1>
                <form onSubmit={handleSubmit}>
                <h2>Rate your experience 1-5 stars:</h2>
                    <div className="errors">{errors?.stars}</div>
                    {[...Array(5)].map((star, index) => {
                        const currentStars = index + 1
                        return (
                            <label>
                                <input
                                    className="star-input"
                                    type="radio"
                                    name="stars"
                                    value={formData.stars}
                                    onClick={() => setReviewStars(currentStars)}
                                    onChange={(e) => setFormData({...formData, stars: currentStars})}
                                    checked={currentStars === reviewStars}
                                />
                                <FaStar
                                className="star"
                                color={currentStars <= (hover || reviewStars) ? "#06c0d1" : "#026770"}
                                onMouseEnter={() => setHover(currentStars)}
                                onMouseLeave={() => setHover(null)}
                                />
                            </label>
                        )
                    })}
                    <h2>Give a Description of your experience:</h2>
                    <div className="errors">{errors?.description}</div>
                    <textarea
                    cols="30"
                    rows="5"
                    className="form-input"
                    placeholder="Description"
                    value={formData.description}
                    onChange={(e) => setFormData({...formData, description: e.target.value})}
                    />
                    <button className="login-button" type="submit">Submit</button>

                </form>

            </div>
        </div>
    )
}

export default EditReview
