from fastapi import FastAPI, Depends
from database import engine, get_db
from sqlalchemy.orm import Session
import model
from pydantic import BaseModel

app = FastAPI()

class Bookstore(BaseModel):
  # id:int
  title:str
  author:str
  published_date:str


@app.post("/books")
def create_bookstore(book:Bookstore, db: Session = Depends(get_db)):
  new_book = model.Book(
    id=len(db.query(model.Book).all()) + 1,
    title=book.title,
    author=book.author,
    published_date=book.published_date
  )
  db.add(new_book)
  db.commit()
  db.refresh(new_book)
  return {"message": "Book added successfully", "book": new_book}