import React, { useEffect, useState } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { useHistory } from "react-router-dom";
import * as reviewActions from "../../store/reviews"
import "./DeleteReviewModal.css"

function DeleteReview({review, reviewId}){
    const {closeModal} = useModal();
    const [deleted, setDeleted] = useState(false);
    const dispatch = useDispatch();
    const history = useHistory();

    const handleCancel = () => {
        closeModal()
    }

    const handleDelete = async (e) => {
        await dispatch(reviewActions.removeReview(reviewId))
        setDeleted(true)
    }
    useEffect(() => {
        if (deleted) {
          const timeout = setTimeout(() => {
            closeModal();
          }, 1500);

          return () => clearTimeout(timeout);
        }
      }, [deleted, closeModal]);

      return (
        <div className="delete-modal">
            {deleted ? (
                <>
                <h1>Deleted Successfully!</h1>
                </>
            ) : (
            <>
            <h1>Are you sure you want to delete your Review?</h1>
            <div className="delete-deck-btn">
                <button className="cancel-btn" onClick={handleCancel}>Cancel</button>
                <button className="delete-btn" onClick={handleDelete}>
                    Delete
                </button>

            </div>
            </>
            )}
        </div>
    )
}

export default DeleteReview
