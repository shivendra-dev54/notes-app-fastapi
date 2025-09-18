# Notes App

A simple **Notes Application backend** built with **FastAPI** and **PostgreSQL (NeonDB)**. Supports user authentication, CRUD operations on notes, and token-based security.

## Features

* User registration and login with hashed passwords.
* JWT-based authentication with **access token (15 min)** and **refresh token (7 days)**.
* CRUD operations for notes (Create, Read, Update, Delete).
* Relationship between **User** and **Notes**.
* Middleware to protect routes using JWT verification.
* Async database operations using SQLAlchemy with AsyncSession.

---
---
# Backend
## Tech Stack

* **Backend:** FastAPI
* **Database:** PostgreSQL (NeonDB)
* **ORM:** SQLAlchemy (Async)
* **Password Hashing:** passlib (bcrypt)
* **Token Handling:** JWT

---

## Database Schema

### Users Table

| Column         | Type     | Notes             |
| -------------- | -------- | ----------------- |
| id             | Integer  | Primary Key       |
| username       | String   | Required          |
| email          | String   | Unique, Required  |
| password       | String   | Hashed            |
| created\_at    | DateTime | Auto timestamp    |
| access\_token  | String   | JWT access token  |
| refresh\_token | String   | JWT refresh token |

### Notes Table

| Column      | Type     | Notes                            |
| ----------- | -------- | -------------------------------- |
| id          | Integer  | Primary Key                      |
| user\_id    | Integer  | Foreign key → Users.id (CASCADE) |
| content     | String   | Note content                     |
| created\_at | DateTime | Auto timestamp                   |
| updated\_at | DateTime | Auto updated on change           |

---

## Installation

1. Clone the repository:

```bash
git clone git@github.com:shivendra-dev54/notes-app-fastapi.git
cd notes-app-fastapi/server
```

2. Create a virtual environment:

```bash
python -m venv venv_notes
source venv_notes/bin/activate   # Linux/macOS
venv_notes\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in `src/config`:

```env
db_connection_string=postgresql+asyncpg://<username>:<password>@<host>:<port>/<database>
SECRET_KEY=<your-jwt-secret-key>
```

5. Create database tables:

```bash
python -m src.db.create_tables
```

---

## Running the Server

```bash
uvicorn src.main:app --reload
```

* **API Docs:** [http://localhost:8000/docs](http://localhost:8000/docs)

---

## API Endpoints

### User Authentication

| Endpoint               | Method | Description                  |
| ---------------------- | ------ | ---------------------------- |
| `/api/v0/user/sign_up` | POST   | Register a new user          |
| `/api/v0/user/sign_in` | POST   | Sign in and get tokens       |
| `/api/v0/user/refresh` | POST   | Refresh access token         |
| `/api/v0/user/logout`  | POST   | Logout and invalidate tokens |

### Notes

| Endpoint       | Method | Description                 |
| -------------- | ------ | --------------------------- |
| `/note/create` | POST   | Create a new note           |
| `/note/read`   | GET    | Read notes (all or by user) |
| `/note/update` | PUT    | Update a note by ID         |
| `/note/delete` | DELETE | Delete a note by ID         |

---

## Notes

* Passwords are hashed using **bcrypt**.
* Protected routes require **Authorization header** with Bearer token.
* Database operations are **async** for better performance.
* Uses **foreign key constraints** to automatically delete notes when a user is deleted.

---
---
# Frontend
