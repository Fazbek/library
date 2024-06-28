from fastapi import APIRouter
from database.bookservice import *
from datetime import datetime


book_router = APIRouter(tags=["Control of books"], prefix="/book")
author_router = APIRouter(tags=["Control of authors"], prefix="/author")
genre_router = APIRouter(tags=["Control of genres"], prefix="/genre")


# done
@book_router.post("/add-book/")
async def add_book(title: str, description: str, genre_id: int, author_id: int):
    add = create_book_db(title=title, description=description, genre_id=genre_id, author_id=author_id)
    return add


# done
@book_router.get('/get-exact-book/')
async def get_exact_book(id: int):
    exact_book = get_book_db(id=id)
    return exact_book


# not done
@book_router.put("/change_book/")
async def change_book(id: int, change_info, new_info: str):
    data = update_book_db(id=id, change_info=change_info, new_info=new_info)
    return data


# done
@book_router.delete("/delete_book/")
async def delete_book(id: int):
    data = delete_book_db(id=id)
    return data


# done
@book_router.get("/all-books/")
async def get_all_books():
    all = get_all_books_db()
    return all


# Author
@author_router.post("/add-author/")
async def add_author(name: str, biography: str):
    add = create_author_db(name=name, biography=biography)
    return add


# done
@author_router.get('/get-exact-author/')
async def get_exact_author(id: int):
    exact_author = get_author_db(id=id)
    return exact_author


# done
@author_router.put("/change_author/")
async def change_author(id: int, change_info, new_info: str):
    data = update_author_db(id=id, change_info=change_info, new_info=new_info)
    return data


# done
@author_router.delete("/delete_author/")
async def delete_author(id: int):
    data = delete_author_db(id=id)
    return data


# done
@author_router.get("/all-authors/")
async def get_all_authors():
    all = get_all_authors_db()
    return all


# Genres, done
@genre_router.post("/add-genre/")
async def add_genre(name: str):
    add = create_genre_db(name=name)
    return add


# done
@genre_router.get('/get-exact-genre/')
async def get_exact_genre(id: int):
    exact_genre = get_genre_db(id=id)
    return exact_genre


# done
@genre_router.put("/change_genre/")
async def change_genre(id: int, change_info, new_info: str):
    data = update_genre_db(id=id, change_info=change_info, new_info=new_info)
    return data


# done
@genre_router.delete("/delete_genre/")
async def delete_genre(id: int):
    data = delete_genre_db(id=id)
    return data


# done
@genre_router.get("/all-genres/")
async def get_all_genres():
    all = get_all_genres_db()
    return all


@book_router.put("/available")
def mark_book_as_available(id: int):
    return mark_book_as_available_db(id=id)


@book_router.put("/unavailable")
def mark_book_as_unavailable(id: int):
    return mark_book_as_unavailable_db(id=id)


@book_router.get("/search-by-author-name/")
def get_books_by_author_name(author_name: str):
    return get_books_by_author_name_db(author_name)


@book_router.get("/search-by-title/")
def search_books_by_title(title: str):
    return search_books_by_title_db(title)


@book_router.get("/search-by-genre")
def get_books_by_genre(genre_name: str):
    return get_books_by_genre_db(genre_name)
