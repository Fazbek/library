from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    publication_date = Column(DateTime, nullable=True)
    genre_id = Column(Integer, ForeignKey('genres.id'))
    author_id = Column(Integer, ForeignKey('authors.id'))
    available = Column(Boolean, default=True)

    genre = relationship("Genre", back_populates="books")
    author = relationship("Author", back_populates="books")
    borrowings = relationship("Borrowing", back_populates="book")
    reviews = relationship("Review", back_populates="book")


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, nullable=False)
    biography = Column(String, nullable=False)

    books = relationship("Book", back_populates="author")


class Genre(Base):
    __tablename__ = 'genres'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, nullable=False)

    books = relationship("Book", back_populates="genre")


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    phone_number = Column(Integer, unique=True, nullable=False)
    is_active = Column(Boolean, default=True)

    borrowings = relationship("Borrowing", back_populates="user")
    reviews = relationship("Review", back_populates="user")


class Borrowing(Base):
    __tablename__ = 'borrowings'
    id = Column(Integer, autoincrement=True, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    borrow_date = Column(DateTime)

    book = relationship("Book", back_populates="borrowings")
    user = relationship("User", back_populates="borrowings")


class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, autoincrement=True, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    rating = Column(Integer, nullable=False)
    comment = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    book = relationship("Book", back_populates="reviews")
    user = relationship("User", back_populates="reviews")
