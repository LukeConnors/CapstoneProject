from app.models import db, Question, environment, SCHEMA
from sqlalchemy.sql import text

def seed_questions():
#1
    general1 = Question(
        owner_id=1,
        category="General Knowledge",
        type="multiple",
        difficulty="medium",
        question="Rolex is a company that specializes in what type of product?",
        correct_answer="Watches",
        incorrect_answers="Cars, Computers, Sports equipment"
    )
#2
    general2 = Question(
        owner_id=1,
        category="General Knowledge",
        type="boolean",
        difficulty="easy",
        question="Video streaming website YouTube was purchased in its entirety by Facebook for US$1.65 billion in stock.",
        correct_answer="False",
        incorrect_answers="True"
    )
#3
    general3 = Question( owner_id=3,
        category="General Knowledge",
        type="boolean",
        difficulty="medium",
        question="Typewriter is the longest word that can be typed using only the first row on a QWERTY keyboard.",
        correct_answer="True",
        incorrect_answers="False"
    )
#4
    general4 = Question( owner_id=4,
        category="General Knowledge",
        type="boolean",
        difficulty="easy",
        question="Gumbo is a stew that originated in Louisiana.",
        correct_answer="True",
        incorrect_answers="False"
    )
#5
    general5 = Question( owner_id=5,
        category="General Knowledge",
        type="multiple",
        difficulty="medium",
        question="What does the G mean in G-Man?",
        correct_answer="Government",
        incorrect_answers="Going, Ghost, Geronimo"
    )
#6
    general6 = Question( owner_id=6,
        category="General Knowledge",
        type="multiple",
        difficulty="easy",
        question="What is the shape of the toy invented by Hungarian professor Ernő Rubik?",
        correct_answer="Cube",
        incorrect_answers="Sphere, Cylinder, Pyramid"
    )
#7
    general7 = Question( owner_id=7,
        category="General Knowledge",
        type="multiple",
        difficulty="easy",
        question="Which one of the following rhythm games was made by Harmonix?",
        correct_answer="Rock Band",
        incorrect_answers="Meat Beat Mania, Guitar Hero Live, Dance Dance Revolution"
    )
#8
    general8 = Question( owner_id=5,
        category="General Knowledge",
        type="boolean",
        difficulty="medium",
        question="Furby was released in 1998.",
        correct_answer="True",
        incorrect_answers="False"
    )
#9
    general9 = Question( owner_id=4,
        category="General Knowledge",
        type="boolean",
        difficulty="easy",
        question="Nutella is produced by the German company Ferrero.",
        correct_answer="False",
        incorrect_answers="True"
    )
#10
    general10 = Question( owner_id=3,
        category="General Knowledge",
        type="multiple",
        difficulty="easy",
        question="How many colors are there in a rainbow?",
        correct_answer="7",
        incorrect_answers="8, 9, 10"
    )

#11
    general11 = Question( owner_id=6,
        category="General Knowledge",
        type="boolean",
        difficulty="medium",
        question="The bikini is named after the Bikini Atoll, an island where the United States conducted tests on atomic bombs.",
        correct_answer="True",
        incorrect_answers="False"
    )
#12
    general12 = Question( owner_id=7,
        category="General Knowledge",
        type="boolean",
        difficulty="easy",
        question="Bulls are attracted to the color red.",
        correct_answer="False",
        incorrect_answers="True"
    )
#13
    general13 = Question( owner_id=7,
        category="General Knowledge",
        type="boolean",
        difficulty="medium",
        question="You are allowed to sell your soul on eBay.",
        correct_answer="False",
        incorrect_answers="True"
    )
#14
    general14 = Question( owner_id=8,
        category="General Knowledge",
        type="multiple",
        difficulty="medium",
        question="Which of these is the name of a Japanese system of alternative medicine, literally meaning finger pressure?",
        correct_answer="Shiatsu",
        incorrect_answers="Ukiyo, Majime, Ikigai"
    )
#15
    general15 = Question( owner_id=9,
        category="General Knowledge",
        type="multiple",
        difficulty="easy",
        question="What was the nickname given to the Hughes H-4 Hercules, a heavy transport flying boat which achieved flight in 1947?",
        correct_answer="Spruce Goose",
        incorrect_answers="Noah's Ark, Fat Man, Trojan Horse"
    )
#16
    general16 = Question( owner_id=2,
        category="General Knowledge",
        type="multiple",
        difficulty="medium",
        question="What is the name given to Indian food cooked over charcoal in a clay oven?",
        correct_answer="Tandoori",
        incorrect_answers="Biryani, Pani puri, Tiki masala"
    )
#17
    general17 = Question( owner_id=1,
        category="General Knowledge",
        type="multiple",
        difficulty="medium",
        question="What is the name of the popular animatronic singing fish prop, singing such hits such as Don't Worry, Be Happy?",
        correct_answer="Big Mouth Billy Bass",
        incorrect_answers="Big Billy Bass, Singing Fish, Sardeen"
    )
#18
    general18 = Question( owner_id=3,
        category="General Knowledge",
        type="boolean",
        difficulty="medium",
        question="The French word to travel is Travail",
        correct_answer="False",
        incorrect_answers="True"
    )
#19
    general19 = Question( owner_id=3,
        category="General Knowledge",
        type="multiple",
        difficulty="medium",
        question="What year was Apple Inc. founded?",
        correct_answer="1976",
        incorrect_answers="1978, 1980, 1974"
    )
#
    general20 = Question( owner_id=4,
        category="General Knowledge",
        type="multiple",
        difficulty="easy",
        question="What do the letters of the fast food chain KFC stand for?",
        correct_answer="Kentucky Fried Chicken",
        incorrect_answers="Kentucky Fresh Cheese, Kibbled Freaky Cow, Kiwi Food Cut"
    )
#
    general21 = Question( owner_id=5,
        category="General Knowledge",
        type="multiple",
        difficulty="medium",
        question="Which of the General Mills Corporation's monster cereals was the last to be released in the 1970's?",
        correct_answer="Fruit Brute",
        incorrect_answers="Count Chocula, Franken Berry, Boo-Berry"
    )
#
    general22 = Question( owner_id=1,
        category="General Knowledge",
        type="multiple",
        difficulty="easy",
        question="Which restaurant's mascot is a clown?",
        correct_answer="McDonald's",
        incorrect_answers="Whataburger, Burger King, Sonic"
    )
#
    general23 = Question( owner_id=2,
        category="General Knowledge",
        type="multiple",
        difficulty="medium",
        question="What was the soft drink Pepsi originally introduced as?",
        correct_answer="Brad's Drink",
        incorrect_answers="Pepsin Pop, Carolina Cola, Pepsin Syrup"
    )
#
    general24 = Question( owner_id=8,
        category="General Knowledge",
        type="boolean",
        difficulty="hard",
        question="Stagecoach owned South West Trains before losing the rights to FirstGroup and MTR in March of 2017.",
        correct_answer="True",
        incorrect_answers="False"
    )
