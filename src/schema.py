from pydantic import BaseModel
from typing import List


class Questions_pydantic_post(BaseModel):
    title: str
    question_text: str 
    options: list
    question_type: str 

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True


class Questions_pydantic(BaseModel):
    id: int
    title: str
    question_text: str 
    options: list
    question_type: str 

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True
