from fastapi import FastAPI
from api.book_api.books import book_router, author_router, genre_router
from api.borrowing_api.borrowings import borrowing_router
from api.review_api.reviews import review_router
from database import Base, engine
from api.user_api.users import user_router

Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url="/")

app.include_router(user_router)
app.include_router(review_router)
app.include_router(borrowing_router)
app.include_router(book_router)
app.include_router(author_router)
app.include_router(genre_router)
