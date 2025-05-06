# Flask CRUD REST API

A lightweight Flask-based CRUD API for managing users, containerized with Docker and backed by PostgreSQL.

## 🛠 Tech Stack

- Python 3.6
- Flask & SQLAlchemy
- PostgreSQL
- Docker & Docker Compose

---

## 📁 Project Structure

```bash
├── app.py              # Flask application with CRUD endpoints
├── requirements.txt    # Python dependencies
├── Dockerfile          # Flask app container
├── docker-compose.yml  # Orchestrates Flask + PostgreSQL containers
```

## 🚀 Getting Started
### 1. Clone the repository
```
git clone https://github.com/your-username/flask-live-crud.git
cd flask-live-crud
```
### 2. Build and run with Docker Compose
```
docker-compose up --build
```
- The API will be available at: http://localhost:4000

## 📦 API Endpoints
All responses are JSON-formatted.

| Method | Endpoint        | Description         |
|--------|-----------------|---------------------|
| GET    | /test           | Test the API        |
| POST   | /users          | Create a new user   |
| GET    | /users          | Get all users       |
| GET    | /users/<id>     | Get a specific user |
| PUT    | /users/<id>     | Update a user       |
| DELETE | /users/<id>     | Delete a user       |



## 🧪 Testing the API with Postman
1. Open Postman.
2. Use the following examples:

## ➕ Create a User
- Method: POST
- URL: http://localhost:4000/users
- Body (JSON):
```
{
  "username": "johndoe",
  "email": "john@example.com"
}
```
## 📄 Get All Users
- Method: GET
- URL: http://localhost:4000/users

## ✏️ Update a User
- Method: PUT
- URL: http://localhost:4000/users/1
- Body (JSON):
```
{
  "username": "johnupdated",
  "email": "updated@example.com"
}
```
## ❌ Delete a User
- Method: DELETE
- URL: http://localhost:4000/users/1

## 🗃 View the Database with TablePlus
1. Open TablePlus and create a new PostgreSQL connection:
- Host: localhost
- Port: 5432
- User: postgres
- Password: postgres
- Database: postgres
2. Once connected, explore the users table to view, edit, or delete entries.

## 🧹 Cleanup
To stop and remove all containers, run:
```
docker-compose down
```
To delete volumes and clean DB data:
```
docker-compose down -v
```
## 💡 Notes
- This app uses SQLAlchemy to handle migrations.
- Container ports are exposed at 4000 for the Flask app and 5432 for the DB.