#
    general25 = Question( owner_id=4,
        category="General Knowledge",
        type="boolean",
        difficulty="hard",
        question="Spoon theory is a theory, utilizing Spoons as a metaphor for energy they can use in a day.",
        correct_answer="True",
        incorrect_answers="False"
    )
#
    general26 = Question( owner_id=5,
        category="General Knowledge",
        type="multiple",
        difficulty="easy",
        question="What machine element is located in the center of fidget spinners?",
        correct_answer="Bearings",
        incorrect_answers="Axles, Gears, Belts"
    )
#
    general27 = Question( owner_id=6,
        category="General Knowledge",
        type="multiple",
        difficulty="hard",
        question="Named after the mallow flower, mauve is a shade of what?",
        correct_answer="Purple",
        incorrect_answers="Red, Brown, Pink"
    )
#
    general28 = Question( owner_id=3,
        category="General Knowledge",
        type="multiple",
        difficulty="hard",
        question="Chartreuse is a color between yellow and what?",
        correct_answer="Green",
        incorrect_answers="Red, Black, Purple"
    )
#
    general29 = Question( owner_id=1,
        category="General Knowledge",
        type="multiple",
        difficulty="medium",
        question="Which of these words means idle spectator?",
        correct_answer="Gongoozler",
        incorrect_answers="Gossypiboma, Jentacular, Meupareunia"
    )
#
    general30 = Question( owner_id=3,
        category="General Knowledge",
        type="multiple",
        difficulty="hard",
        question="Where is Apple Inc. headquartered?",
        correct_answer="Cupertino, California",
        incorrect_answers="Redwood City, California, Redmond, Washington, Santa Monica, CA"
    )
#
    general31 = Question( owner_id=2,
        category="General Knowledge",
        type="multiple",
        difficulty="easy",
        question="What nuts are used in the production of marzipan?",
        correct_answer="Almonds",
        incorrect_answers="Peanuts, Walnuts, Pistachios"
    )
#
    general32 = Question( owner_id=10,
        category="General Knowledge",
        type="boolean",
        difficulty="medium",
        question="Popcorn was invented in 1871 by Frederick W. Rueckheim in the USA where he sold the snack on the streets of Chicago.",
        correct_answer="False",
        incorrect_answers="True"
    )
#
    general33 = Question( owner_id=9,
        category="General Knowledge",
        type="multiple",
        difficulty="medium",
        question="Which American manufactured submachine gun was informally known by the American soldiers that used it as Grease Gun?",
        correct_answer="M3",
        incorrect_answers="Colt 9mm, Thompson, MAC-10"
    )
#
    general34 = Question( owner_id=8,
        category="General Knowledge",
        type="multiple",
        difficulty="medium",
        question="What is the highest number of Michelin stars a restaurant can receive?",
        correct_answer="Three",
        incorrect_answers="Four, Five, Six"
    )
#
    general35 = Question( owner_id=5,
        category="General Knowledge",
        type="boolean",
        difficulty="easy",
        question="Slovakia is a member of European Union-",
        correct_answer="True",
        incorrect_answers="False"
    )
#
    general36 = Question( owner_id=5,
        category="General Knowledge",
        type="multiple",
        difficulty="hard",
        question="The word aprosexia means which of the following?",
        correct_answer="The inability to concentrate on anything",
        incorrect_answers="The inability to make decisions, A feverish desire to rip one's clothes off, The inability to stand up"
    )
#
    general37 = Question( owner_id=2,
        category="General Knowledge",
        type="multiple",
        difficulty="easy",
        question="What is the profession of Elon Musk's mom, Maye Musk?",
        correct_answer="Model",
        incorrect_answers="Professor, Biologist, Musician"
    )
#
    general38 = Question( owner_id=2,
        category="General Knowledge",
        type="multiple",
        difficulty="medium",
        question="What fast food chain has the most locations globally? ",
        correct_answer="Subway",
        incorrect_answers="Starbucks, McDonalds, KFC"
    )
#
    general39 = Question( owner_id=1,
        category="General Knowledge",
        type="multiple",
        difficulty="easy",
        question="What kind of aircraft was developed by Igor Sikorsky in the United States in 1942?",
        correct_answer="Helicopter",
        incorrect_answers="Stealth Blimp, Jet, Space Capsule"
    )
#40
    computers2 = Question( owner_id=2,
        category="Science: Computers",
        type="multiple",
        difficulty="medium",
        question="What does LTS stand for in the software market?",
        correct_answer="Long Term Support",
        incorrect_answers="Long Taco Service, Ludicrous Transfer Speed, Ludicrous Turbo Speed"
    )

#41
    videogames3 = Question( owner_id=6,
        category="Entertainment: Video Games",
        type="boolean",
        difficulty="easy",
        question="In Super Mario Bros., the clouds and bushes have the same artwork and are just different colors.",
        correct_answer="True",
        incorrect_answers="False"
    )

#42
    celebrities1 = Question( owner_id=4,
        category="Celebrities",
        type="multiple",
        difficulty="medium",
        question="Which of these people is NOT a part of the Internet comedy group Mega64?",
        correct_answer="Jon Jafari",
        incorrect_answers="Rocco Botte, Derrick Acosta, Shawn Chatfield"
    )

#43
    science2 = Question( owner_id=3,
        category="Science & Nature",
        type="multiple",
        difficulty="hard",
        question="Which of the following is NOT a real element?",
        correct_answer="Vitrainium",
        incorrect_answers="Praseodymium, Hassium, Lutetium"
    )

#44
    musicals1 = Question( owner_id=1,
        category="Entertainment: Musicals & Theatres",
        type="multiple",
        difficulty="hard",
        question="What is the name of Broadway's first long-run musical?",
        correct_answer="The Elves",
        incorrect_answers="Wicked, Hamilton, The Book of Mormon"
    )

#45
    boardgames1 = Question( owner_id=10,
        category="Entertainment: Board Games",
        type="boolean",
        difficulty="easy",
        question="The Angry Video Game Nerd's alter ego is Board James.",
        correct_answer="True",
        incorrect_answers="False"
    )

#46
    videogames4 = Question( owner_id=8,
        category="Entertainment: Video Games",
        type="multiple",
        difficulty="medium",
        question="In Need For Speed: Most Wanted (2005), how many people are there to defeat on the blacklist?",
        correct_answer="15",
        incorrect_answers="5, 10, 20"
    )

#47
    books1 = Question( owner_id=10,
        category="Entertainment: Books",
        type="multiple",
        difficulty="medium",
        question="The novel Of Mice And Men was written by what author? ",
        correct_answer="John Steinbeck ",
        incorrect_answers="George Orwell, Mark Twain, Harper Lee"
    )

