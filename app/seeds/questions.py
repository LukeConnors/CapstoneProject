from app.models import db, Question, environment, SCHEMA
from sqlalchemy.sql import text

def seed_questions():
#1
    general1 = Question(
        category="General Knowledge",
        type="multiple",
        difficulty="medium",
        question="Rolex is a company that specializes in what type of product?",
        correct_answer="Watches",
        incorrect_answers="Cars, Computers, Sports equipment"
    )
#2
    general2 = Question(
        category="General Knowledge",
        type="boolean",
        difficulty="easy",
        question="Video streaming website YouTube was purchased in its entirety by Facebook for US$1.65 billion in stock.",
        correct_answer="False",
        incorrect_answers="True"
    )
#3
    general3 = Question(
        category="General Knowledge",
        type="boolean",
        difficulty="medium",
        question="Typewriter is the longest word that can be typed using only the first row on a QWERTY keyboard.",
        correct_answer="True",
        incorrect_answers="False"
    )
#4
    general4 = Question(
        category="General Knowledge",
        type="boolean",
        difficulty="easy",
        question="Gumbo is a stew that originated in Louisiana.",
        correct_answer="True",
        incorrect_answers="False"
    )
#5
    general5 = Question(
        category="General Knowledge",
        type="multiple",
        difficulty="medium",
        question="What does the G mean in G-Man?",
        correct_answer="Government",
        incorrect_answers="Going, Ghost, Geronimo"
    )
#6
    general6 = Question(
        category="General Knowledge",
        type="multiple",
        difficulty="easy",
        question="What is the shape of the toy invented by Hungarian professor Ernő Rubik?",
        correct_answer="Cube",
        incorrect_answers="Sphere, Cylinder, Pyramid"
    )
#7
    general7 = Question(
        category="General Knowledge",
        type="multiple",
        difficulty="easy",
        question="Which one of the following rhythm games was made by Harmonix?",
        correct_answer="Rock Band",
        incorrect_answers="Meat Beat Mania, Guitar Hero Live, Dance Dance Revolution"
    )
#8
    general8 = Question(
        category="General Knowledge",
        type="boolean",
        difficulty="medium",
        question="Furby was released in 1998.",
        correct_answer="True",
        incorrect_answers="False"
    )
#9
    general9 = Question(
        category="General Knowledge",
        type="boolean",
        difficulty="easy",
        question="Nutella is produced by the German company Ferrero.",
        correct_answer="False",
        incorrect_answers="True"
    )
#10
    general10 = Question(
        category="General Knowledge",
        type="multiple",
        difficulty="easy",
        question="How many colors are there in a rainbow?",
        correct_answer="7",
        incorrect_answers="8, 9, 10"
    )

#11
    general11 = Question(
        category="General Knowledge",
        type="boolean",
        difficulty="medium",
        question="The bikini is named after the Bikini Atoll, an island where the United States conducted tests on atomic bombs.",
        correct_answer="True",
        incorrect_answers="False"
    )
#12
    general12 = Question(
        category="General Knowledge",
        type="boolean",
        difficulty="easy",
        question="Bulls are attracted to the color red.",
        correct_answer="False",
        incorrect_answers="True"
    )
#13
    general13 = Question(
        category="General Knowledge",
        type="boolean",
        difficulty="medium",
        question="You are allowed to sell your soul on eBay.",
        correct_answer="False",
        incorrect_answers="True"
    )
#14
    general14 = Question(
        category="General Knowledge",
        type="multiple",
        difficulty="medium",
        question="Which of these is the name of a Japanese system of alternative medicine, literally meaning finger pressure?",
        correct_answer="Shiatsu",
        incorrect_answers="Ukiyo, Majime, Ikigai"
    )
#15
    general15 = Question(
        category="General Knowledge",
        type="multiple",
        difficulty="easy",
        question="What was the nickname given to the Hughes H-4 Hercules, a heavy transport flying boat which achieved flight in 1947?",
        correct_answer="Spruce Goose",
        incorrect_answers="Noah's Ark, Fat Man, Trojan Horse"
    )
#16
    general16 = Question(
        category="General Knowledge",
        type="multiple",
        difficulty="medium",
        question="What is the name given to Indian food cooked over charcoal in a clay oven?",
        correct_answer="Tandoori",
        incorrect_answers="Biryani, Pani puri, Tiki masala"
    )
