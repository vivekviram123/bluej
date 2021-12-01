from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from database import Base, engine

from . import (
   Column, String, Integer, UUID, uuid4,
    DateTime, Boolean, ARRAY, Sequence
)
from datetime import datetime
# from config.app_config import DEFAULT_USER_IMAGE
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Questions(Base):
    __tablename__ = "Questions"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    question_text = Column(String, nullable=False)
    options = Column(ARRAY(String))
    question_type = Column(String, nullable=True)


class Answer(Base):
    __tablename__ = "Answer"

    id = Column(Integer, primary_key=True, index=True)
    answer = Column(String, nullable=True)

# class DropdownChoices(str, Enum):
#     employee = "EMPLOYEE"
#     dependent_contractor = "DEPENDENT_CONTRACTOR"
#     professional = "PROFESSIONAL"
#     scientific = "SCIENTIFIC"
#     technical = "TECHNICAL"
#     componsation = "60000"
#     alberta = "ALBERTA"
#     british_columbia = "BRITISH_COLUMBIA"
#     manitoba = "MANITOBA"
#     new_brunswick = "NEW_BRUNSWICK"
#     nova_scotia = "NOVA_SCOTIA"
#     ontario = "ONTARIO"
#     new_foundland_and_labrour = "NEW_FOUNDLAND_AND_LABROUR"

Base.metadata.create_all(bind=engine)