#48
    videogames5 = Question( owner_id=3,
        category="Entertainment: Video Games",
        type="multiple",
        difficulty="medium",
        question="In the game Paper Mario for the Nintendo 64 the first partner you meet is a Goomba, what is its name?",
        correct_answer="Goombario",
        incorrect_answers="Goombella, Goombarry, Goomby"
    )
# 49
    videogames6 = Question( owner_id=6,
        category="Entertainment: Video Games",
        type="multiple",
        difficulty="easy",
        question="In PROTOTYPE 2. who is referred to as Tango Primary?",
        correct_answer="James Heller",
        incorrect_answers="Alex Mercer, Dana Mercer, Any Goliaths roaming around"
    )

#50
    anime1 = Question( owner_id=3,
        category="Entertainment: Japanese Anime & Manga",
        type="multiple",
        difficulty="easy",
        question="In the anime Seven Deadly Sins what is the name of one of the sins?",
        correct_answer="Diane",
        incorrect_answers="Sakura, Ayano, Sheska"
    )

#51
    history1 = Question( owner_id=2,
        category="History",
        type="multiple",
        difficulty="easy",
        question="What was the first sport to have been played on the moon?",
        correct_answer="Golf",
        incorrect_answers="Football, Tennis, Soccer"
    )

#52
    boardgames2 = Question( owner_id=6,
        category="Entertainment: Board Games",
        type="multiple",
        difficulty="easy",
        question="The board game Monopoly takes its street names from which real American city?",
        correct_answer="Atlantic City, New Jersey",
        incorrect_answers="Las Vegas, Nevada, Duluth, Minnesota, Charleston, South Carolina"
    )

#53
    computers3 = Question( owner_id=7,
        category="Science: Computers",
        type="multiple",
        difficulty="easy",
        question="What does LTS stand for in the software market?",
        correct_answer="Long Term Support",
        incorrect_answers="Long Taco Service, Ludicrous Transfer Speed, Ludicrous Turbo Speed"
    )
#54
    music2 = Question( owner_id=3,
        category="Entertainment: Music",
        type="multiple",
        difficulty="medium",
        question="In what film was the Michael Jackson song Will You Be There featured?",
        correct_answer="Free Willy",
        incorrect_answers="Sleepless in Seattle, Men in Black, Bad Boys"
    )

#55
    videogames7 = Question( owner_id=2,
        category="Entertainment: Video Games",
        type="multiple",
        difficulty="medium",
        question="Phil Fish was the designer of which game?",
        correct_answer="Fez",
        incorrect_answers="Super Meat Boy, Hotline Miami, FTL"
    )

#56
    history2 = Question( owner_id=4,
        category="History",
        type="boolean",
        difficulty="easy",
        question="Kublai Khan is the grandchild of Genghis Khan?",
        correct_answer="True",
        incorrect_answers="False"
    )
#57
    science3 = Question( owner_id=5,
        category="Science & Nature",
        type="multiple",
        difficulty="hard",
        question="What is the unit of electrical inductance?",
        correct_answer="Henry",
        incorrect_answers="Weber, Coulomb, Mho"
    )

#58
    videogames8 = Question( owner_id=5,
        category="Entertainment: Video Games",
        type="multiple",
        difficulty="medium",
        question="What is the full name of the protagonist from the indie adventure game Night in the Woods?",
        correct_answer="Margaret Borowski",
        incorrect_answers="Marlena Woborski, Milena Catharina, Katia Managan"
    )

#59
    music3 = Question( owner_id=10,
        category="Entertainment: Music",
        type="multiple",
        difficulty="medium",
        question="Who is the vocalist and frontman of rock band Guns N' Roses?",
        correct_answer="Axl Rose",
        incorrect_answers="Kurt Cobain, Slash, Bono"
    )
#60
    film2 = Question( owner_id=8,
        category="Entertainment: Film",
        type="multiple",
        difficulty="medium",
        question="In Jurassic World, which company purchases InGen and creates Jurassic World?",
        correct_answer="Masrani Global Corporation ",
        incorrect_answers="Biology Synthetics Technologies, International Genetics Incorporated, International Genetic Technologies"
    )

#61
    cartoon1 = Question( owner_id=9,
        category="Entertainment: Cartoon & Animations",
        type="multiple",
        difficulty="easy",
        question="Which of these characters live in a pineapple under the sea in the cartoon SpongeBob SquarePants.",
        correct_answer="SpongeBob SquarePants ",
        incorrect_answers="Patrick Star, Squidward Tentacles, Mr. Krabs"
    )

#62
    history3 = Question( owner_id=2,
        category="History",
        type="boolean",
        difficulty="easy",
        question="The French Kingdom helped the United States gain their independence over Great Britain during the Revolutionary War.",
        correct_answer="True",
        incorrect_answers="False"
    )
#63
    videogames9 = Question( owner_id=3,
        category="Entertainment: Video Games",
        type="multiple",
        difficulty="medium",
        question="What was the original release date of Grand Theft Auto V?",
        correct_answer="September 17, 2013",
        incorrect_answers="August 17, 2013, April 14, 2015, November 18, 2014"
    )

# 64
    geography3 = Question( owner_id=4,
        category="Geography",
        type="multiple",
        difficulty="medium",
        question="What is the capital city of Slovenia?",
        correct_answer="Ljubljana",
        incorrect_answers="Maribor, Velenje, Trbovlje"
    )

#65
    general40 = Question( owner_id=4,
        category="General Knowledge",
        type="multiple",
        difficulty="medium",
        question="Whose greyscale face is on the kappa emoticon on Twitch?",
        correct_answer="Josh DeSeno",
        incorrect_answers="Justin DeSeno, John DeSeno, Jimmy DeSeno"
    )

#66
    film3 = Question( owner_id=1,
        category="Entertainment: Film",
        type="multiple",
        difficulty="medium",
        question="What is the name of the queen's pet in A Bug's Life?",
        correct_answer="Aphie",
        incorrect_answers="Flik, Hopper, Dot"
    )

#67
    gadgets1 = Question( owner_id=10,
        category="Science: Gadgets",
        type="multiple",
        difficulty="easy",
        question="What round is a classic AK-47 chambered in?",
        correct_answer="7.62x39mm",
        incorrect_answers="7.62x51mm, 5.56x45mm, 5.45x39mm"
    )

#68
    videogames10 = Question( owner_id=6,
        category="Entertainment: Video Games",
        type="multiple",
        difficulty="hard",
        question="What is the default name of the Vampire character in Shining Soul 2.",
        correct_answer="Bloodstar",
        incorrect_answers="Sachs, Dracuul, Alucard"
    )
#69
    science4 = Question( owner_id=3,
        category="Science & Nature",
        type="multiple",
        difficulty="hard",
        question="What is Stenoma?",
        correct_answer="A genus of moths",
        incorrect_answers="A combat stimulant from WW2, A type of seasoning, A port city in the Caribbean"
    )

