import { useState } from "react"
import { useDispatch, useSelector } from "react-redux";
import { useModal } from "../../context/Modal";
import * as reviewActions from "../../store/reviews"
import {FaStar} from "react-icons/fa"
import "./AddReviewModal.css"


function AddReview() {
    const [errors, setErrors] = useState({});
    const dispatch = useDispatch();
    const [stars, setStars] = useState(null)
    const [hover, setHover] = useState(null)
    const { closeModal } = useModal();
    const [formData, setFormData] = useState({
        stars: "",
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
        let newReview = await dispatch(reviewActions.createReview(formData))
        if (newReview && newReview?.id) {
            closeModal()
        }
    }

    return (
        <div>
            <div className="form-container">
                <h1>Add your Review</h1>
                <form onSubmit={handleSubmit}>
                    <h2>Rate your review 1-5 Stars</h2>
                    <div className="errors">{errors?.stars}</div>
                    {[...Array(5)].map((star, index) => {
                        const currentStars = index + 1
                        return (
                            <label>
                                <input
                                    className="star-input"
                                    type="radio"
                                    name="stars"
                                    value={currentStars}
                                    onClick={() => setStars(currentStars)}
                                    checked={currentStars === stars}
                                />
                                <FaStar
                                className="star"
                                color={currentStars <= (hover || stars) ? "#06c0d1" : "#026770"}
                                onMouseEnter={() => setHover(currentStars)}
                                onMouseLeave={() => setHover(null)}
                                />
                            </label>
                        )
                    })}

                </form>

            </div>
        </div>
    )
}

export default AddReview
