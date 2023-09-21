from flask import Blueprint, jsonify, session, request
from app.models import Question, Deck, Deck_question, Review, db
from app.forms import ReviewForm
from flask_login import current_user, login_required


review_routes = Blueprint('reviews', __name__)

# GET all reviews by current user
@review_routes.route('/my_reviews')
def reviews():
    reviews = Review.query.filter(Review.user_id == current_user.id)

    return {"my_reviews": [review.to_dict() for review in reviews]}


# PUT a review by review ID
@review_routes.route("/<int:id>", methods=["PUT"])
def edit_review(id):
    form=ReviewForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    if form.validate_on_submit():
        review = Review.query.get(id)
        if review:
            if form.data.get("stars"):
                review.stars = form.data["stars"]
            if form.data.get("description"):
                review.description = form.data["description"]
            db.session.commit()
            return review.to_dict()
        else:
            return jsonify({"error": "Review not found"}), 404
    else:
        return jsonify({"error": "Invalid form data", "form_errors": form.errors}), 400


# DELETE a review by review ID
@review_routes.route("/<int:id>", methods=["DELETE"])
def remove_review(id):
    review = Review.query.get(id)
    if not review:
        return jsonify({"error": "Review not found"}), 404

    if review.user_id != current_user.id:
        return jsonify({"error": "Unauthorized"}), 403

    db.session.delete(review)
    db.session.commit()

    return jsonify({"Message": "Successfully deleted!"})
