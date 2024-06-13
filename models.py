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

    class ManagementGuard(Base):
     __tablename__ = 'management_guards'
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
    guard_id = Column(Integer, ForeignKey('operations_guards.id'))  # Add foreign key relationship to OperationsGuard
    department = Column(String)  # New column to store the department of the guard
    guard = relationship("OperationsGuard", back_populates="incidents")  # Use OperationsGuard as the relationship target
