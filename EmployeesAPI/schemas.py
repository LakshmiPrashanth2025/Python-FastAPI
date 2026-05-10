# we use pydantic to create the schema for the employee data
from pydantic import BaseModel

class Employee(BaseModel):
    id: int
    name: str
    email: str
    department: str
    salary: float