#70
    videogames11 = Question( owner_id=4,
        category="Entertainment: Video Games",
        type="multiple",
        difficulty="medium",
        question="Which of these champions from the MOBA 'League of Legends' is NOT a Yordle?",
        correct_answer="Annie",
        incorrect_answers="Veigar, Tristana, Lulu"
    )

#71
    comics1 = Question( owner_id=8,
        category="Entertainment: Comics",
        type="multiple",
        difficulty="medium",
        question="What is the real name of the Master Of Magnetism Magneto?",
        correct_answer="Max Eisenhardt",
        incorrect_answers="Charles Xavier, Pietro Maximoff, Johann Schmidt"
    )

#72
    anime2 = Question( owner_id=10,
        category="Entertainment: Japanese Anime & Manga",
        type="multiple",
        difficulty="hard",
        question="Who was the Author of the manga Monster Hunter Orage?",
        correct_answer="Hiro Mashima",
        incorrect_answers="Shin Yamamoto, Keiichi Hikami, Hirohiko Araki"
    )

#73
    mythology1 = Question( owner_id=7,
        category="Mythology",
        type="multiple",
        difficulty="medium",
        question="Which Greek god/goddess tossed a golden apple with the words for the fairest into the middle of the feast of the gods?",
        correct_answer="Eris",
        incorrect_answers="Hades, Ares, Artemis"
    )

#74
    computers4 = Question( owner_id=3,
        category="Science: Computers",
        type="multiple",
        difficulty="medium",
        question="Unix Time is defined as the number of seconds that have elapsed since when?",
        correct_answer="00:00:00 UTC on 1 January 1970",
        incorrect_answers="00:00:00 UTC on 1 January 1960, 00:00:00 UTC on 1 January 1980, 00:00:00 UTC on 1 January 1990"
    )
#75
    anime3 = Question( owner_id=1,
        category="Entertainment: Japanese Anime & Manga",
        type="multiple",
        difficulty="medium",
        question="In Toriko, what does the capture level refer to?",
        correct_answer="The difficulty of procuring or hunting down a particular ingredient",
        incorrect_answers="The difficulty of cooking a particular ingredient, The level of danger of a particular ingredient, The level of spiciness of a particular ingredient"
    )
#76
    gadgets2 = Question( owner_id=6,
        category="Science: Gadgets",
        type="multiple",
        difficulty="medium",
        question="Which is NOT a feature of Apple Watch Series 7?",
        correct_answer="Built-in Breathalyzer",
        incorrect_answers="Fall detection, Blood Oxygen monitoring, ECG monitoring"
    )
#77
    general41 = Question( owner_id=1,
        category="General Knowledge",
        type="multiple",
        difficulty="medium",
        question="Which planet in our solar system has the most gravity?",
        correct_answer="Jupiter",
        incorrect_answers="Earth, Saturn, Neptune"
    )
#78
    music4 = Question( owner_id=8,
        category="Entertainment: Music",
        type="multiple",
        difficulty="medium",
        question="Which famous rapper was featured in 50 Cent's 2003 hit, In Da Club?",
        correct_answer="Eminem",
        incorrect_answers="Dr. Dre, Snoop Dogg, Jay-Z"
    )
#79
    books2 = Question( owner_id=9,
        category="Entertainment: Books",
        type="multiple",
        difficulty="medium",
        question="What year was the book To Kill a Mockingbird published?",
        correct_answer="1960",
        incorrect_answers="1955, 1965, 1970"
    )
#80
    science5 = Question( owner_id=10,
        category="Science & Nature",
        type="multiple",
        difficulty="medium",
        question="Which of the following is NOT a type of cell?",
        correct_answer="Neuronal Cells",
        incorrect_answers="Prokaryotes, Eukaryotes, Germline Cells"
    )

#81
    videogames12 = Question( owner_id=2,
        category="Entertainment: Video Games",
        type="multiple",
        difficulty="medium",
        question="Which of these is NOT a game mode in Super Smash Bros. for Wii U?",
        correct_answer="Run Mode",
        incorrect_answers="Smash Tour, Crazy Orders, Master Orders"
    )

#82
    gadgets3 = Question( owner_id=4,
        category="Science: Gadgets",
        type="multiple",
        difficulty="medium",
        question="What did Sir Isaac Newton use to explore the properties of light?",
        correct_answer="A Prism",
        incorrect_answers="A Telescope, A Microscope, A Mirror"
    )

#83
    film4 = Question( owner_id=5,
        category="Entertainment: Film",
        type="multiple",
        difficulty="medium",
        question="What is the nickname of the stunt double that leads the motorcycle chase at the end of The Great Escape (1963)?",
        correct_answer="The Cooler King",
        incorrect_answers="The Bike Master, The Great Escape, The Stunt Master"
    )
#84
    computers5 = Question( owner_id=7,
        category="Science: Computers",
        type="multiple",
        difficulty="medium",
        question="What was the first computer virus to be unleashed on the internet?",
        correct_answer="The Morris Worm",
        incorrect_answers="ILOVEYOU, Mydoom, Storm Worm"
    )
#85
    music5 = Question( owner_id=1,
        category="Entertainment: Music",
        type="multiple",
        difficulty="medium",
        question="Which band released songs such as Rio and Hungry Like the Wolf?",
        correct_answer="Duran Duran",
        incorrect_answers="Wham!, A-ha, Tears for Fears"
    )

#86
    general42 = Question( owner_id=10,
        category="General Knowledge",
        type="multiple",
        difficulty="medium",
        question="What is the name of the character that is a bear from the Star Wars series?",
        correct_answer="Wicket W. Warrick",
        incorrect_answers="Boba Fett, Lando Calrissian, Chewbacca"
    )

#87
    music6 = Question( owner_id=4,
        category="Entertainment: Music",
        type="multiple",
        difficulty="medium",
        question="Which of these songs by the American singer Lady Gaga is not part of her debut studio album The Fame?",
        correct_answer="Born This Way",
        incorrect_answers="Just Dance, Poker Face, LoveGame"
    )
#88
    computers6 = Question( owner_id=5,
        category="Science: Computers",
        type="multiple",
        difficulty="easy",
        question="What does the 'MP' stand for in MP3?",
        correct_answer="MPEG Audio Layer",
        incorrect_answers="Multi-Player, Many Plays, Multiple Precussions"
    )

    # 89
    musicals2 = Question(
        owner_id=3,
        category="Entertainment: Musicals & Theatres",
        type="multiple",
        difficulty="medium",
        question="When was the play \"Macbeth\" written?",
        correct_answer="1606",
        incorrect_answers="1605, 1723, 1628"
    )
# 90
    musicals3 = Question(
        owner_id=7,
        category="Entertainment: Musicals & Theatres",
        type="multiple",
        difficulty="hard",
        question="Who wrote the lyrics for Leonard Bernstein's 1957 Broadway musical West Side Story?",
        correct_answer="Stephen Sondheim",
        incorrect_answers="Himself, Oscar Hammerstein, Richard Rodgers"
    )