#17
    general17 = Question(
        category="General Knowledge",
        type="multiple",
        difficulty="medium",
        question="What is the name of the popular animatronic singing fish prop, singing such hits such as Don't Worry, Be Happy?",
        correct_answer="Big Mouth Billy Bass",
        incorrect_answers="Big Billy Bass, Singing Fish, Sardeen"
    )
#18
    general18 = Question(
        category="General Knowledge",
        type="boolean",
        difficulty="medium",
        question="The French word to travel is Travail",
        correct_answer="False",
        incorrect_answers="True"
    )
#19
    general19 = Question(
        category="General Knowledge",
        type="multiple",
        difficulty="medium",
        question="What year was Apple Inc. founded?",
        correct_answer="1976",
        incorrect_answers="1978, 1980, 1974"
    )
#
    general20 = Question(
        category="General Knowledge",
        type="multiple",
        difficulty="easy",
        question="What do the letters of the fast food chain KFC stand for?",
        correct_answer="Kentucky Fried Chicken",
        incorrect_answers="Kentucky Fresh Cheese, Kibbled Freaky Cow, Kiwi Food Cut"
    )
#
    general21 = Question(
        category="General Knowledge",
        type="multiple",
        difficulty="medium",
        question="Which of the General Mills Corporation's monster cereals was the last to be released in the 1970's?",
        correct_answer="Fruit Brute",
        incorrect_answers="Count Chocula, Franken Berry, Boo-Berry"
    )
#
    general22 = Question(
        category="General Knowledge",
        type="multiple",
        difficulty="easy",
        question="Which restaurant's mascot is a clown?",
        correct_answer="McDonald's",
        incorrect_answers="Whataburger, Burger King, Sonic"
    )
#
    general23 = Question(
        category="General Knowledge",
        type="multiple",
        difficulty="medium",
        question="What was the soft drink Pepsi originally introduced as?",
        correct_answer="Brad's Drink",
        incorrect_answers="Pepsin Pop, Carolina Cola, Pepsin Syrup"
    )
#
    general24 = Question(
        category="General Knowledge",
        type="boolean",
        difficulty="hard",
        question="Stagecoach owned South West Trains before losing the rights to FirstGroup and MTR in March of 2017.",
        correct_answer="True",
        incorrect_answers="False"
    )
#
    general25 = Question(
        category="General Knowledge",
        type="boolean",
        difficulty="hard",
        question="Spoon theory is a theory, utilizing Spoons as a metaphor for energy they can use in a day.",
        correct_answer="True",
        incorrect_answers="False"
    )
#
    general26 = Question(
        category="General Knowledge",
        type="multiple",
        difficulty="easy",
        question="What machine element is located in the center of fidget spinners?",
        correct_answer="Bearings",
        incorrect_answers="Axles, Gears, Belts"
    )
#
    general27 = Question(
        category="General Knowledge",
        type="multiple",
        difficulty="hard",
        question="Named after the mallow flower, mauve is a shade of what?",
        correct_answer="Purple",
        incorrect_answers="Red, Brown, Pink"
    )
#
    general28 = Question(
        category="General Knowledge",
        type="multiple",
        difficulty="hard",
        question="Chartreuse is a color between yellow and what?",
        correct_answer="Green",
        incorrect_answers="Red, Black, Purple"
    )
#
    general29 = Question(
        category="General Knowledge",
        type="multiple",
        difficulty="medium",
        question="Which of these words means idle spectator?",
        correct_answer="Gongoozler",
        incorrect_answers="Gossypiboma, Jentacular, Meupareunia"
    )
#
    general30 = Question(
        category="General Knowledge",
        type="multiple",
        difficulty="hard",
        question="Where is Apple Inc. headquartered?",
        correct_answer="Cupertino, California",
        incorrect_answers="Redwood City, California, Redmond, Washington, Santa Monica, CA"
    )
#
    general31 = Question(
        category="General Knowledge",
        type="multiple",
        difficulty="easy",
        question="What nuts are used in the production of marzipan?",
        correct_answer="Almonds",
        incorrect_answers="Peanuts, Walnuts, Pistachios"
    )
#
    general32 = Question(
        category="General Knowledge",
        type="boolean",
        difficulty="medium",
        question="Popcorn was invented in 1871 by Frederick W. Rueckheim in the USA where he sold the snack on the streets of Chicago.",
        correct_answer="False",
        incorrect_answers="True"
    )
