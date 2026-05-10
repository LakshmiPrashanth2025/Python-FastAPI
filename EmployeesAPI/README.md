# Python-FastAPI  -  REST API Project

Explored FastAPI with hands-on implementation of REST APIs, JWT authentication, Python database connectivity, and ORM mappings.

## Implemented Features

- REST API development using FastAPI decorators  
- JWT token generation and validation  
- Protected APIs with Bearer Authentication  
- Database integration using SQLAlchemy ORM  
- CRUD operations with ORM mappings  
- Request validation using Pydantic schemas  

FastAPI provides a clean, modern, and high-performance approach for building secure backend APIs with minimal boilerplate code.

# Installation and Setup

## Clone Repository

```bash
git clone https://github.com/LakshmiPrashanth2025/Python-FastAPI.git
```

Navigate to project folder:

```bash
cd Python-FastAPI/EmployeesAPI
```

---

# Create Virtual Environment

## Windows

```bash
python -m venv venv
.\venv\Scripts\activate
```

---

# Install Dependencies

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary python-jose python-jwt
```

---

# Additional Recommended Packages

```bash
pip install passlib[bcrypt] python-multipart
```

---

# Package Purpose

| Package | Purpose |
|---|---|
| fastapi | REST API Framework |
| uvicorn | ASGI Server |
| sqlalchemy | ORM Framework |
| psycopg2-binary | PostgreSQL Driver |
| python-jose | JWT Token Handling |
| passlib[bcrypt] | Password Hashing |
| python-multipart | Form Data Support |

---

# PostgreSQL Database Setup

Create PostgreSQL database:

```sql
CREATE DATABASE employee_db;
```

---

# Configure Database Connection

Update `DATABASE_URL` inside:

```text
database.py
```

Example:

```python
DATABASE_URL = "postgresql://postgres:password@localhost:5432/employee_db"
```

If password contains special characters like `@`, use URL encoding.

Example:

```python
DATABASE_URL = "postgresql://postgres:Candy%4001@localhost:5432/employee_db"
```

---

# Run Application

Start FastAPI server:

```bash
uvicorn main:app --reload
```

Application starts at:

```text
http://127.0.0.1:8000
```

---

# Swagger API Documentation

FastAPI automatically generates Swagger/OpenAPI documentation.

## Swagger UI

Open:

```text
http://127.0.0.1:8000/docs
```

---

## ReDoc Documentation

Open:

```text
http://127.0.0.1:8000/redoc
```

---

# API Testing Using Swagger

1. Open Swagger UI
2. Select API endpoint
3. Click "Try it out"
4. Enter request payload
5. Execute API request
6. View API response instantly

---

# JWT Authentication Flow

```text
User Login
    ↓
JWT Token Generated
    ↓
Bearer Token Returned
    ↓
Authorization Header Validation
    ↓
Protected API Access
```

Authorization Header Example:

```text
Authorization: Bearer <JWT_TOKEN>
```

---

# Example Run Command

Development Mode:

```bash
uvicorn main:app --reload
```

Production Mode:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

---

# Common Fixes

## Uvicorn Reload Error

Wrong:

```bash
uvicorn main:app –reload
```

Correct:

```bash
uvicorn main:app --reload
```

Use double hyphen `--`.

---

# PostgreSQL Connection Error

Wrong:

```text
postgresql://postgres:Candy@01@localhost:5432/employee_db
```

Correct:

```text
postgresql://postgres:Candy%4001@localhost:5432/employee_db
```

Reason:

`@` must be URL encoded inside connection URLs.

---
