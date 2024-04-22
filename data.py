from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    name = Column(String(32), primary_key=True, nullable=False)
    password = Column(String(512))

class Student(Base):
    __tablename__ = 'student'

    id = Column(String(9), primary_key=True, unique=True)
    name = Column(String(32), nullable=False)
    age = Column(Integer)
    gender = Column(String(1))
    major = Column(String(32))
    phone = Column(String(32))

class Score(Base):
    __tablename__ = 'score'

    id = Column(String(9), primary_key=True, unique=True)
    name = Column(String(32), nullable=False)
    CS1030 = Column(Integer)
    CS1100 = Column(Integer)
    CS2030 = Column(Integer)

engine = create_engine('sqlite:///students.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)