#
    general33 = Question(
        category="General Knowledge",
        type="multiple",
        difficulty="medium",
        question="Which American manufactured submachine gun was informally known by the American soldiers that used it as Grease Gun?",
        correct_answer="M3",
        incorrect_answers="Colt 9mm, Thompson, MAC-10"
    )
#
    general34 = Question(
        category="General Knowledge",
        type="multiple",
        difficulty="medium",
        question="What is the highest number of Michelin stars a restaurant can receive?",
        correct_answer="Three",
        incorrect_answers="Four, Five, Six"
    )
#
    general35 = Question(
        category="General Knowledge",
        type="boolean",
        difficulty="easy",
        question="Slovakia is a member of European Union-",
        correct_answer="True",
        incorrect_answers="False"
    )
#
    general36 = Question(
        category="General Knowledge",
        type="multiple",
        difficulty="hard",
        question="The word aprosexia means which of the following?",
        correct_answer="The inability to concentrate on anything",
        incorrect_answers="The inability to make decisions, A feverish desire to rip one's clothes off, The inability to stand up"
    )
#
    general37 = Question(
        category="General Knowledge",
        type="multiple",
        difficulty="easy",
        question="What is the profession of Elon Musk's mom, Maye Musk?",
        correct_answer="Model",
        incorrect_answers="Professor, Biologist, Musician"
    )
#
    general38 = Question(
        category="General Knowledge",
        type="multiple",
        difficulty="medium",
        question="What fast food chain has the most locations globally? ",
        correct_answer="Subway",
        incorrect_answers="Starbucks, McDonalds, KFC"
    )
#
    general39 = Question(
        category="General Knowledge",
        type="multiple",
        difficulty="easy",
        question="What kind of aircraft was developed by Igor Sikorsky in the United States in 1942?",
        correct_answer="Helicopter",
        incorrect_answers="Stealth Blimp, Jet, Space Capsule"
    )
#40
    computers2 = Question(
        category="Science: Computers",
        type="multiple",
        difficulty="medium",
        question="What does LTS stand for in the software market?",
        correct_answer="Long Term Support",
        incorrect_answers="Long Taco Service, Ludicrous Transfer Speed, Ludicrous Turbo Speed"
    )

#41
    videogames3 = Question(
        category="Entertainment: Video Games",
        type="boolean",
        difficulty="easy",
        question="In Super Mario Bros., the clouds and bushes have the same artwork and are just different colors.",
        correct_answer="True",
        incorrect_answers="False"
    )

#42
    celebrities1 = Question(
        category="Celebrities",
        type="multiple",
        difficulty="medium",
        question="Which of these people is NOT a part of the Internet comedy group Mega64?",
        correct_answer="Jon Jafari",
        incorrect_answers="Rocco Botte, Derrick Acosta, Shawn Chatfield"
    )

#43
    science2 = Question(
        category="Science & Nature",
        type="multiple",
        difficulty="hard",
        question="Which of the following is NOT a real element?",
        correct_answer="Vitrainium",
        incorrect_answers="Praseodymium, Hassium, Lutetium"
    )

#44
    musicals1 = Question(
        category="Entertainment: Musicals & Theatres",
        type="multiple",
        difficulty="hard",
        question="What is the name of Broadway's first long-run musical?",
        correct_answer="The Elves",
        incorrect_answers="Wicked, Hamilton, The Book of Mormon"
    )

#45
    boardgames1 = Question(
        category="Entertainment: Board Games",
        type="boolean",
        difficulty="easy",
        question="The Angry Video Game Nerd's alter ego is Board James.",
        correct_answer="True",
        incorrect_answers="False"
    )

#46
    videogames4 = Question(
        category="Entertainment: Video Games",
        type="multiple",
        difficulty="medium",
        question="In Need For Speed: Most Wanted (2005), how many people are there to defeat on the blacklist?",
        correct_answer="15",
        incorrect_answers="5, 10, 20"
    )

#47
    books1 = Question(
        category="Entertainment: Books",
        type="multiple",
        difficulty="medium",
        question="The novel Of Mice And Men was written by what author? ",
        correct_answer="John Steinbeck ",
        incorrect_answers="George Orwell, Mark Twain, Harper Lee"
    )

#48
    videogames5 = Question(
        category="Entertainment: Video Games",
        type="multiple",
        difficulty="medium",
        question="In the game Paper Mario for the Nintendo 64 the first partner you meet is a Goomba, what is its name?",
        correct_answer="Goombario",
        incorrect_answers="Goombella, Goombarry, Goomby"
    )
