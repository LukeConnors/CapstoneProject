import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { useHistory } from 'react-router-dom'
import * as questionActions from "../../store/questions"
import "./DeleteQuestion.css"


function DeleteQuestion({question, questionId}){
    const {closeModal} = useModal();
    const [deleted, setDeleted] = useState(false);
    const dispatch = useDispatch();
    const history = useHistory();

    const handleCancel = () => {
        closeModal()
    }
    const handleDelete = async (e) => {
        e.preventDefault();
        await dispatch(questionActions.removeQuestion(questionId))
        setDeleted(true)
    }
    // useEffect(() => {
    //     if (deleted) {
    //       const timeout = setTimeout(() => {
    //         history.push('/my_profile')
    //         closeModal();
    //       }, 1500);

    //       return () => clearTimeout(timeout);
    //     }
    //   }, [deleted, closeModal]);

      return (
        <div className="delete-q-modal">
            {deleted ? (
                <>
                <h1>Deleted Successfully!</h1>
                {closeModal()}
                </>
            ) : (
            <>
            <h1>Are you sure you want to delete your Question?</h1>
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

export default DeleteQuestion
