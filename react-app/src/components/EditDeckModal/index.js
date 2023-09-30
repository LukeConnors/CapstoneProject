import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { useHistory } from 'react-router-dom'
import * as deckActions from "../../store/decks"
import "./EditDeck.css"



function EditDeck({deck, deckId}){
    const { closeModal } = useModal();
    const [errors, setErrors] = useState({})
    const dispatch = useDispatch();
    const history = useHistory()
    const [formData, setFormData] = useState({
        title: deck.title,
        description: deck.description,
        category: deck.category,
    })


    const handleSubmit = async (e) => {
        e.preventDefault();

        let formErrors = {};
        if (!formData.title){
            formErrors.title = "Title is required"
        }
        if (!formData.description || formData.description.length < 25) {
            formErrors.description = "Description needs to be 25 or more characters";
          }
        if (!formData.category){
            formErrors.category = "Please select a category"
        }

        if (Object.keys(formErrors).length > 0){
            setErrors(formErrors);
            return;
        }

        let updated = await dispatch(deckActions.editDeck(deckId, formData))
        if(updated && updated?.id){
            closeModal()
            history.push(`/decks/${updated?.id}`)
        } else {
          return updated;
        }
    }

return (
    <div className="edit-form-container">
        <h1>Edit your Deck</h1>
        <form onSubmit={handleSubmit}>
        <h2>Give your Deck a Title:</h2>
        <div className="errors">{errors?.title}</div>
        <input
        type="text"
        className="form-input"
        placeholder="Title"
        value={formData?.title}
        onChange={(e) => setFormData({ ...formData, title: e.target.value })}
        >
        </input>
        <h2>Give your Deck a Creative Description:</h2>
        <div className="errors">{errors?.description}</div>
        <textarea
        cols="30"
        rows="5"
        className="form-input"
        placeholder="Description"
        value={formData.description}
        onChange={(e) => setFormData({ ...formData, description: e.target.value })}
        />
        <h2>Choose a Category for your Deck:</h2>
        <div className="errors">{errors?.category}</div>
        <select
        name="categories"
        value={formData?.category}
        onChange={(e)=> setFormData({ ...formData, category: e.target.value })}
        >
        <option>
            Please select a Category...
        </option>
        <option>
            General Knowledge
        </option>
        <option>
            Science
        </option>
        <option>
            Entertainment
        </option>
        <option>
            Science & Nature
        </option>
        <option>
            Mythology
        </option>
        <option>
            Geography
        </option>
        <option>
            History
        </option>
        <option>
            Celebrities
        </option>
        </select>
        <div className="login-button-div">
        <button className="login-button" type="submit">Submit</button>
        </div>
        </form>

    </div>
)

}


export default EditDeck
