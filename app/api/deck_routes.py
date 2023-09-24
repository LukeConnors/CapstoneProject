from flask import Blueprint, jsonify, session, request
from app.models import Question, Deck, Deck_question, Review, db
from app.forms import DeckForm, ReviewForm
from flask_login import current_user, login_required
# import requests

deck_routes = Blueprint('decks', __name__)

# GET all decks
@deck_routes.route('/')
def decks():
    decks = Deck.query.all()

    return {"decks": [deck.to_dict() for deck in decks]}

# GET all decks by category
@deck_routes.route("/deck_category")
def get_decks_category():
    category = request.args.get("category", "")
    decks = Deck.query.filter(Deck.category == category)
    return {"decks": [deck.to_dict() for deck in decks]}

# GET all questions that belong to a deck by ID
@deck_routes.route("/<int:id>/questions")
def get_deck_questions(id):
    questions = []
    deck_questions = Deck_question.query.filter(Deck_question.deck_id == id)
    for deck_question in deck_questions:
        question = Question.query.get(deck_question.question_id)
        questions.append(question)
    return {"deck_questions": [question.to_dict() for question in questions]}

# GET all decks owned by the current user
@deck_routes.route("/my_decks")
def my_decks():
    decks = Deck.query.filter(Deck.user_id == current_user.id)
    return {"decks": [deck.to_dict() for deck in decks]}

# GET a deck by ID
@deck_routes.route('/<int:id>')
def get_deck(id):
    deck = Deck.query.get(id)
    return deck.to_dict()

# GET all reviews by deck ID
@deck_routes.route('/<int:id>/reviews')
def get_deck_reviews(id):
    reviews = Review.query.filter(Review.deck_id == id)
    return {"deck_reviews": [review.to_dict() for review in reviews]}

# POST a deck to decks
@deck_routes.route('/', methods=["POST"])
@login_required
def create_deck():
    form = DeckForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        new_deck = Deck(
            user_id=current_user.id,
            title=form.data["title"],
            description=form.data["description"],
            category=form.data["category"],
        )
        print("!!!!!!!!!!!THIS IS THE BACKEND NEW DECK!!!!!!!!!!!!!!!", new_deck)
        db.session.add(new_deck)
        db.session.commit()
        return new_deck.to_dict()

# POST a review by deckID
@deck_routes.route("/<int:id>/reviews", methods=["POST"])
@login_required
def create_review(id):
    form = ReviewForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    if form.validate_on_submit():
        new_review=Review(
            user_id=current_user.id,
            deck_id=id,
            stars=form.data["stars"],
            description=form.data["description"]
        )
        db.session.add(new_review)
        db.session.commit()
        return new_review.to_dict()


# PUT a deck by ID
@deck_routes.route("/<int:id>", methods=["PUT"])
@login_required
def edit_deck(id):
    form = DeckForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    if form.validate_on_submit():
        deck = Deck.query.get(id)
        if deck:
            if form.data.get("title"):
                deck.title = form.data["title"]
            if form.data.get("description"):
                deck.description = form.data["description"]
            if form.data.get("category"):
                deck.category = form.data["category"]
            db.session.commit()
            return deck.to_dict()
        else:
            return jsonify({"error": "Deck not found"}), 404
    else:
        return jsonify({"error": "Invalid form data", "form_errors": form.errors}), 400



# DELETE a deck by id
@deck_routes.route('/<int:id>', methods=["DELETE"])
def delete_deck(id):
    deck = Deck.query.get(id)
    if not deck:
        return jsonify({"error": "Deck not found"}), 404

    if deck.user_id != current_user.id:
        return jsonify({"error": "Unauthorized"}), 403

    db.session.delete(deck)
    db.session.commit()

    return jsonify({"Message": "Successfully deleted!"})


# ADD a question to a deck by deck id
@deck_routes.route('/<int:id>/questions', methods=["POST"])
def add_deck_question(id):
    question = request.json
    print(question)
    new_deck_question = Deck_question(
        deck_id=id,
        question_id=question["id"]
    )
    db.session.add(new_deck_question)
    db.session.commit()
    return new_deck_question.to_dict()

# DELETE/remove a question from a deck
@deck_routes.route('/<int:d_id>/questions/<int:q_id>', methods=["DELETE"])
def remove_deck_question(d_id, q_id):
    deck = Deck.query.get(d_id)
    question = Question.query.get(q_id)
    deck_question = Deck_question.query.filter(Deck_question.deck_id == deck.id and Deck_question.question_id == question.id)

    if not deck:
        return jsonify({"error": "Deck not found"}), 404
    if not question:
        return jsonify({"error": "Question not found"}), 404
    if deck.user_id != current_user.id:
        return jsonify({"error": "this deck doesn't belong to you"})
    if not deck_question:
        return jsonify({"error": "This question and deck combination does not exist"})

    db.session.delete(deck_question)
    db.session.commit()

    return jsonify({"Message": "Successfully deleted!"})
