from datetime import datetime
from database import get_db
from .models import Book, Author, Genre


# Books, done
def create_book_db(title, description, genre_id, author_id):
    db = next(get_db())
    genre = db.query(Genre).filter(Genre.id == genre_id).first()
    author = db.query(Author).filter(Author.id == author_id).first()
    if not genre:
        return "Genre not found."
    if not author:
        return "Author not found."
    new_book = Book(description=description, publication_date=datetime.now(),
                        title=title, genre_id=genre_id, author_id=author_id)
    db.add(new_book)
    db.commit()
    return "Book successfully created!"


# done
def get_all_books_db():
    db = next(get_db())
    books = db.query(Book).all()
    return books


# done
def get_book_db(id):
    db = next(get_db())
    book = db.query(Book).filter_by(id=id).first()
    if book:
        return book
    return "Book not found"


# done
def update_book_db(id, change_info, new_info):
    db = next(get_db())
    book = db.query(Book).filter_by(id=id).first()
    if book:
        try:
            if change_info == "title":
                book.title = new_info
                db.commit()
                return "Successfully changed"
            elif change_info == "description":
                book.description = new_info
                db.commit()
                return "Successfully changed"
            elif change_info == "genre_id":
                book.genre_id = new_info
                db.commit()
                return "Successfully changed"
            elif change_info == "author_id":
                book.author_id = new_info
                db.commit()
                return "Successfully changed"
        except:
            return "There is no value for changing"
    return False


# done
def delete_book_db(id):
    db = next(get_db())
    book = db.query(Book).filter_by(id=id).first()
    if book:
        db.delete(book)
        db.commit()
        return "Book successfully deleted!"
    return "Book not found"


# Authors, done
def create_author_db(name, biography):
    db = next(get_db())
    new_author = Author(name=name, biography=biography)
    db.add(new_author)
    db.commit()
    return "Author successfully created!"


# done
def get_all_authors_db():
    db = next(get_db())
    authors = db.query(Author).all()
    return authors


# done
def get_author_db(id):
    db = next(get_db())
    author = db.query(Author).filter_by(id=id).first()
    if author:
        return author
    return "Author not found"


# done
def update_author_db(id, change_info, new_info):
    db = next(get_db())
    author = db.query(Author).filter_by(id=id).first()
    if author:
        try:
            if change_info == "name":
                author.name = new_info
                db.commit()
                return "Successfully changed"
            elif change_info == "biography":
                author.biography = new_info
                db.commit()
                return "Successfully changed"
        except:
            return "There is no value for changing"
    return False


# done
def delete_author_db(id):
    db = next(get_db())
    author = db.query(Author).filter_by(id=id).first()
    if author:
        db.delete(author)
        db.commit()
        return "Author successfully deleted!"
    return "Author not found"


# Genre , done
def create_genre_db(name):
    db = next(get_db())
    new_genre = Genre(name=name)
    db.add(new_genre)
    db.commit()
    return "Genre successfully created!"


# done
def get_all_genres_db():
    db = next(get_db())
    genres = db.query(Genre).all()
    return genres


# done
def get_genre_db(id):
    db = next(get_db())
    genre = db.query(Genre).filter_by(id=id).first()
    if genre:
        return genre
    return "Genre not found"


# done
def update_genre_db(id, change_info, new_info):
    db = next(get_db())
    genre = db.query(Genre).filter_by(id=id).first()
    if genre:
        try:
            if change_info == "name":
                genre.name = new_info
                db.commit()
                return "Successfully changed"
        except:
            return "There is no value for changing"
    return False


# done
def delete_genre_db(id):
    db = next(get_db())
    genre = db.query(Genre).filter_by(id=id).first()
    if genre:
        db.delete(genre)
        db.commit()
        return "Genre successfully deleted!"
    return "Genre not found"


# other methods, done
def mark_book_as_available_db(id):
    db = next(get_db())
    book = db.query(Book).filter_by(id=id).first()
    if book:
        book.available = True
        db.commit()
        db.refresh(book)
        return "Book marked as available"
    return "Book not found"


# done
def mark_book_as_unavailable_db(id):
    db = next(get_db())
    book = db.query(Book).filter_by(id=id).first()
    if book:
        book.available = False
        db.commit()
        db.refresh(book)
        return "Book marked as unavailable"
    return "Book not found"


# def get_books_by_author_db(author_id):
#     db = next(get_db())
#     books = db.query(Book).filter(Book.author_id == author_id).all()
#     return books


def search_books_by_title_db(title):
    db = next(get_db())
    books = db.query(Book).filter(Book.title.contains(title)).all()
    return books


def get_books_by_author_name_db(author_name: str):
    db = next(get_db())
    books = db.query(Book).join(Author).filter(Author.name == author_name).all()
    return books


def get_books_by_genre_db(genre_name: str):
    db = next(get_db())
    books = db.query(Book).join(Genre).filter(Genre.name == genre_name).all()
    return books

