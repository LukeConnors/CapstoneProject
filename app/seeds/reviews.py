from app.models import db, Review, environment, SCHEMA
from sqlalchemy.sql import text

def seed_reviews():
    review1 = Review(
        user_id=1,
        deck_id= 1,
        stars=4,
        description="This General Knowledge deck is perfect for beginners. The questions are straightforward and enjoyable, making it a great choice to kickstart your trivia journey."
    )
    review2 = Review(
        user_id=2,
        deck_id= 1,
        stars=5,
        description="A fantastic deck for trivia newcomers. It offers a wide range of general knowledge questions that are easy to grasp, ensuring a fun and informative experience."
    )
    review3 = Review(
        user_id=4,
        deck_id= 1,
        stars=5,
        description="I found General: Deck 1 to be an excellent starting point for trivia enthusiasts. The questions are engaging and provide a solid foundation for more challenging decks."
    )

    review4 = Review(
        user_id=6,
        deck_id= 2,
        stars=4,
        description="Science: Deck 1 is a knowledge-packed adventure into the world of science. If you're a science enthusiast, this deck is a must-try."
    )

    review5 = Review(
        user_id=7,
        deck_id= 2,
        stars=4,
        description="I thoroughly enjoyed Science: Deck 1. It's filled with intriguing science questions that will test your understanding of the natural world. Highly recommended!"
    )

    review6 = Review(
        user_id=9,
        deck_id= 2,
        stars=5,
        description="As a science lover, I found Science: Deck 1 to be an absolute delight. The questions cover a wide array of scientific topics, making it both entertaining and educational."
    )

    review7 = Review(
        user_id=4,
        deck_id= 3,
        stars=3,
        description="Entertainment: Deck 1 is pure fun! It's a fantastic mix of questions related to movies, music, and more. Perfect for a casual trivia night with friends."
    )

    review8 = Review(
        user_id=7,
        deck_id= 3,
        stars=4,
        description="If you're looking for a deck to enjoy with friends or family, Entertainment: Deck 1 is an excellent choice. It's packed with entertainment-related trivia that everyone can relate to."
    )

    review9 = Review(
        user_id=2,
        deck_id= 3,
        stars=2,
        description="I found Entertainment: Deck 1 to be a bit too focused on pop culture. If you're not up-to-date with the latest trends, you might struggle with some questions."
    )

    review10 = Review(
        user_id=5,
        deck_id= 4,
        stars=5,
        description="Science & Nature: Deck 1 is a nature lover's dream. The questions cover a wide range of topics related to the natural world, making it both educational and enjoyable."
    )

    review11 = Review(
        user_id=1,
        deck_id= 4,
        stars=5,
        description="Exploring the wonders of our planet has never been more fun! Science & Nature: Deck 1 offers an exciting journey through science and the environment."
    )

    review12 = Review(
        user_id=2,
        deck_id= 4,
        stars=2,
        description="While Science & Nature: Deck 1 is informative, I found some questions to be overly detailed and challenging. It might not be suitable for casual players."
    )

    review13 = Review(
        user_id=6,
        deck_id= 5,
        stars=4,
        description="Mythology: Deck 1 takes you on a captivating journey into ancient stories and legends. It's a must-try for anyone intrigued by mythology."
    )

    review14 = Review(
        user_id=9,
        deck_id= 5,
        stars=1,
        description="Mythology: Deck 1 felt a bit too niche for my taste. If you're not already well-versed in mythology, you might struggle to answer many of the questions."
    )

    review15 = Review(
        user_id=10,
        deck_id= 5,
        stars=5,
        description="Delve into the mysteries of mythology with Mythology: Deck 1. The questions are both entertaining and educational, making it a great choice for history buffs."
    )

    review16 = Review(
        user_id=4,
        deck_id= 6,
        stars=3,
        description="Geography: Deck 1 is a good way to test your knowledge of the world's geography. It's both informative and enjoyable, perfect for geography enthusiasts."
    )

    review17 = Review(
        user_id=2,
        deck_id= 6,
        stars=1,
        description="I found Geography: Deck 1 to be too focused on obscure geographic facts. It might be overwhelming for those who aren't geography buffs."
    )

    review18 = Review(
        user_id=5,
        deck_id= 6,
        stars=4,
        description="Travel the globe from the comfort of your home with Geography: Deck 1. It's packed with questions about countries, capitals, and landmarks, making it a geography lover's paradise."
    )

    review19 = Review(
        user_id=9,
        deck_id= 7,
        stars=2,
        description="History: Deck 1 felt a bit dry to me. While it's informative, it lacks the excitement and entertainment value that some other decks offer."
    )

    review20 = Review(
        user_id=7,
        deck_id= 7,
        stars=5,
        description="Step into the shoes of historical figures and relive the past with History: Deck 1. The questions are intriguing and thought-provoking, making it an engaging history trivia deck."
    )

    review21 = Review(
        user_id=10,
        deck_id= 7,
        stars=5,
        description="History: Deck 1 is a time machine that transports you to significant historical events and figures. It's a must-try for history enthusiasts."
    )

    review22 = Review(
        user_id=4,
        deck_id= 8,
        stars=5,
        description="Celebrities: Deck 1 is your backstage pass to the world of famous personalities. It's packed with questions about celebrities, making it a great choice for pop culture enthusiasts."
    )

    review23 = Review(
        user_id=6,
        deck_id= 8,
        stars=4,
        description="Get ready to be entertained with Celebrities: Deck 1. It's a fun and lighthearted deck that lets you test your knowledge of the stars."
    )

    review24 = Review(
        user_id=8,
        deck_id= 8,
        stars=1,
        description="Celebrities: Deck 1 felt superficial to me. It focuses too much on gossip and tabloid-style questions, which I found uninteresting."
    )


    db.session.add_all([
      review1, review2, review3, review4, review5, review6, review7,
      review8, review9, review10, review11, review12, review13, review14,
      review15, review16, review17, review18, review19, review20, review21,
      review22, review23, review24
    ])

    db.session.commit()


def undo_reviews():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.reviews RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM reviews"))

    db.session.commit()
