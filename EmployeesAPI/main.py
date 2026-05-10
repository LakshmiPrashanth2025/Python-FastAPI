from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from auth import create_token,verify_jwt

from sqlalchemy.orm import Session
from starlette import status

from database import SessionLocal, engine
from model import EmployeeDB
from schemas import Employee

app = FastAPI() # object of FastAPI class to create the application instance

# Expect Authorization: Bearer <jwt_token> in http headers
security = HTTPBearer()  #object for HTTP Bearer Token

# create the database tables based on the models
EmployeeDB.metadata.create_all(bind=engine)

@app.post('/login')  # create a route for login
def login(username: str, password: str):
    if username != 'admin' and password != 'password':
        raise HTTPException(status_code=401, detail='Invalid credentials')

    if username == 'admin' and password == 'admin123':
        token = create_token({'user': username})

    return {'access_token': token}


# tasks = []
# FastAPI automatically: # Reads the Authorization header # Extracts the Bearer token
# Creates a credentials object
def verify_token(credentials: HTTPAuthorizationCredentials =
                 Depends(security)):
    token = credentials.credentials

    #call auth.verify_jwt()
    payload = verify_jwt(token)
    if payload is None:
        raise HTTPException(status_code=401, detail='Invalid token')

    return payload


#create a dependency to get the database session
def get_db():
    db = SessionLocal() # create a new database session
    try:
        yield db # yield the session to be used in the routes
    finally:
        db.close() # close the session after use

@app.get("/") # decorator to define the route for the home page
def home():
    return {"message": "welcome to FastAPI Workshop"}

@app.post("/employees/") # decorator to define the route for adding a new employee
def add_employee(employee: Employee, db: Session= Depends(get_db),user:dict = Depends(verify_token) ):
    new_employee = EmployeeDB(
        id=employee.id,
        name=employee.name,
        email=employee.email,
        department=employee.department,
        salary=employee.salary
    )
    db.add(new_employee) # add the new employee to the session
    db.commit() # commit the transaction to save the employee in the database
    db.refresh(new_employee) # refresh the session to get the new employee data
    return {
        'message': 'employee added successfully',
    }

@app.get("/employees/")
def get_employees(db: Session = Depends(get_db),user:dict = Depends(verify_token)):
    employees = db.query(EmployeeDB).all()
    return employees

@app.put("/employees/{employee_id}") # decorator to define the route for adding a new employee
def update_employee(employee_id:int, employee:Employee, db: Session= Depends(get_db),user:dict = Depends(verify_token)):
    existing_employee_in_db = db.query(EmployeeDB).filter(EmployeeDB.id == employee_id).first()
    if not existing_employee_in_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="employee not found")
    existing_employee_in_db.name = employee.name
    existing_employee_in_db.email = employee.email
    existing_employee_in_db.department = employee.department
    existing_employee_in_db.salary = employee.salary

    db.commit() #  update the  employee in the database
    db.refresh(existing_employee_in_db) # refresh the session to get the new employee data
    return {
        'message': 'employee updated successfully',
    }


@app.delete("/employees/{employee_id}") # decorator to define the route for adding a new employee
def delete_employee(employee_id:int, db: Session= Depends(get_db),user:dict = Depends(verify_token)):
    existing_employee_in_db = db.query(EmployeeDB).filter(EmployeeDB.id == employee_id).first()
    if not existing_employee_in_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="employee not found")

    db.delete(existing_employee_in_db)
    db.commit() #  update the  employee in the database
    return {
        'message': 'employee deleted successfully',
    }
