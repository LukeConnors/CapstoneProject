import React, { useState, useEffect } from "react";
import "./HomePage.css";
import { Link } from "react-router-dom";

function HomePage(){

return (
    <div className="card-container">
        <Link to="/decks/deck_category?category=General%20Knowledge">
        <div className="card">
            <h1>General Knowledge</h1>
        </div>
        </Link>
        <Link to="/decks/deck_category?category=Entertainment">
        <div className="card">
            <h1>Entertainment</h1>
        </div>
        </Link>
        <Link to="/decks/deck_category?category=Science">
        <div className="card">
            <h1>Science</h1>
        </div>
        </Link>
        <Link to="/decks/deck_category?category=Science%20&%20Nature">
        <div className="card">
            <h1>Science & Nature</h1>
        </div>
        </Link>
        <Link to="/decks/deck_category?category=Mythology">
        <div className="card">
            <h1>Mythology</h1>
        </div>
        </Link>
        <Link to="/decks/deck_category?category=Geology">
        <div className="card">
            <h1>Geology</h1>
        </div>
        </Link>
        <Link to="/decks/deck_category?category=History">
        <div className="card">
            <h1>History</h1>
        </div>
        </Link>
        <Link to="/decks/deck_category?category=Celebrities">
        <div className="card">
            <h1>Celebrities</h1>
        </div>
        </Link>
    </div>
)

}


export default HomePage
