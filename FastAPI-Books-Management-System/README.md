# FastAPI Books Project

## Project Overview

This project is a simple REST API built using FastAPI and Python. It allows users to retrieve books, search books by ID, filter books by rating or publication year, create new books, update existing books, and delete books.

## Technologies Used

- Python
- FastAPI
- Pydantic
- Uvicorn
- PyCharm

## Project Structure

```text
Books_Project/
├── .venv/
├── output/
├── Book.py
├── README.md
└── .gitignore
```

## Features

- Retrieve all books.
- Retrieve a book by its ID.
- Filter books by rating.
- Filter books by publication year.
- Create a new book.
- Update an existing book.
- Delete a book.
- Validate request data using Pydantic.
- Handle errors using HTTPException.

## Installation

### 1. Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
python -m pip install fastapi uvicorn
```

## Run the Application

Run the following command from the project directory:

```powershell
python -m uvicorn Book:app --reload
```

The API server will start at:

http://127.0.0.1:8000

## API Documentation

Open the interactive Swagger UI documentation:

http://127.0.0.1:8000/docs

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/books` | Retrieve all books |
| GET | `/books/{book_id}` | Retrieve a book by ID |
| DELETE | `/books/{book_id}` | Delete a book by ID |
| GET | `/books/?book_rating=5` | Filter books by rating |
| GET | `/books/publish/?published_date=1995` | Filter books by publication year |
| POST | `/crate-book` | Create a new book |
| PUT | `/books/update_book` | Update a book |