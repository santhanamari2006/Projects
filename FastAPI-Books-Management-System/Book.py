
from typing import Optional

from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from starlette import status


app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date


class BookRequest(BaseModel):
    id: Optional[int] = Field(
        default=None,
        description="ID is not needed on create",
        gt=0,
    )
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)
    published_date: int = Field(gt=1991, lt=2031)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A new book",
                "author": "codingwithsmari",
                "description": "A new description of a book",
                "rating": 5,
                "published_date": 1995,
            }
        }
    }


BOOKS = [
    Book(1, "Computer Science Pro", "codingwithsmari",
         "A very nice book", 5, 2026),
    Book(2, "Be Fast with FastAPI", "codingwithsmari",
         "A great book", 5, 2006),
    Book(3, "Master Endpoints", "codingwithsmari",
         "An awesome book", 5, 2004),
    Book(4, "HP1", "Author1", "Book Description", 2, 1994),
    Book(5, "HP2", "Author2", "Book Description", 3, 2030),
    Book(6, "HP3", "Author3", "Book Description", 1, 1994),
]


# 1. GET - Read All Books
@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS


# 2. GET - Read Book by ID
@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found",
    )


# 3. DELETE - Delete Book by ID
@app.delete(
    "/books/{book_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_book(book_id: int = Path(gt=0)):
    for i, book in enumerate(BOOKS):
        if book.id == book_id:
            BOOKS.pop(i)
            return

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found",
    )


# 4. GET - Read Books by Rating
@app.get("/books/", status_code=status.HTTP_200_OK)
async def read_book_by_rating(
    book_rating: int = Query(gt=0, lt=6)
):
    books_to_return = []

    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)

    return books_to_return


# 5. GET - Read Books by Publication Date
@app.get("/books/publish/", status_code=status.HTTP_200_OK)
async def read_books_by_publish_date(
    published_date: int = Query(gt=1991, lt=2031)
):
    books_to_return = []

    for book in BOOKS:
        if book.published_date == published_date:
            books_to_return.append(book)

    return books_to_return


# Generate the next book ID
def find_book_id(book: Book):
    book.id = max(
        (existing_book.id for existing_book in BOOKS),
        default=0,
    ) + 1
    return book.id


# 6. POST - Create Book
@app.post("/crate-book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    book_data = book_request.model_dump(exclude={"id"})

    new_book = Book(
        id=0,
        **book_data,
    )

    find_book_id(new_book)
    BOOKS.append(new_book)

    return new_book


# 7. PUT - Update Book
@app.put(
    "/books/update_book",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def update_book(book: BookRequest):
    if book.id is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Book ID is required for updating",
        )

    for i, existing_book in enumerate(BOOKS):
        if existing_book.id == book.id:
            updated_data = book.model_dump(exclude={"id"})

            BOOKS[i] = Book(
                id=book.id,
                **updated_data,
            )
            return

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found",
    )