# 49
    videogames6 = Question(
        category="Entertainment: Video Games",
        type="multiple",
        difficulty="easy",
        question="In PROTOTYPE 2. who is referred to as Tango Primary?",
        correct_answer="James Heller",
        incorrect_answers="Alex Mercer, Dana Mercer, Any Goliaths roaming around"
    )

#50
    anime1 = Question(
        category="Entertainment: Japanese Anime & Manga",
        type="multiple",
        difficulty="easy",
        question="In the anime Seven Deadly Sins what is the name of one of the sins?",
        correct_answer="Diane",
        incorrect_answers="Sakura, Ayano, Sheska"
    )

#51
    history1 = Question(
        category="History",
        type="multiple",
        difficulty="easy",
        question="What was the first sport to have been played on the moon?",
        correct_answer="Golf",
        incorrect_answers="Football, Tennis, Soccer"
    )

#52
    boardgames2 = Question(
        category="Entertainment: Board Games",
        type="multiple",
        difficulty="easy",
        question="The board game Monopoly takes its street names from which real American city?",
        correct_answer="Atlantic City, New Jersey",
        incorrect_answers="Las Vegas, Nevada, Duluth, Minnesota, Charleston, South Carolina"
    )

#53
    computers3 = Question(
        category="Science: Computers",
        type="multiple",
        difficulty="easy",
        question="What does LTS stand for in the software market?",
        correct_answer="Long Term Support",
        incorrect_answers="Long Taco Service, Ludicrous Transfer Speed, Ludicrous Turbo Speed"
    )
#54
    music2 = Question(
        category="Entertainment: Music",
        type="multiple",
        difficulty="medium",
        question="In what film was the Michael Jackson song Will You Be There featured?",
        correct_answer="Free Willy",
        incorrect_answers="Sleepless in Seattle, Men in Black, Bad Boys"
    )

#55
    videogames7 = Question(
        category="Entertainment: Video Games",
        type="multiple",
        difficulty="medium",
        question="Phil Fish was the designer of which game?",
        correct_answer="Fez",
        incorrect_answers="Super Meat Boy, Hotline Miami, FTL"
    )

#56
    history2 = Question(
        category="History",
        type="boolean",
        difficulty="easy",
        question="Kublai Khan is the grandchild of Genghis Khan?",
        correct_answer="True",
        incorrect_answers="False"
    )
#57
    science3 = Question(
        category="Science & Nature",
        type="multiple",
        difficulty="hard",
        question="What is the unit of electrical inductance?",
        correct_answer="Henry",
        incorrect_answers="Weber, Coulomb, Mho"
    )

#58
    videogames8 = Question(
        category="Entertainment: Video Games",
        type="multiple",
        difficulty="medium",
        question="What is the full name of the protagonist from the indie adventure game Night in the Woods?",
        correct_answer="Margaret Borowski",
        incorrect_answers="Marlena Woborski, Milena Catharina, Katia Managan"
    )

#59
    music3 = Question(
        category="Entertainment: Music",
        type="multiple",
        difficulty="medium",
        question="Who is the vocalist and frontman of rock band Guns N' Roses?",
        correct_answer="Axl Rose",
        incorrect_answers="Kurt Cobain, Slash, Bono"
    )
#60
    film2 = Question(
        category="Entertainment: Film",
        type="multiple",
        difficulty="medium",
        question="In Jurassic World, which company purchases InGen and creates Jurassic World?",
        correct_answer="Masrani Global Corporation ",
        incorrect_answers="Biology Synthetics Technologies, International Genetics Incorporated, International Genetic Technologies"
    )

#61
    cartoon1 = Question(
        category="Entertainment: Cartoon & Animations",
        type="multiple",
        difficulty="easy",
        question="Which of these characters live in a pineapple under the sea in the cartoon SpongeBob SquarePants.",
        correct_answer="SpongeBob SquarePants ",
        incorrect_answers="Patrick Star, Squidward Tentacles, Mr. Krabs"
    )

#62
    history3 = Question(
        category="History",
        type="boolean",
        difficulty="easy",
        question="The French Kingdom helped the United States gain their independence over Great Britain during the Revolutionary War.",
        correct_answer="True",
        incorrect_answers="False"
    )
#63
    videogames9 = Question(
        category="Entertainment: Video Games",
        type="multiple",
        difficulty="medium",
        question="What was the original release date of Grand Theft Auto V?",
        correct_answer="September 17, 2013",
        incorrect_answers="August 17, 2013, April 14, 2015, November 18, 2014"
    )

