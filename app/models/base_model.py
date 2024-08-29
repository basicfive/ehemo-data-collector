from app.db.base import Base
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.sql import func

class TimeStampModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    createdAt = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updatedAt = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now(), nullable=False)

    # @declared_attr
    # def __tablename__(cls):
    #     return cls.__name__.lower()

