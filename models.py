from sqlalchemy import Boolean, Column, Integer, String
from database import Base

class hired_employees(Base):
    __tablename__ = 'hired_employees'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    datetime = Column(String(20))
    deparment_id = Column(Integer, foreign_key=True)
    job_id = Column(Integer, foreign_key=True)

class deparments(Base):
    __tablename__ = 'deparments'

    id = Column(Integer, primary_key=True, index=True)
    department = Column(String(50))

class jobs(Base):
    __tablename__ = 'jobs'
    
    id = Column(Integer, primary_key=True, index=True)
    department = Column(String(50))