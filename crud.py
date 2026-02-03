from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# In-memory "database" as list of dicts
books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"id": 2, "title": "The Games of small things", "author": "Kazuo Ishiguro"},
    {"id": 3, "title": "The White Tiger", "author": "Aravind Adiga"},
    {"id": 4, "title": "The Place of Illusion", "author": "Rohinton Mistry"},
]

# In-memory "database" as list of dicts 
books = [ 
  {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"}, 
  {"id": 2, "title": "The Games of small things", "author": "Kazuo Ishiguro"}, 
  {"id": 3, "title": "The White Tiger", "author": "Aravind Adiga"}, 
  {"id": 4, "title": "The Place of Illusion", "author": "Rohinton Mistry"}, 
]

class Book(BaseModel):
  title:str
  author:str

@app.get("/books")
def get_books():
  if not books:
    return {"message": "No books available"}
  return {"books": books}

@app.get("/books/{book_id}")
def get_book(id:int):
  for b in books:
    if b["id"]== id:
      return {"book": b}
  return {"message": "Book not found"}

@app.post("/book")
def add_book(book:Book):
  new_book = {
    "id":len(books)+ 1,
    "title": book.title,
    "author": book.author
  }
  books.append(new_book)
  return {"message": "Book added successfully", "book": new_book}

@app.put("/books/{id}")
def update_book(book_id:int, book: Book):
  for b in books:
    if b["id"] == book_id:
      b["title"] = book.title
      b["author"] = book.author
      return {"message": "Book updated successfully", "book": b}
  return {"message": "Book not found"}

@app.delete("/books/{id}")
def delete_book(book_id:int):
  for b in books:
    if b["id"]== book_id:
      books.remove(b)
      return {"message": "Book deleted successfully"}
  return {"message": "Book not found"}