from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class OperationsGuard(Base):
    __tablename__ = 'operations_guards'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    start_date = Column(Date)
    assignment = Column(String)
    shift = Column(String)
    location = Column(String)
    incidents = relationship("Incident", back_populates="guard")