from pydantic import BaseModel


class Questions_pydantic_post(BaseModel):
    title: str
    description: str
    question_text: str 
    options: str
    question_type: str 

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True


class Questions_pydantic(BaseModel):
    id: int
    title: str
    description: str
    question_text: str 
    options: str
    question_type: str 

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True