# 91
    musicals4 = Question(
        owner_id=5,
        category="Entertainment: Musicals & Theatres",
        type="multiple",
        difficulty="hard",
        question="Who serves as the speaker of the prologue in Shakespeare's Romeo and Juliet?",
        correct_answer="Chorus",
        incorrect_answers="Montague, Refrain, Capulet"
    )
# 92
    musicals5 = Question(
        owner_id=9,
        category="Entertainment: Musicals & Theatres",
        type="multiple",
        difficulty="medium",
        question="The musical \"Dirty Rotten Scoundrels\" is set in what country?",
        correct_answer="France",
        incorrect_answers="USA, Germany, Sweden"
    )
# 93
    musicals6 = Question(
        owner_id=2,
        category="Entertainment: Musicals & Theatres",
        type="multiple",
        difficulty="hard",
        question="Which Shakespeare play features the stage direction \"Enter a messenger, with two heads and a hand\"?",
        correct_answer="Titus Andronicus",
        incorrect_answers="Othello, Macbeth, King Lear"
    )
# 94
    books3 = Question(
    owner_id=4,
    category="Entertainment: Books",
    type="multiple",
    difficulty="hard",
    question="Where does the book \"The Silence of the Lambs\" get its title from?",
    correct_answer="The main character's trauma in childhood",
    incorrect_answers="The relation it has with killing the innocents, The villain's favourite meal, The voice of innocent people being shut by the powerful"
    )
#95
    books4 = Question(
        owner_id=8,
        category="Entertainment: Books",
        type="multiple",
        difficulty="medium",
        question="What book series published by Jim Butcher follows a wizard in modern-day Chicago?",
        correct_answer="The Dresden Files",
        incorrect_answers="A Hat in Time, The Cinder Spires, My Life as a Teenage Wizard"
    )
#96
    books5 = Question(
        owner_id=6,
        category="Entertainment: Books",
        type="multiple",
        difficulty="medium",
        question="In Terry Pratchett's Discworld novel 'Wyrd Sisters', which of these is not one of the three main witches?",
        correct_answer="Winny Hathersham",
        incorrect_answers="Granny Weatherwax, Nanny Ogg, Magrat Garlick"
    )
#97
    books6 = Question(
        owner_id=10,
        category="Entertainment: Books",
        type="multiple",
        difficulty="easy",
        question="Under what pseudonym did Stephen King publish five novels between 1977 and 1984?",
        correct_answer="Richard Bachman",
        incorrect_answers="J. D. Robb, Mark Twain, Lewis Carroll"
    )
#98
    books7 = Question(
        owner_id=2,
        category="Entertainment: Books",
        type="multiple",
        difficulty="medium",
        question="J.K. Rowling completed \"Harry Potter and the Deathly Hallows\" in which hotel in Edinburgh, Scotland?",
        correct_answer="The Balmoral",
        incorrect_answers="The Dunstane Hotel, Hotel Novotel, Sheraton Grand Hotel & Spa"
    )
# 99
    celebrities2 = Question(
        owner_id=4,
        category="Celebrities",
        type="multiple",
        difficulty="easy",
        question="By what name is Carlos Estevez better known?",
        correct_answer="Charlie Sheen",
        incorrect_answers="Ricky Martin, Bruno Mars, Joaquin Phoenix"
    )
# 100
    celebrities3 = Question(
        owner_id=8,
        category="Celebrities",
        type="multiple",
        difficulty="medium",
        question="When was Elvis Presley born?",
        correct_answer="January 8, 1935",
        incorrect_answers="December 13, 1931, July 18, 1940, April 17, 1938"
    )
# 101
    celebrities4 = Question(
        owner_id=6,
        category="Celebrities",
        type="boolean",
        difficulty="easy",
        question="Marilyn Monroe was born on July 1, 1926.",
        correct_answer="False",
        incorrect_answers="True"
    )
# 102
    celebrities5 = Question(
        owner_id=10,
        category="Celebrities",
        type="multiple",
        difficulty="easy",
        question="By which name is Ramon Estevez better known as?",
        correct_answer="Martin Sheen",
        incorrect_answers="Charlie Sheen, Ramon Sheen, Emilio Estevez"
    )
# 103
    celebrities6 = Question(
        owner_id=2,
        category="Celebrities",
        type="multiple",
        difficulty="medium",
        question="What year was O.J. Simpson acquitted of his murder charges?",
        correct_answer="1995",
        incorrect_answers="1992, 1996, 1991"
    )
# 104
    boardgames3 = Question(
        owner_id=4,
        category="Entertainment: Board Games",
        type="multiple",
        difficulty="hard",
        question="The board game \"Monopoly\" is a variation of what board game?",
        correct_answer="The Landlord's Game",
        incorrect_answers="Territorial Dispute, Property Feud, The Monopolist's Game"
    )
# 105
    boardgames4 = Question(
        owner_id=8,
        category="Entertainment: Board Games",
        type="multiple",
        difficulty="easy",
        question="How many pieces are there on the board at the start of a game of chess?",
        correct_answer="32",
        incorrect_answers="16, 20, 36"
    )
# 106
    boardgames5 = Question(
        owner_id=6,
        category="Entertainment: Board Games",
        type="multiple",
        difficulty="medium",
        question="In Chess, the Queen has the combined movement of which two pieces?",
        correct_answer="Bishop and Rook",
        incorrect_answers="Rook and King, Knight and Bishop, King and Knight"
    )
# 107
    boardgames6 = Question(
        owner_id=10,
        category="Entertainment: Board Games",
        type="multiple",
        difficulty="hard",
        question="What Magic: The Gathering card's flavor text is just 'Ribbit.'?",
        correct_answer="Turn to Frog",
        incorrect_answers="Spore Frog, Bloated Toad, Frogmite"
    )
# 108
    boardgames7 = Question(
        owner_id=2,
        category="Entertainment: Board Games",
        type="multiple",
        difficulty="hard",
        question="What is the sum of all the tiles in a standard box of Scrabble?",
        correct_answer="187",
        incorrect_answers="207, 197, 177"
    )
# 109
    anime4 = Question(
        owner_id=4,
        category="Entertainment: Japanese Anime & Manga",
        type="multiple",
        difficulty="medium",
        question="The main protagonist of the fifth part of JoJo's Bizarre Adventure is which of the following?",
        correct_answer="Giorno Giovanna",
        incorrect_answers="Guido Mista, Jonathan Joestar, Joey JoJo"
    )
# 110
    anime5 = Question(
        owner_id=8,
        category="Entertainment: Japanese Anime & Manga",
        type="multiple",
        difficulty="medium",
        question="What song plays in the ending credits of the anime 'Ergo Proxy'?",
        correct_answer="Paranoid Android",
        incorrect_answers="Sadistic Summer, Bittersweet Symphony, Mad World"
    )
