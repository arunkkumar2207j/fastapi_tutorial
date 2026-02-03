from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

from crud import app as crud_app

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/about")
def about():
  return {"message":"About Page"}

@app.get("/greet")
def greet():
   return {"message": f"Hello, Arun"}

@app.get("/greet/")
def greet_name(name:str, age:Optional[int] = None):
   return {"message": f"Hello, {name}, your age is {age}"}

class Student(BaseModel):
   name: str
   age: int
   roll: int
   grade: Optional[str] = None

@app.post("/create_student")
def create_student(student: Student):
   return {"message": f"Student {student.name} created successfully", "student": student}