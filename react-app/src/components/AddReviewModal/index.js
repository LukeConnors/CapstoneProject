import { useState } from "react"
import { useDispatch, useSelector } from "react-redux";
import { useModal } from "../../context/Modal";
import * as reviewActions from "../../store/reviews"
import { useParams } from "react-router-dom";
import {FaStar} from "react-icons/fa"
import "./AddReviewModal.css"


function AddReview(deckId) {
    const [errors, setErrors] = useState({});
    const dispatch = useDispatch();
    const [reviewStars, setReviewStars] = useState(null)
    const [hover, setHover] = useState(null)
    const { closeModal } = useModal();
    const [formData, setFormData] = useState({
        stars: reviewStars,
        description: "",
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
        let newReview = await dispatch(reviewActions.createReview(deckId.deckId, formData))
        if (newReview && newReview?.id) {
            closeModal()
        }
    }

    return (
        <div>
            <div className="form-container">
                <h1>Add your Review</h1>
                <form className="review-form" onSubmit={handleSubmit}>
                    <h2>Rate your experience 1-5 stars:</h2>
                    <div className="errors">{errors?.stars}</div>
                    <div>
                    {[...Array(5)].map((star, index) => {
                        const currentStars = index + 1
                        return (
                            <label>
                                <input
                                    className="star-input"
                                    type="radio"
                                    name="stars"
                                    value={currentStars}
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
                    </div>
                    <h2>Give a Description of your experience:</h2>
                    <div className="errors">{errors?.description}</div>
                    <textarea
                    cols="30"
                    rows="5"
                    className="description-input"
                    placeholder="Description"
                    value={formData.description}
                    onChange={(e) => setFormData({...formData, description: e.target.value})}
                    />
                    <button className="review-button" type="submit">Submit</button>
                </form>

            </div>
        </div>
    )
}

export default AddReview
