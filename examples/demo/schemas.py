from pydantic import BaseModel

class Student(BaseModel):
    id: int
    name: str
    age: int

class StudentCreateFields(BaseModel):
    name:str
    age:int

class StudentUpdateFields(BaseModel):
    name:str
    age:int
