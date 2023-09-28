import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useModal } from "../../context/Modal";
import { useHistory } from 'react-router-dom'
import * as deckActions from "../../store/decks"
import * as userActions from "../../store/session"


function DeckForm(){
    const [errors, setErrors] = useState({})
    const dispatch = useDispatch();
    const history = useHistory()
    const user = useSelector(state => state.session.user)
    const [formData, setFormData] = useState({
        title: "",
        description: "",
        category: "",
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
        let newDeck = await dispatch(deckActions.createDeck(formData))
        if(newDeck && newDeck?.id){
            history.push(`/decks/${newDeck?.id}`)
        } else {
          return newDeck;
        }
    }
if(user === null){
history.push("/login")
}
return (
    <div className="form-container">
        <h1>Create a New Deck</h1>
        <form onSubmit={handleSubmit}>
        <h2>Give your Deck a Title:</h2>
        <div className="errors">{errors?.title}</div>
        <input
        type="text"
        className="form-input"
        placeholder="Title"
        value={formData.title}
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
        <button type="submit">Submit</button>
        </form>

    </div>
)

}


export default DeckForm