# 64
    geography3 = Question(
        category="Geography",
        type="multiple",
        difficulty="medium",
        question="What is the capital city of Slovenia?",
        correct_answer="Ljubljana",
        incorrect_answers="Maribor, Velenje, Trbovlje"
    )

#65
    general40 = Question(
        category="General Knowledge",
        type="multiple",
        difficulty="medium",
        question="Whose greyscale face is on the kappa emoticon on Twitch?",
        correct_answer="Josh DeSeno",
        incorrect_answers="Justin DeSeno, John DeSeno, Jimmy DeSeno"
    )

#66
    film3 = Question(
        category="Entertainment: Film",
        type="multiple",
        difficulty="medium",
        question="What is the name of the queen's pet in A Bug's Life?",
        correct_answer="Aphie",
        incorrect_answers="Flik, Hopper, Dot"
    )

#67
    gadgets1 = Question(
        category="Science: Gadgets",
        type="multiple",
        difficulty="easy",
        question="What round is a classic AK-47 chambered in?",
        correct_answer="7.62x39mm",
        incorrect_answers="7.62x51mm, 5.56x45mm, 5.45x39mm"
    )

#68
    videogames10 = Question(
        category="Entertainment: Video Games",
        type="multiple",
        difficulty="hard",
        question="What is the default name of the Vampire character in Shining Soul 2.",
        correct_answer="Bloodstar",
        incorrect_answers="Sachs, Dracuul, Alucard"
    )
#69
    science4 = Question(
        category="Science & Nature",
        type="multiple",
        difficulty="hard",
        question="What is Stenoma?",
        correct_answer="A genus of moths",
        incorrect_answers="A combat stimulant from WW2, A type of seasoning, A port city in the Caribbean"
    )

#70
    videogames11 = Question(
        category="Entertainment: Video Games",
        type="multiple",
        difficulty="medium",
        question="Which of these champions from the MOBA 'League of Legends' is NOT a Yordle?",
        correct_answer="Annie",
        incorrect_answers="Veigar, Tristana, Lulu"
    )

#71
    comics1 = Question(
        category="Entertainment: Comics",
        type="multiple",
        difficulty="medium",
        question="What is the real name of the Master Of Magnetism Magneto?",
        correct_answer="Max Eisenhardt",
        incorrect_answers="Charles Xavier, Pietro Maximoff, Johann Schmidt"
    )

#72
    anime2 = Question(
        category="Entertainment: Japanese Anime & Manga",
        type="multiple",
        difficulty="hard",
        question="Who was the Author of the manga Monster Hunter Orage?",
        correct_answer="Hiro Mashima",
        incorrect_answers="Shin Yamamoto, Keiichi Hikami, Hirohiko Araki"
    )

#73
    mythology1 = Question(
        category="Mythology",
        type="multiple",
        difficulty="medium",
        question="Which Greek god/goddess tossed a golden apple with the words for the fairest into the middle of the feast of the gods?",
        correct_answer="Eris",
        incorrect_answers="Hades, Ares, Artemis"
    )

#74
    computers4 = Question(
        category="Science: Computers",
        type="multiple",
        difficulty="medium",
        question="Unix Time is defined as the number of seconds that have elapsed since when?",
        correct_answer="00:00:00 UTC on 1 January 1970",
        incorrect_answers="00:00:00 UTC on 1 January 1960, 00:00:00 UTC on 1 January 1980, 00:00:00 UTC on 1 January 1990"
    )
#75
    anime3 = Question(
        category="Entertainment: Japanese Anime & Manga",
        type="multiple",
        difficulty="medium",
        question="In Toriko, what does the capture level refer to?",
        correct_answer="The difficulty of procuring or hunting down a particular ingredient",
        incorrect_answers="The difficulty of cooking a particular ingredient, The level of danger of a particular ingredient, The level of spiciness of a particular ingredient"
    )
#76
    gadgets2 = Question(
        category="Science: Gadgets",
        type="multiple",
        difficulty="medium",
        question="Which is NOT a feature of Apple Watch Series 7?",
        correct_answer="Built-in Breathalyzer",
        incorrect_answers="Fall detection, Blood Oxygen monitoring, ECG monitoring"
    )
#77
    general41 = Question(
        category="General Knowledge",
        type="multiple",
        difficulty="medium",
        question="Which planet in our solar system has the most gravity?",
        correct_answer="Jupiter",
        incorrect_answers="Earth, Saturn, Neptune"
    )
