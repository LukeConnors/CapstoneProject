from app.models import db, Deck, environment, SCHEMA
from sqlalchemy.sql import text

def seed_decks():
#1
    general1 = Deck(
        user_id=1,
        title="General: Deck 1",
        description="This deck is made with some General trivia questions, it is meant for users that are newer to trivia and should be relatively easy.",
        category="General Knowledge"
    )
#2
    science1 = Deck(
        user_id=2,
        title="Science: Deck 1",
        description="This deck contains a variety of science-related trivia questions. Test your knowledge about the world of science!",
        category="Science"
    )

#3
    entertainment1 = Deck(
        user_id=3,
        title="Entertainment: Deck 1",
        description="Get ready for some entertainment trivia! This deck covers movies, music, and more from the world of entertainment.",
        category="Entertainment"
    )

#4
    science_nature1 = Deck(
        user_id=4,
        title="Science & Nature: Deck 1",
        description="Explore the wonders of the natural world with this science and nature-themed trivia deck.",
        category="Science & Nature"
    )

#5
    mythology1 = Deck(
        user_id=5,
        title="Mythology: Deck 1",
        description="Delve into the realms of mythology and ancient stories with this trivia deck.",
        category="Mythology"
    )

#6
    geography1 = Deck(
        user_id=6,
        title="Geography: Deck 1",
        description="Test your knowledge of countries, capitals, and landmarks with this geography trivia deck.",
        category="Geography"
    )

#7
    history1 = Deck(
        user_id=7,
        title="History: Deck 1",
        description="Travel back in time and learn about historical events and figures with this history trivia deck.",
        category="History"
    )

#8
    celebrities1 = Deck(
        user_id=8,
        title="Celebrities: Deck 1",
        description="Get the latest scoop on famous personalities and celebrities with this trivia deck.",
        category="Celebrities"
    )

    db.session.add_all([
        general1, science1, entertainment1, science_nature1,
        mythology1, geography1, history1, celebrities1
    ])

    db.session.commit()

def undo_decks():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.decks RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM decks"))

    db.session.commit()
