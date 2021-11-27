from pydantic import BaseModel


class ToDo_pydantic_post(BaseModel):
    title: str
    description: str

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True


class ToDo_pydantic(BaseModel):
    id: int
    title: str
    description: str

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True
