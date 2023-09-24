import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Switch } from "react-router-dom";
import SignupFormPage from "./components/SignupFormPage";
import LoginFormPage from "./components/LoginFormPage";
import { authenticate } from "./store/session";
import Navigation from "./components/Navigation";
import HomePage from "./components/HomePage";
import Category from "./components/CategoryPage";
import DeckForm from "./components/DeckForm";
import DeckDetails from "./components/DeckDetailsPage";
import DeckQuestionsPage from "./components/DeckQuestionsPage";
import QuestionForm from "./components/QuestionForm";

function App() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);
  useEffect(() => {
    dispatch(authenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);

  return (
    <>
      <Navigation isLoaded={isLoaded} />
      {isLoaded && (
        <Switch>
          <Route path='/decks/deck_category'>
            <Category />
          </Route>
          <Route exact path="/decks/:deckId/questions">
          <DeckQuestionsPage />
          </Route>
          <Route exact path="/decks/:deckId">
            <DeckDetails />
          </Route>
          <Route path="/login" >
            <LoginFormPage />
          </Route>
          <Route path="/signup">
            <SignupFormPage />
          </Route>
          <Route path="/new_deck">
          <DeckForm />
          </Route>
          <Route path="/new_question">
          <QuestionForm />
          </Route>
          <Route exact path="/">
            <HomePage />
          </Route>
        </Switch>
      )}
    </>
  );
}

export default App;
