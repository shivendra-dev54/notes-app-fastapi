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
for local docker container created with docker-compose.yml
 - postgresql+asyncpg://notes_user:notes_pass@localhost:5432/notes_db

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

| Endpoint               | Method | Description                  | Body                  	    |
| ---------------------- | ------ | ---------------------------- | ---------------------------- |
| `/api/v0/user/sign_up` | POST   | Register a new user          | {username, email, password}  |
| `/api/v0/user/sign_in` | POST   | Sign in and get tokens       | {email, password}            |
| `/api/v0/user/refresh` | POST   | Refresh access token         | {}                           |
| `/api/v0/user/logout`  | POST   | Logout and invalidate tokens | {}                           |

### Notes

| Endpoint                    | Method | Description                 | Body         |
| --------------------------- | ------ | --------------------------- | ------------ |
| `api/v0/note/create`        | POST   | Create a new note           | {content}    |
| `api/v0/note/read`          | GET    | Read notes (all or by user) | {}           |
| `api/v0/note/update/:id`    | PUT    | Update a note by ID         | {content}    |
| `api/v0/note/delete/:id`    | DELETE | Delete a note by ID         | {}           |

---

## Notes

* Passwords are hashed using **bcrypt**.
* Protected routes require **Authorization header** with Bearer token.
* Database operations are **async** for better performance.
* Uses **foreign key constraints** to automatically delete notes when a user is deleted.

---
---
# Frontend

A simple **React + Vite** frontend for the Notes App.  
Provides authentication pages, note management UI, and integration with the FastAPI backend.

---

## Tech Stack

- **Frontend Framework:** React (Vite + TypeScript)
- **State Management:** Zustand (with persistent storage)
- **Styling:** TailwindCSS (dark theme)
- **Routing:** React Router
- **API Handling:** Custom request handler with auto-refresh token support

---

## Pages

1. **Homepage (`App.tsx`)**  
   - Intro/landing page with navigation to Sign In / Sign Up.
   - Fully dark-themed (black background, white text).

2. **SignUpPage (`pages/SignUpPage.tsx`)**  
   - Form for registering a new user.
   - On success → redirects to Sign In.

3. **SignInPage (`pages/SignInPage.tsx`)**  
   - Login form (email + password).  
   - Stores `user` in Zustand store after login.  
   - Access/Refresh tokens handled automatically.

4. **MainPage (`pages/MainPage.tsx`)**  
   - Displays all user’s notes.  
   - CRUD functionality:
     - Create new notes.
     - Read all notes.
     - Update notes inline.
     - Delete notes.  
   - Logout button clears store & cookies.

---

## Components

- **Navbar (`components/Navbar.tsx`)**  
  - Navigation links (Home, Sign In, Sign Up, Main).  
  - Conditionally shows user state (if logged in or not).

---

## State Management

Zustand store (`lib/AuthStore.ts`):

- Stores user info (`id, username, email`) persistently.
- Functions: `setUser`, `logout`.
- Uses **localStorage** for persistence.

---

## API Layer

`utils/requestHandler.ts`

- Wrapper around `fetch`:
  - Automatically attaches `Authorization` header with access token.
  - Handles **401 Unauthorized** by calling `/api/v0/user/refresh` and retrying.
  - Keeps tokens updated in the store.

---

## Setup

1. Navigate to the `client` directory:

```bash
cd client
````

2. Install dependencies:

```bash
bun install
```

3. Create a `.env` file:

```env
VITE_API_URL=http://localhost:8000/api/v0
```

4. Run the development server:

```bash
bun run dev
```

---

## Notes

* All requests go through `requestHandler.ts`.
* Tokens are stored in **cookies** (HTTP-only) and user info in Zustand store.
* The app is **dark-themed** with Tailwind.
* Navigation is handled with **React Router**.

---