# 111
    anime6 = Question(
        owner_id=6,
        category="Entertainment: Japanese Anime & Manga",
        type="multiple",
        difficulty="medium",
        question="What is the name of the final villain in the manga series 'Bleach'?",
        correct_answer="Yhwach",
        incorrect_answers="Juha Bach, Yuhabah, Juhabach"
    )
# 112
    anime7 = Question(
        owner_id=10,
        category="Entertainment: Japanese Anime & Manga",
        type="boolean",
        difficulty="medium",
        question="In 'JoJo's Bizarre Adventure', Father Enrico Pucci uses a total of 3 stands in Part 6: Stone Ocean.",
        correct_answer="True",
        incorrect_answers="False"
    )
# 113
    anime8 = Question(
        owner_id=2,
        category="Entertainment: Japanese Anime & Manga",
        type="multiple",
        difficulty="medium",
        question="'Silhouette', a song performed by the group 'KANA-BOON' is featured as the sixteenth opening of which anime?",
        correct_answer="Naruto: Shippūden",
        incorrect_answers="One Piece, Naruto, Gurren Lagann"
    )
# 114
    film5 = Question(
        owner_id=4,
        category="Entertainment: Film",
        type="multiple",
        difficulty="medium",
        question="What is the name of the first 'Star Wars' film by release order?",
        correct_answer="A New Hope",
        incorrect_answers="The Phantom Menace, The Force Awakens, Revenge of the Sith"
    )
# 115
    film6 = Question(
        owner_id=8,
        category="Entertainment: Film",
        type="multiple",
        difficulty="hard",
        question="In what Disney movie can you spot the character 'Pac-Man' in if you look closely enough in some scenes?",
        correct_answer="Tron",
        incorrect_answers="Big Hero 6, Fantasia, Monsters, Inc."
    )
# 116
    film7 = Question(
        owner_id=6,
        category="Entertainment: Film",
        type="multiple",
        difficulty="medium",
        question="In the 2010 Nightmare on Elm Street reboot, who played Freddy Krueger?",
        correct_answer="Jackie Earle Haley",
        incorrect_answers="Tyler Mane, Derek Mears, Gunnar Hansen"
    )
# 117
    film8 = Question(
        owner_id=10,
        category="Entertainment: Film",
        type="multiple",
        difficulty="easy",
        question="For the film 'Raiders of The Lost Ark', what was Harrison Ford sick with during the filming of the Cairo chase?",
        correct_answer="Dysentery",
        incorrect_answers="Anemia, Constipation, Acid Reflux"
    )
# 118
    film9 = Question(
        owner_id=2,
        category="Entertainment: Film",
        type="multiple",
        difficulty="medium",
        question="Which stand-up comedian voiced the talking parrot 'Iago' in Disney's 1992 adaptation of Aladdin?",
        correct_answer="Gilbert Gottfried",
        incorrect_answers="Robin Williams, Pauly Shore, Jonathan Freeman"
    )
# 119
    cartoon2 = Question(
        owner_id=4,
        category="Entertainment: Cartoon & Animations",
        type="boolean",
        difficulty="easy",
        question="In the 'Shrek' film franchise, Donkey is played by Eddie Murphy.",
        correct_answer="True",
        incorrect_answers="False"
    )
# 120
    cartoon3 = Question(
        owner_id=8,
        category="Entertainment: Cartoon & Animations",
        type="multiple",
        difficulty="easy",
        question="What is the relationship between Rick and Morty in the show 'Rick and Morty'?",
        correct_answer="Grandfather and Grandson",
        incorrect_answers="Father and Son, Best Friends, Crimefighting Partners"
    )
# 121
    cartoon4 = Question(
        owner_id=6,
        category="Entertainment: Cartoon & Animations",
        type="multiple",
        difficulty="easy",
        question="In 'Avatar: The Last Airbender', which element does Aang begin to learn after being defrosted?",
        correct_answer="Water",
        incorrect_answers="Air, Earth, Fire"
    )
# 122
    cartoon5 = Question(
        owner_id=10,
        category="Entertainment: Cartoon & Animations",
        type="multiple",
        difficulty="medium",
        question="Who created 'RWBY'?",
        correct_answer="Monty Oum",
        incorrect_answers="Miles Luna, Kerry Shawcross, Shane Newville"
    )
# 123
    cartoon6 = Question(
        owner_id=2,
        category="Entertainment: Cartoon & Animations",
        type="multiple",
        difficulty="hard",
        question="In 'Rick and Morty', from which dimension do Rick and Morty originate from?",
        correct_answer="C-137",
        incorrect_answers="J1977, C-136, C500-a"
    )
# 124
    comics2 = Question(
        owner_id=4,
        category="Entertainment: Comics",
        type="boolean",
        difficulty="medium",
        question="In the webcomic Homestuck, the first character introduced is Dave Strider.",
        correct_answer="False",
        incorrect_answers="True"
    )
# 125
    comics3 = Question(
        owner_id=8,
        category="Entertainment: Comics",
        type="multiple",
        difficulty="easy",
        question="This Marvel superhero is often called 'The man without fear'.",
        correct_answer="Daredevil",
        incorrect_answers="Thor, Wolverine, Hulk"
    )
# 126
    comics4 = Question(
        owner_id=6,
        category="Entertainment: Comics",
        type="multiple",
        difficulty="hard",
        question="Which of the following rings from the DC Comics' 'Lantern Corps' are classified as Parasitic?",
        correct_answer="Indigo (Compassion)",
        incorrect_answers="Green (Willpower), White (Life), Yellow (Fear)"
    )
# 127
    comics5 = Question(
        owner_id=10,
        category="Entertainment: Comics",
        type="multiple",
        difficulty="easy",
        question="What's the race of Invincible's father?",
        correct_answer="Viltrumite",
        incorrect_answers="Kryptonian, Kree, Irken"
    )
# 128
    comics6 = Question(
        owner_id=2,
        category="Entertainment: Comics",
        type="multiple",
        difficulty="medium",
        question="Who was the first American Vampire (Scott Snyder's American Vampire)?",
        correct_answer="Skinner Sweet",
        incorrect_answers="Hattie Hargrove, Pearl Jones, James 'Jim' Book"
    )
# 129
    geography2 = Question(
        owner_id=4,
        category="Geography",
        type="boolean",
        difficulty="medium",
        question="Antarctica is the largest desert in the world.",
        correct_answer="True",
        incorrect_answers="False"
    )
# 130
    geography3 = Question(
        owner_id=8,
        category="Geography",
        type="multiple",
        difficulty="easy",
        question="What is the capital of the US State of New York?",
        correct_answer="Albany",
        incorrect_answers="Buffalo, New York, Rochester"
    )
# 131
    geography4 = Question(
        owner_id=6,
        category="Geography",
        type="multiple",
        difficulty="hard",
        question="What is the land connecting North America and South America?",
        correct_answer="Isthmus of Panama",
        incorrect_answers="Isthmus of Suez, Urals, Australasia"
    )
