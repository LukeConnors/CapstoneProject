import React, { useState, useEffect } from "react";
import "./HomePage.css";
import { Link } from "react-router-dom";

function HomePage(){

return (
    <>
    <h1 className="welcome">Welcome to Trivia Titan! Please Select a Category:</h1>
    <div className="card-container">
        <Link className="home-link" to="/decks/deck_category?category=General%20Knowledge">
        <div className="card">
            <h1 className="home-title">General Knowledge</h1>
            <img className="home-img" src="https://res.cloudinary.com/dyt7uoeck/image/upload/v1695652386/GK_w17j9r.png"></img>
        </div>
        </Link>
        <Link className="home-link" to="/decks/deck_category?category=Entertainment">
        <div className="card">
            <h1 className="home-title">Entertainment</h1>
            <img className="home-img" src="https://res.cloudinary.com/dyt7uoeck/image/upload/v1695846170/entertainment2_eihe58.png"></img>
        </div>
        </Link>
        <Link className="home-link" to="/decks/deck_category?category=Science">
        <div className="card">
            <h1 className="home-title">Science</h1>
            <img className="home-img" src="https://res.cloudinary.com/dyt7uoeck/image/upload/v1695841294/Science_n3cvzq.png"></img>
        </div>
        </Link>
        <Link className="home-link" to="/decks/deck_category?category=Science%20&%20Nature">
        <div className="card">
            <h1 className="home-title">Science & Nature</h1>
            <img className="home-img" src="https://res.cloudinary.com/dyt7uoeck/image/upload/v1695841614/S_N_frz2gh.png"></img>
        </div>
        </Link>
        <Link className="home-link" to="/decks/deck_category?category=Mythology">
        <div className="card">
            <h1 className="home-title">Mythology</h1>
            <img className="home-img" src="https://res.cloudinary.com/dyt7uoeck/image/upload/v1695841786/mythology_gk2acu.png"></img>
        </div>
        </Link>
        <Link className="home-link" to="/decks/deck_category?category=Geology">
        <div className="card">
            <h1 className="home-title">Geology</h1>
            <img className="home-img" src="https://res.cloudinary.com/dyt7uoeck/image/upload/v1695842013/geology_wd6gjd.png"></img>
        </div>
        </Link>
        <Link className="home-link" to="/decks/deck_category?category=History">
        <div className="card">
            <h1 className="home-title">History</h1>
            <img className="home-img" src="https://res.cloudinary.com/dyt7uoeck/image/upload/v1695842146/history_ent70a.png"></img>
        </div>
        </Link>
        <Link className="home-link" to="/decks/deck_category?category=Celebrities">
        <div className="card">
            <h1 className="home-title">Celebrities</h1>
            <img className="home-img" src="https://res.cloudinary.com/dyt7uoeck/image/upload/v1695842275/celebrity_z1tqrg.png"></img>
        </div>
        </Link>
    </div>
    </>
)

}


export default HomePage
