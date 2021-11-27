import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import declarative_base, Session
from typing import Optional, List

from database import get_db
from models import ToDo
from schema import ToDo_pydantic, ToDo_pydantic_post

app = FastAPI()


@app.get("/", response_model=List[ToDo_pydantic])
def todo_list(db: Session = Depends(get_db)):
    """
    Api to get list of TODO.
    :return: [{id, title, description},]
    """
    return db.query(ToDo).all()


@app.post("/to-do/", response_model=ToDo_pydantic)
def create_todo_view(todo: ToDo_pydantic_post, db: Session = Depends(get_db)):
    """
    Api to create a TODO.
    :param todo: {title, description}
    :return: {id, title, description}
    """
    todo_task = ToDo(**todo.dict())
    db.add(todo_task)
    db.commit()
    db.refresh(todo_task)
    return todo_task


@app.get('/to-do/{todo_id}', response_model=ToDo_pydantic)
def get_todo_view(todo_id: int, db: Session = Depends(get_db)):
    """
    Api to get a single TODO with todo_id
    :param todo_id: todo_id got form list or create api
    :return: {id, title, description}
    """
    todo = db.query(ToDo).where(ToDo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=400, detail="Oops!! ToDo not found!")
    return todo


@app.put('/to-do/', response_model=ToDo_pydantic)
def update_todo_view(todo: ToDo_pydantic, db: Session = Depends(get_db)):
    """
    Api to update a TODO.
    :param todo: {id, title, description}
    :return: {id, title, description}
    """
    todo_dict = todo.dict()
    todo = db.query(ToDo).where(ToDo.id == todo_dict['id']).first()
    if not todo:
        raise HTTPException(status_code=400, detail="Oops!! ToDo not found!")
    todo.title = todo_dict['title']
    todo.description = todo_dict['description']
    db.add(todo)
    db.commit()
    return todo


@app.delete('/to-do/{todo_id}')
def delete_todo_view(todo_id: int, db: Session = Depends(get_db)):
    """
        Api to delete a TODO with todo_id
        :param todo_id: todo_id got form list or create api
        """
    try:
        db.query(ToDo).filter(ToDo.id == todo_id).delete()
        db.commit()
        return {"message": "ToDo item successfully deleted"}
    except:
        raise HTTPException(status_code=400, detail="Oops!! ToDo not found!")


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