# 132
    geography5 = Question(
        owner_id=10,
        category="Geography",
        type="multiple",
        difficulty="medium",
        question="How many rivers are in Saudi Arabia?",
        correct_answer="0",
        incorrect_answers="1, 2, 3"
    )
# 133
    geography6 = Question(
        owner_id=2,
        category="Geography",
        type="multiple",
        difficulty="easy",
        question="The longest shared border in the world can be found between which two nations?",
        correct_answer="Canada and the United States",
        incorrect_answers="Chile and Argentina, Russia and China, India and Pakistan"
    )
# 134
    mythology2 = Question(
        owner_id=4,
        category="Mythology",
        type="multiple",
        difficulty="easy",
        question="Who was the only god from Greece who did not get a name change in Rome?",
        correct_answer="Apollo",
        incorrect_answers="Demeter, Zeus, Athena"
    )
# 135
    mythology3 = Question(
        owner_id=8,
        category="Mythology",
        type="multiple",
        difficulty="medium",
        question="This Greek mythological figure is the god/goddess of battle strategy (among other things).",
        correct_answer="Athena",
        incorrect_answers="Ares, Artemis, Apollo"
    )
# 136
    mythology4 = Question(
        owner_id=6,
        category="Mythology",
        type="multiple",
        difficulty="easy",
        question="Who in Greek mythology led the Argonauts in search of the Golden Fleece?",
        correct_answer="Jason",
        incorrect_answers="Castor, Daedalus, Odysseus"
    )
# 137
    mythology5 = Question(
        owner_id=10,
        category="Mythology",
        type="multiple",
        difficulty="medium",
        question="A minotaur is half human half what?",
        correct_answer="Bull",
        incorrect_answers="Cow, Horse, Eagle"
    )
# 138
    mythology6 = Question(
        owner_id=2,
        category="Mythology",
        type="multiple",
        difficulty="medium",
        question="According to Japanese folklore, what is the favorite food of the Kappa?",
        correct_answer="Cucumbers",
        incorrect_answers="Kabocha, Nasu, Soba"
    )
# 139
    math1 = Question(
        owner_id=4,
        category="Science: Mathematics",
        type="multiple",
        difficulty="easy",
        question="What's the square root of 49?",
        correct_answer="7",
        incorrect_answers="4, 12, 9"
    )
# 140
    math2 = Question(
        owner_id=8,
        category="Science: Mathematics",
        type="multiple",
        difficulty="easy",
        question="What prime number comes next after 19?",
        correct_answer="23",
        incorrect_answers="25, 21, 27"
    )
# 141
    math3 = Question(
        owner_id=6,
        category="Science: Mathematics",
        type="boolean",
        difficulty="medium",
        question="E = MC^3",
        correct_answer="False",
        incorrect_answers="True"
    )
# 142
    math4 = Question(
        owner_id=10,
        category="Science: Mathematics",
        type="multiple",
        difficulty="hard",
        question="Which of these numbers is closest to the total number of possible states for an army standard Enigma Machine?",
        correct_answer="1.58 x 10^20",
        incorrect_answers="1.58 x 10^22, 1.58 x  10^18, 1.58 x 10^24"
    )
# 143
    math5 = Question(
        owner_id=2,
        category="Science: Mathematics",
        type="multiple",
        difficulty="hard",
        question="What is the fourth digit of π?",
        correct_answer="1",
        incorrect_answers="2, 3, 4"
    )

# 144
    tele1 = Question(
        owner_id=4,
        category="Entertainment: Television",
        type="multiple",
        difficulty="hard",
        question="Which of these in the Star Trek series is NOT Klingon food?",
        correct_answer="Hors d'oeuvre",
        incorrect_answers="Racht, Gagh, Bloodwine"
    )
# 145
    tele2 = Question(
        owner_id=8,
        category="Entertainment: Television",
        type="boolean",
        difficulty="medium",
        question="In 'Star Trek', Klingons respect William Shakespeare, they even suspect him having a Klingon lineage.",
        correct_answer="True",
        incorrect_answers="False"
    )
# 146
    tele3 = Question(
        owner_id=6,
        category="Entertainment: Television",
        type="multiple",
        difficulty="medium",
        question="What was Nickelodeon's original name?",
        correct_answer="Pinwheel",
        incorrect_answers="MTVKids, KidsTV, Splat!"
    )
# 147
    tele4 = Question(
        owner_id=10,
        category="Entertainment: Television",
        type="multiple",
        difficulty="hard",
        question="Which of these voices wasn't a choice for the House AI in 'The Simpsons Treehouse of Horror' short, House of Whacks?",
        correct_answer="George Clooney",
        incorrect_answers="Matthew Perry, Dennis Miller, Pierce Brosnan"
    )
# 148
    tele5 = Question(
        owner_id=2,
        category="Entertainment: Television",
        type="multiple",
        difficulty="medium",
        question="Baron Silas Greenback is the arch nemesis of which cartoon hero?",
        correct_answer="Danger Mouse",
        incorrect_answers="Bananaman, SuperTed, Captain Star"
    )
# 149
    sports1 = Question(
        owner_id=4,
        category="Sports",
        type="boolean",
        difficulty="easy",
        question="Peyton Manning retired after winning Super Bowl XLIX.",
        correct_answer="False",
        incorrect_answers="True"
    )
# 150
    sports2 = Question(
        owner_id=8,
        category="Sports",
        type="multiple",
        difficulty="medium",
        question="What is the highest belt you can get in Taekwondo?",
        correct_answer="Black",
        incorrect_answers="White, Red, Green"
    )
# 151
    sports3 = Question(
        owner_id=6,
        category="Sports",
        type="multiple",
        difficulty="hard",
        question="Which male player won the gold medal of table tennis singles in 2016 Olympics Games?",
        correct_answer="Ma Long (China)",
        incorrect_answers="Zhang Jike (China), Jun Mizutani (Japan), Vladimir Samsonov (Belarus)"
    )
# 152
    sports4 = Question(
        owner_id=10,
        category="Sports",
        type="multiple",
        difficulty="medium",
        question="In what sport does Fanny Chmelar compete for Germany?",
        correct_answer="Skiing",
        incorrect_answers="Swimming, Showjumping, Gymnastics"
    )
# 153
    sports5 = Question(
        owner_id=2,
        category="Sports",
        type="multiple",
        difficulty="easy",
        question="What team did England beat to win in the 1966 World Cup final?",
        correct_answer="West Germany",
        incorrect_answers="Soviet Union, Portugal, Brazil"
    )

# 154
    politics1 = Question(
        owner_id=4,
        category="Politics",
        type="boolean",
        difficulty="medium",
        question="George W. Bush lost the popular vote in the 2004 United States presidential election.",
        correct_answer="False",
        incorrect_answers="True"
    )
