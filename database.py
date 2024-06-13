from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Guard(Base):
    __tablename__ = 'guards'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    start_date = Column(Date)
    assignment = Column(String)
    shift = Column(String)
    location = Column(String)
    incidents = relationship("Incident", back_populates="guard")

class Incident(Base):
    __tablename__ = 'incidents'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    description = Column(String)
    guard_id = Column(Integer, ForeignKey('guards.id'))
    department = Column(String)
    guard = relationship("Guard", back_populates="incidents")
