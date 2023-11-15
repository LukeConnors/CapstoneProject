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
# 9
    books1 = Deck(
        user_id=9,
        title="Books: Deck 1",
        description="Explore the world of literature with this trivia deck.",
        category="Entertainment"
    )
# 10
    film1 = Deck(
        user_id=10,
        title="Film: Deck 1",
        description="Test your knowledge of movies with this trivia deck.",
        category="Entertainment"
    )

# 11
    music1 = Deck(
        user_id=3,
        title="Music: Deck 1",
        description="Test your knowledge of music with this trivia deck.",
        category="Entertainment"
    )

# 12
    musicals_theatres1 = Deck(
        user_id=4,
        title="Musicals & Theatres: Deck 1",
        description="Test your knowledge of musicals and theatres with this trivia deck.",
        category="Entertainment"
    )

# 13
    television1 = Deck(
        user_id=7,
        title="Television: Deck 1",
        description="Test your knowledge of television with this trivia deck.",
        category="Entertainment"
    )

# 14
    board_games1 = Deck(
        user_id=1,
        title="Board Games: Deck 1",
        description="Test your knowledge of board games with this trivia deck.",
        category="Entertainment"
    )

    # 15
    anime1 = Deck(
        user_id=5,
        title="Anime: Deck 1",
        description="Test your knowledge of anime with this trivia deck.",
        category="Entertainment"
    )

    # 16
    film2 = Deck(
        user_id=8,
        title="Film: Deck 2",
        description="Test your knowledge of movies with this trivia deck.",
        category="Entertainment"
    )

    # 17
    cartoons1 = Deck(
        user_id=9,
        title="Cartoons: Deck 1",
        description="Test your knowledge of cartoons with this trivia deck.",
        category="Entertainment"
    )

    # 18
    comics1 = Deck(
        user_id=10,
        title="Comics: Deck 1",
        description="Test your knowledge of comics with this trivia deck.",
        category="Entertainment"
    )

# 19
    geography2 = Deck(
        user_id=2,
        title="Geography: Deck 2",
        description="Test your knowledge of geography with this trivia deck.",
        category="Geography"
    )

# 20
    mythology2 = Deck(
        user_id=2,
        title="Mythology: Deck 2",
        description="Test your knowledge of mythology with this trivia deck.",
        category="Mythology"
    )

# 21
    math1 = Deck(
        user_id=6,
        title="Math: Deck 1",
        description="Test your knowledge of math with this trivia deck.",
        category="Science"
    )

    # 22
    tele1 = Deck(
        user_id=8,
        title="Television: Deck 2",
        description="Test your knowledge of television with this trivia deck.",
        category="Entertainment"
    )

    # 23
    sports1 = Deck(
        user_id=4,
        title="Sports: Deck 1",
        description="Test your knowledge of sports with this trivia deck.",
        category="Entertainment"
    )
# 24
    politics1 = Deck(
        user_id=7,
        title="Politics: Deck 1",
        description="Test your knowledge of politics with this trivia deck.",
        category="General Knowledge"
    )

# 25
    art1 = Deck(
        user_id=2,
        title="Art: Deck 1",
        description="Test your knowledge of art with this trivia deck.",
        category="Entertainment"
    )

# 26
    animals1 = Deck(
        user_id=8,
        title="Animals: Deck 1",
        description="Test your knowledge of animals with this trivia deck.",
        category="Science & Nature"
    )

# 27
    vehicles1 = Deck(
        user_id=4,
        title="Vehicles: Deck 1",
        description="Test your knowledge of vehicles with this trivia deck.",
        category="Science"
    )

# 28
    comics1 = Deck(
        user_id=6,
        title="Comics: Deck 1",
        description="Test your knowledge of comics with this trivia deck.",
        category="Entertainment"
    )


    db.session.add_all([
        general1, science1, entertainment1, science_nature1,
        mythology1, geography1, history1, celebrities1,
        books1, film1, music1, musicals_theatres1, television1,
        board_games1, anime1, film2, cartoons1, comics1, geography2,
        mythology2, math1, tele1, sports1, politics1, art1, animals1,
        vehicles1, comics1

    ])

    db.session.commit()

def undo_decks():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.decks RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM decks"))

    db.session.commit()
