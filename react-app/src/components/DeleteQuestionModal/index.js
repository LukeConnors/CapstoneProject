import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import * as questionActions from "../../store/questions"


function DeleteQuestion({question, questionId}){
    const {closeModal} = useModal();
    const [deleted, setDeleted] = useState(false);
    const dispatch = useDispatch();

    const handleCancel = () => {
        closeModal()
    }
    const handleDelete = async (e) => {
        e.preventDefault();
        await dispatch(questionActions.removeQuestion(questionId))
        setDeleted(true)
    }
    useEffect(() => {
        if (deleted) {
          const timeout = setTimeout(() => {
            dispatch(questionActions.fetchMyQuestions())
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
            <h1>Are you sure you want to delete your Question?</h1>
            <div className="delete-deck-btn">
                <button onClick={handleCancel}>Cancel</button>
                <button className="delete btn" onClick={handleDelete}>
                    Delete
                </button>

            </div>
            </>
            )}
        </div>
    )
}

export default DeleteQuestion