# 155
    politics2 = Question(
        owner_id=8,
        category="Politics",
        type="multiple",
        difficulty="hard",
        question="Which of the following United States Presidents served the shortest term in office?",
        correct_answer="William Henry Harrison",
        incorrect_answers="Zachary Taylor, James A. Garfield, Warren G. Harding"
    )
# 156
    politics3 = Question(
        owner_id=6,
        category="Politics",
        type="multiple",
        difficulty="hard",
        question="Which of the following United States senators is known for performing a 24-hour long filibuster?",
        correct_answer="Strom Thurmond",
        incorrect_answers="Roy Blunt, John Barrasso, Chuck Schumer"
    )
# 157
    politics4 = Question(
        owner_id=10,
        category="Politics",
        type="multiple",
        difficulty="medium",
        question="Who was elected leader of the UK Labour Party in September 2015?",
        correct_answer="Jeremy Corbyn",
        incorrect_answers="Ed Miliband, David Cameron, Theresa May"
    )
# 158
    politics5 = Question(
        owner_id=2,
        category="Politics",
        type="multiple",
        difficulty="medium",
        question="What year did Gerald Ford Become President?",
        correct_answer="1974",
        incorrect_answers="1977, 1973, 1969"
    )
# 159
    art1 = Question(
        owner_id=4,
        category="Art",
        type="multiple",
        difficulty="easy",
        question="Who painted the Sistine Chapel?",
        correct_answer="Michelangelo",
        incorrect_answers="Leonardo da Vinci, Pablo Picasso, Raphael"
    )
# 160
    art2 = Question(
        owner_id=8,
        category="Art",
        type="boolean",
        difficulty="easy",
        question="Leonardo da Vinci's Mona Lisa does not have eyebrows.",
        correct_answer="True",
        incorrect_answers="False"
    )
# 161
    art3 = Question(
        owner_id=6,
        category="Art",
        type="multiple",
        difficulty="medium",
        question="Who designed the Chupa Chups logo?",
        correct_answer="Salvador Dali",
        incorrect_answers="Pablo Picasso, Andy Warhol, Vincent van Gogh"
    )
# 162
    art4 = Question(
        owner_id=10,
        category="Art",
        type="multiple",
        difficulty="medium",
        question="Who painted the epic mural Guernica?",
        correct_answer="Pablo Picasso",
        incorrect_answers="Francisco Goya, Leonardo da Vinci, Henri Matisse"
    )
# 163
    art5 = Question(
        owner_id=2,
        category="Art",
        type="multiple",
        difficulty="easy",
        question="Who painted the biblical fresco The Creation of Adam?",
        correct_answer="Michelangelo",
        incorrect_answers="Leonardo da Vinci, Caravaggio, Rembrandt"
    )
# 164
    animals1 = Question(
        owner_id=3,
        category="Animals",
        type="boolean",
        difficulty="medium",
        question="An octopus can fit through any hole larger than its beak.",
        correct_answer="True",
        incorrect_answers="False"
    )
# 165
    animals2 = Question(
        owner_id=7,
        category="Animals",
        type="multiple",
        difficulty="hard",
        question="What is the scientific name of the cheetah?",
        correct_answer="Acinonyx jubatus",
        incorrect_answers="Panthera onca, Lynx rufus, Felis catus"
    )
# 166
    animals3 = Question(
        owner_id=5,
        category="Animals",
        type="multiple",
        difficulty="medium",
        question="The now extinct species 'Thylacine' was native to where?",
        correct_answer="Tasmania, Australia",
        incorrect_answers="Baluchistan, Pakistan, Wallachia, Romania, Oregon, United States"
    )
# 167
    animals4 = Question(
        owner_id=9,
        category="Animals",
        type="multiple",
        difficulty="easy",
        question="What is Grumpy Cat's real name?",
        correct_answer="Tardar Sauce",
        incorrect_answers="Sauce, Minnie, Broccoli"
    )
# 168
    animals5 = Question(
        owner_id=1,
        category="Animals",
        type="boolean",
        difficulty="easy",
        question="The freshwater amphibian, the Axolotl, can regrow its limbs.",
        correct_answer="True",
        incorrect_answers="False"
    )
# 169
    vehicles1 = Question(
        owner_id=6,
        category="Vehicles",
        type="multiple",
        difficulty="medium",
        question="Which of the following vehicles featured a full glass roof at base model?",
        correct_answer="Renault Avantime",
        incorrect_answers="Chevy Volt, Mercedes-Benz A-Class, Honda Odyssey"
    )
# 170
    vehicles2 = Question(
        owner_id=2,
        category="Vehicles",
        type="multiple",
        difficulty="hard",
        question="In 2014, over 6 million General Motors vehicles were recalled due to what critical flaw?",
        correct_answer="Faulty ignition switch",
        incorrect_answers="Malfunctioning gas pedal, Breaking fuel lines, Faulty brake pads"
    )
# 171
    vehicles3 = Question(
        owner_id=8,
        category="Vehicles",
        type="multiple",
        difficulty="easy",
        question="Which car tire manufacturer is famous for its 'P Zero' line?",
        correct_answer="Pirelli",
        incorrect_answers="Goodyear, Bridgestone, Michelin"
    )
# 172
    vehicles4 = Question(
        owner_id=4,
        category="Vehicles",
        type="multiple",
        difficulty="medium",
        question="What nickname was given to Air Canada Flight 143 after it ran out of fuel and glided to safety in 1983?",
        correct_answer="Gimli Glider",
        incorrect_answers="Gimli Microlight, Gimli Chaser, Gimli Superb"
    )
# 173
    vehicles5 = Question(
        owner_id=10,
        category="Vehicles",
        type="multiple",
        difficulty="easy",
        question="What is the fastest road legal car in the world?",
        correct_answer="Koenigsegg Agera RS",
        incorrect_answers="Hennessy Venom GT, Bugatti Veyron Super Sport, Pagani Huayra BC"
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
        videogames12, gadgets3, film4, computers5, music5, general42, music6, computers6, musicals2, musicals3, musicals4,
        musicals5, musicals6 , books3, books4, books5, books6, books7, celebrities2, celebrities3, celebrities4, celebrities5,
        celebrities6, boardgames3, boardgames4, boardgames5, boardgames6, boardgames7, anime4, anime5, anime6, anime7, anime8,
        film5, film6, film7, film8, film9, cartoon2, cartoon3, cartoon4, cartoon5, cartoon6, comics2, comics3, comics4, comics5,
        comics6, geography2, geography3, geography4, geography5, geography6, mythology2, mythology3, mythology4, mythology5,
        mythology6, math1, math2, math3, math4, math5, tele1, tele2, tele3, tele4, tele5, sports1, sports2, sports3, sports4, sports5,
        politics1, politics2, politics3, politics4, politics5, art1, art2, art3, art4, art5, animals1, animals2, animals3, animals4, animals5,
        vehicles1, vehicles2, vehicles3, vehicles4, vehicles5
    ])


    db.session.commit()

def undo_questions():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.questions RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM questions"))

    db.session.commit()
