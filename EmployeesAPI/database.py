from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

                             #username:password@db name
DATABASE_URL = "postgresql://postgres:Candy%4001@localhost:5432/employee_db"

engine = create_engine(DATABASE_URL) # create the database engine

SessionLocal = sessionmaker( bind=engine) # create a session factory

Base = declarative_base() # create a base class for the models


