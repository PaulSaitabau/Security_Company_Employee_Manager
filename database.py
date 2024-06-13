from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class OperationsGuard(Base):
    __tablename__ = 'operations_guards'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    start_date = Column(Date)
    assignment = Column(String)
    shift = Column(String)
    location = Column(String)

class ManagementGuard(Base):
    __tablename__ = 'management_guards'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    start_date = Column(Date)
    assignment = Column(String)
    shift = Column(String)
    location = Column(String)

    if __name__ == "__main__":
         engine = create_engine('sqlite:///security_company.db')
         Base.metadata.create_all(engine)