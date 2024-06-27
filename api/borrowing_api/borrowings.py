from fastapi import APIRouter
from database.borrowingservice import *
from datetime import datetime


borrowing_router = APIRouter(tags=["Control of borrowings"], prefix="/borrowing")


@borrowing_router.post("/do-borrowing")
def create_borrowing(user_id: int, book_id: int):
    add = create_borrowing_db(user_id=user_id, book_id=book_id)
    return add


# done
@borrowing_router.get('/get-exact-borrowing/')
async def get_exact_borrowing(id: int):
    exact_borrowing = get_borrowing_db(id=id)
    return exact_borrowing


# done
@borrowing_router.put("/change_borrowing/")
async def change_borrowing(id: int, change_info, new_info: str):
    data = update_borrowing_db(id=id, change_info=change_info, new_info=new_info)
    return data


# done
@borrowing_router.delete("/cansel_borrowing/")
async def cansel_borrowing(id: int):
    data = cansel_borrowing_db(id=id)
    return data


# done
@borrowing_router.get("/all-borrowings/")
async def get_all_borrowings():
    all = get_all_borrowings_db()
    return all


@borrowing_router.post("/return-book-back/")
def return_book(borrowing_id: int):
    return return_book_db(borrowing_id=borrowing_id)
