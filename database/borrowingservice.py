from datetime import datetime
from database import get_db
from .models import Borrowing, Book


def get_all_borrowings_db():
    db = next(get_db())
    borrowings = db.query(Borrowing).all()
    return borrowings


def get_borrowing_db(id):
    db = next(get_db())
    borrowing = db.query(Borrowing).filter_by(id=id).first()
    if borrowing:
        return borrowing
    return "Borrowing not found"


def update_borrowing_db(id, change_info, new_info):
    db = next(get_db())
    borrowing = db.query(Borrowing).filter_by(id=id).first()
    if borrowing:
        try:
            if change_info == "book_id":
                borrowing.book_id = new_info
                db.commit()
                return "Successfully changed"
            elif change_info == "user_id":
                borrowing.user_id = new_info
                db.commit()
                return "Successfully changed"
        except:
            return "There is no value for changing"
    return False


def cansel_borrowing_db(id):
    db = next(get_db())
    borrowing = db.query(Borrowing).filter_by(id=id).first()
    if borrowing:
        db.delete(borrowing)
        db.commit()
        return "Borrowing successfully deleted!"
    return "Borrowing not found"


# Borrowings
def create_borrowing_db(user_id: int, book_id: int):
    db = next(get_db())
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        return "Book not found."

    if book.available:
        new_borrowing = Borrowing(user_id=user_id, book_id=book_id, borrow_date=datetime.now())
        db.add(new_borrowing)
        db.commit()

        mark_book_as_unavailable(book_id)

        return "Borrowing created successfully."
    else:
        return "Book is not available for borrowing."


def mark_book_as_unavailable(book_id: int):
    db = next(get_db())
    book = db.query(Book).filter(Book.id == book_id).first()
    if book:
        book.available = False
        db.commit()
        return "Book marked as unavailable."
    else:
        return "Book not found."


def return_book_db(borrowing_id: int):
    db = next(get_db())

    borrowing = db.query(Borrowing).filter(Borrowing.id == borrowing_id).first()
    if not borrowing:
        return "Borrowing record not found."

    db.commit()

    mark_book_as_available_db(borrowing.book_id)

    return "Book returned successfully."


def mark_book_as_available_db(book_id: int):
    db = next(get_db())
    book = db.query(Book).filter(Book.id == book_id).first()
    if book:
        book.available = True
        db.commit()
        return "Book marked as available."
    return "Book not found."
