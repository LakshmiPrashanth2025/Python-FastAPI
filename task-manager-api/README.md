# 🗂️ Task Manager API (FastAPI + PostgreSQL + JWT)

A simple backend project built using **FastAPI** that allows users to manage tasks with full CRUD operations and secure APIs using JWT authentication.

---

## 🚀 Features

- ✅ FastAPI backend
- ✅ PostgreSQL database connection
- ✅ Create, Read, Update, Delete (CRUD) APIs
- ✅ Input validation using Pydantic
- ✅ Error handling with HTTPException
- ✅ JWT Authentication (Login + Secure APIs)
- ✅ Swagger UI for API testing

---

## 📁 Project Structure

```text
task_manager/
├── main.py
├── database.py
├── models.py
├── schemas.py
├── auth.py
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/LakshmiPrashanth2025/Python-FastAPI.git

cd task-manager-api
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
.\venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary python-jose
```

---

## 🗄️ Database Setup (PostgreSQL)

### Create Database

```sql
CREATE DATABASE taskdb;
```

---

## ▶️ Run Project

```bash
uvicorn main:app --reload
```

Application runs at:

```text
http://127.0.0.1:8000
```

---

## 🌐 API Documentation

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

---

## 🔐 Authentication (JWT)

### Login API

```http
POST /login
```

### Input Credentials

```text
username = admin
password = admin
```

---

## 🔑 Use Token

1. Copy token from login response
2. Click **Authorize** in Swagger UI
3. Paste:

```text
Bearer your_token_here
```

---

## 📌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/login` | Generate JWT Token |
| POST | `/tasks` | Create Task |
| GET | `/tasks` | Get All Tasks |
| GET | `/tasks/{id}` | Get Task By ID |
| PUT | `/tasks/{id}` | Update Task |
| DELETE | `/tasks/{id}` | Delete Task |

---

## 🧪 Example Request

```json
{
  "title": "Study",
  "description": "Learn FastAPI",
  "status": "pending"
}
```

---

## 🎯 Learning Outcomes

- Understanding REST APIs
- Working with FastAPI
- Database integration with PostgreSQL
- JWT Authentication
- Error handling
- Swagger/OpenAPI documentation
- CRUD API implementation