#78
    music4 = Question(
        category="Entertainment: Music",
        type="multiple",
        difficulty="medium",
        question="Which famous rapper was featured in 50 Cent's 2003 hit, In Da Club?",
        correct_answer="Eminem",
        incorrect_answers="Dr. Dre, Snoop Dogg, Jay-Z"
    )
#79
    books2 = Question(
        category="Entertainment: Books",
        type="multiple",
        difficulty="medium",
        question="What year was the book To Kill a Mockingbird published?",
        correct_answer="1960",
        incorrect_answers="1955, 1965, 1970"
    )
#80
    science5 = Question(
        category="Science & Nature",
        type="multiple",
        difficulty="medium",
        question="Which of the following is NOT a type of cell?",
        correct_answer="Neuronal Cells",
        incorrect_answers="Prokaryotes, Eukaryotes, Germline Cells"
    )

#81
    videogames12 = Question(
        category="Entertainment: Video Games",
        type="multiple",
        difficulty="medium",
        question="Which of these is NOT a game mode in Super Smash Bros. for Wii U?",
        correct_answer="Run Mode",
        incorrect_answers="Smash Tour, Crazy Orders, Master Orders"
    )

#82
    gadgets3 = Question(
        category="Science: Gadgets",
        type="multiple",
        difficulty="medium",
        question="What did Sir Isaac Newton use to explore the properties of light?",
        correct_answer="A Prism",
        incorrect_answers="A Telescope, A Microscope, A Mirror"
    )

#83
    film4 = Question(
        category="Entertainment: Film",
        type="multiple",
        difficulty="medium",
        question="What is the nickname of the stunt double that leads the motorcycle chase at the end of The Great Escape (1963)?",
        correct_answer="The Cooler King",
        incorrect_answers="The Bike Master, The Great Escape, The Stunt Master"
    )
#84
    computers5 = Question(
        category="Science: Computers",
        type="multiple",
        difficulty="medium",
        question="What was the first computer virus to be unleashed on the internet?",
        correct_answer="The Morris Worm",
        incorrect_answers="ILOVEYOU, Mydoom, Storm Worm"
    )
#85
    music5 = Question(
        category="Entertainment: Music",
        type="multiple",
        difficulty="medium",
        question="Which band released songs such as Rio and Hungry Like the Wolf?",
        correct_answer="Duran Duran",
        incorrect_answers="Wham!, A-ha, Tears for Fears"
    )

#86
    general42 = Question(
        category="General Knowledge",
        type="multiple",
        difficulty="medium",
        question="What is the name of the character that is a bear from the Star Wars series?",
        correct_answer="Wicket W. Warrick",
        incorrect_answers="Boba Fett, Lando Calrissian, Chewbacca"
    )

#87
    music6 = Question(
        category="Entertainment: Music",
        type="multiple",
        difficulty="medium",
        question="Which of these songs by the American singer Lady Gaga is not part of her debut studio album The Fame?",
        correct_answer="Born This Way",
        incorrect_answers="Just Dance, Poker Face, LoveGame"
    )
#88
    computers6 = Question(
        category="Science: Computers",
        type="multiple",
        difficulty="easy",
        question="What does the 'MP' stand for in MP3?",
        correct_answer="MPEG Audio Layer",
        incorrect_answers="Multi-Player, Many Plays, Multiple Precussions"
    )




    db.session.add_all([
        general1, general2, general3, general4, general5, general6, general7, general8, general9, general10,
        general11, general12, general13, general14, general15, general16, general17, general18, general19, general20,
        general21, general22, general23, general24, general25, general26, general27, general28, general29, general30,
        general31, general32, general33, general34, general35, general36, general37, general38, general39, computers2,
        videogames3, celebrities1, science2, musicals1, boardgames1, videogames4, books1, videogames5,
        videogames6, anime1, history1, boardgames2, computers3, music2, videogames7, history2, science3, videogames8,
        music3, film2, cartoon1, history3, videogames9, geography3, general40, film3, gadgets1, videogames10, science4,
        videogames11, comics1, anime2, mythology1, computers4, anime3, gadgets2, general41, music4, books2, science5,
        videogames12, gadgets3, film4, computers5, music5, general42, music6, computers6,
    ])


    db.session.commit()

def undo_questions():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.questions RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM questions"))

    db.session.commit()
