from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from database import Base, engine

# from . import (
#      Column, String, Boolean, UUID, uuid4, JSONB, ForeignKey, ARRAY,
#     DateTime, BigInteger, Sequence, event, DDL, UniqueConstraint, Integer
# )
# from datetime import datetime
# from config.app_config import DEFAULT_USER_IMAGE
# from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base()

# class User(Base):
#     __tablename__ = "users"

#     id = Column(
#         UUID(as_uuid=True), primary_key=True, default=uuid4, unique=True,
#         nullable=False
#     )
#     public_id = Column(
#         BigInteger, Sequence('user_public_id_seq'), unique=True,
#         nullable=False
#     )

#     created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
#     email = Column(String, unique=True, nullable=False)
#     password = Column(String, nullable=False)
#     first_name = Column(String, nullable=False)
#     last_name = Column(String, nullable=False)
#     phone_number = Column(String, nullable=True, unique=True)
#     address = Column(JSONB, nullable=True)
#     profile_image = Column(String, default=DEFAULT_USER_IMAGE)
#     years_angling = Column(String, nullable=True)
  



class Questions(Base):
    __tablename__ = "Questions"

    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(ARRAY(String), default=[])
    description = Column(String, nullable=True)
    options = fields.dropdownChoices(null=True)
    answered  = Column(Boolean, default=False)
    question_type = Column(String, nullable=True)



class Anwer(Base):
    __tablename__ = "Answer"

    id = Column(Integer, primary_key=True, index=True)
    answer = Column(String, nullable=True)
    question

class dropdownChoices(str, Enum):
    employee = "EMPLOYEE"
    dependent_contractor = "DEPENDENT_CONTRACTOR"
    professional = "PROFESSIONAL"
    scientific = "SCIENTIFIC"
    technical = "TECHNICAL"
    componsation = "60000"
    alberta = "ALBERTA"
    british_columbia = "BRITISH_COLUMBIA"
    manitoba = "MANITOBA"
    new_brunswick = "NEW_BRUNSWICK"
    nova_scotia = "NOVA_SCOTIA"
    ontario = "ONTARIO"
    new_foundland_and_labrour = "NEW_FOUNDLAND_AND_LABROUR"

Base.metadata.create_all(bind=engine)