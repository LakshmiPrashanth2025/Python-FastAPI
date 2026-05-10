#this use for the create database tabble
from sqlalchemy import Column, Integer, String, Float
from database import Base

class EmployeeDB(Base):

    __tablename__ = "employees" # name of the table in the database

    id = Column(Integer, primary_key=True, index=True) # id column as primary key
    name = Column(String) # name column
    email = Column(String) # email column with unique constraint
    department = Column(String) # department column
    salary = Column(Float) # salary column
#this file use for the create schema for the employee data

from pydantic import BaseModel

