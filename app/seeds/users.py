from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        username='Demo',
        email='demo@aa.io',
        password='password',
        description="Trivia to me is the perfect blend of learning and fun. I enjoy exploring a wide range of topics, from general knowledge to science and nature. My hobbies include reading, watching documentaries, and visiting museums, which all feed my curiosity and passion for trivia."
    )

    marnie  = User(
        username='marnie',
        email='marnie@aa.io',
        password='password',
        description="Trivia is my way of challenging myself while having a great time. As a science enthusiast, I gravitate towards categories like Science & Nature and Science. When I'm not answering trivia questions, you'll find me conducting DIY science experiments and stargazing."
    )

    bobbie = User(
        username='bobbie',
        email='bobbie@aa.io',
        password='password',
        description="Trivia brings out my competitive spirit, especially in categories like Entertainment and Celebrities. I love movies, music, and keeping up with the latest celebrity news. Trivia nights with friends are my favorite way to unwind."
    )

    tristan = User(
        username='tristan',
        email='tristan@aa.io',
        password='password',
        description="For me, trivia is a journey through time and space. I'm a history buff, and I find the History and Geography categories absolutely fascinating. When I'm not exploring historical facts, I'm planning road trips to visit historical landmarks."
    )

    johnny = User(
        username='johnny',
        email='johnny@aa.io',
        password='password',
        description="Trivial pursuits keep me entertained, and I enjoy testing my knowledge in various categories. I have a soft spot for Geography because it connects with my love for hiking and exploring the outdoors. The thrill of discovering new places is unmatched."
    )

    jacob = User(
        username='jacob',
        email='jacob567@aa.io',
        password='password',
        description="To me, trivia is a way to stay connected with popular culture. I'm a big fan of Entertainment and Celebrities categories, and I never miss a movie premiere or a music concert. Trivia nights are where I can show off my knowledge."
    )

    albert = User(
        username='albert',
        email='albert@aa.io',
        password='password',
        description="As a lover of all things science, trivia is like a playground for my mind. I'm particularly drawn to the Science category and Science & Nature. In my free time, I conduct science experiments and explore the natural world to deepen my trivia knowledge."
    )

    kurt = User(
        username='kurt',
        email='kurt@aa.io',
        password='password',
        description="Geography and trivia go hand in hand for me. I enjoy traveling and have a passion for exploring new cultures and places. Trivia helps me learn about the world's diverse regions and adds depth to my travel experiences."
    )

    luke = User(
        username='luke',
        email='luke@aa.io',
        password='password',
        description="For me, history is more than just a subject—it's a passion. I'm intrigued by historical events and figures, which is why I'm drawn to the History category in trivia. My hobbies include visiting historical sites and collecting rare artifacts."
    )

    jason = User(
        username='jason',
        email='jason@aa.io',
        password='password',
        description="I find trivia to be a great way to stay updated on pop culture. The Entertainment and Celebrities categories are my favorites. When I'm not answering trivia questions, I'm binge-watching the latest TV shows and following celebrity gossip."
    )


    db.session.add(demo)
    db.session.add(marnie)
    db.session.add(bobbie)
    db.session.add(tristan)
    db.session.add(johnny)
    db.session.add(jacob)
    db.session.add(albert)
    db.session.add(kurt)
    db.session.add(luke)
    db.session.add(jason)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()
