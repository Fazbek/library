from datetime import datetime
from database import get_db
from .models import Review, User, Book


# Reviews, done
def create_review_db(user_id, book_id, rating, comment):
    db = next(get_db())
    user = db.query(User).filter(User.id == user_id).first()
    book = db.query(Book).filter(Book.id == book_id).first()
    if not user:
        return "User not found."
    if not user.is_active:
        return "User is deactivated and cannot leave a review."
    if not book:
        return "Book not found."
    if not book.available:
        return "Book is not available and you can't leave a review on that book."
    new_review = Review(user_id=user_id, book_id=book_id, rating=rating, comment=comment)
    if rating > 10:
        return "You can't write rating greater than 10"
    if rating < 0:
        return "You can't write negative number"
    db.add(new_review)
    db.commit()
    return "Review successfully created!"


# done
def get_all_reviews_db():
    db = next(get_db())
    reviews = db.query(Review).all()
    return reviews


# done
def get_review_db(id):
    db = next(get_db())
    review = db.query(Review).filter_by(id=id).first()
    if review:
        return review
    return "Review not found"


def update_review_db(id, change_info, new_info):
    db = next(get_db())
    review = db.query(Review).filter_by(id=id).first()
    if review:
        try:
            if change_info == "book_id":
                review.book_id = new_info
                db.commit()
                return "Successfully changed"
            elif change_info == "user_id":
                review.user_id = new_info
                db.commit()
                return "Successfully changed"
            elif change_info == "rating":
                review.rating = new_info
                db.commit()
                return "Successfully changed"
            elif change_info == "comment":
                review.comment = new_info
                db.commit()
                return "Successfully changed"
        except:
            return "There is no value for changing"
    return False


def delete_review_db(id):
    db = next(get_db())
    review = db.query(Review).filter_by(id=id).first()
    if review:
        db.delete(review)
        db.commit()
        return "Review successfully deleted!"
    return "Review not found"


def search_review_by_rating_db(rating):
    db = next(get_db())
    reviews = db.query(Review).filter(Review.rating.contains(rating)).all()
    return reviews
