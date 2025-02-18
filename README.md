# Gomate Backend

**Gomate** is a carpooling app backend built with Python and FastAPI. It serves as the API layer for user management, trip booking, and various other features within the **Gomate** app, supporting both passenger and driver use cases.

## Description

Gomate is a carpooling platform that connects passengers and drivers for shared rides. The backend provides the essential features, including:

- **User registration and authentication**
- **Trip booking and seat availability**
- **Passenger and driver management**
- **Cost-sharing calculations**
- **Chat and communication system**
- **Admin controls for data and fare management**

This backend is developed using the FastAPI framework, known for its high performance, easy-to-use structure, and automatic generation of documentation (Swagger UI).

## Features
- User registration and identity verification
- Searching for places/routes within a 5 km radius
- Booking trips in advance
- Displaying seat availability in the car
- Setting a destination for the Driver
- Allowing the Driver to select passengers
- Cost-sharing for trips
- Chat system between Passenger and Driver
- Review and rating system
- Issue reporting
- Tracking the vehicle's location during pickups
- Audio recording during trips for safety
- Admin management of data, fare adjustments, and in-app announcements

## Setup Instructions

Follow these steps to set up the **Gomate** backend:

### Prerequisites

- Python 3.8+ (Recommend using a virtual environment)
- Database (SQLite for development, MySQL for production)

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/gomate-backend.git
cd gomate-backend
```

### 2. Create a Virtual Environment

Create a virtual environment to isolate your Python dependencies.

```bash
python -m venv venv
```

Activate the virtual environment:

- On Windows:
    ```bash
    venv\Scripts\activate
    ```
- On macOS/Linux:
    ```bash
    source venv/bin/activate
    ```

### 3. Install Dependencies

Install the required dependencies listed in `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 4. Configure the Database

Edit the `app/database/database.py` file to set your database URL. For development, you can use SQLite, or for production, configure a MySQL database.

Example for SQLite:
```python
DATABASE_URL = "sqlite:///./test.db"
```

Example for MySQL:
```python
DATABASE_URL = "mysql://user:password@localhost/gomate_db"
```

### 5. Run the Application

Run the FastAPI application with Uvicorn:

```bash
uvicorn app.main:app --reload
```

This will start the application at `http://127.0.0.1:8000`.

### 6. Access the Documentation

Once the app is running, you can access the interactive API documentation at:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

The documentation will allow you to test the API endpoints directly from your browser.

### 7. Run Database Migrations (If applicable)

If you're using a database that requires migrations (e.g., MySQL), you can use a migration tool like Alembic (if it's set up in the project) to apply migrations.

```bash
alembic upgrade head
```

### 8. Testing the Endpoints

To test the API, you can use tools like [Postman](https://www.postman.com/) or `curl` to send HTTP requests to the endpoints.

---

## Project Structure

Here's an overview of the project structure:

```
gomate-backend/
│
├── app/
│   ├── __init__.py                # Initializes the app package
│   ├── main.py                    # FastAPI app entry point
│   ├── crud/                      # CRUD operations for interacting with DB
│   │   ├── __init__.py
│   │   └── user_crud.py           # CRUD for user management
│   ├── database/                  # Database connection and session management
│   │   ├── __init__.py
│   │   └── database.py            # DB connection setup, session management
│   ├── models/                    # SQLAlchemy models
│   │   ├── __init__.py
│   │   └── user_model.py          # User model definition
│   ├── routers/                   # API routes and endpoint definitions
│   │   ├── __init__.py
│   │   └── user_router.py         # User-related endpoints
│   ├── schemas/                   # Pydantic schemas for data validation
│   │   ├── __init__.py
│   │   └── user_schema.py         # User schema for validation
│   ├── services/                  # Business logic and service layer
│   │   ├── __init__.py
│   │   └── user_service.py        # User-related business logic
│   ├── utils/                     # Utility functions or classes
│   │   ├── __init__.py
│   │   └── auth.py                # Auth-related utilities (e.g., token generation)
│   ├── config.py                  # Configuration settings (e.g., DB URL)
│
├── requirements.txt               # List of dependencies
└── README.md                      # Project description
```

## Contributing

Feel free to fork the repository and submit pull requests with bug fixes, new features, or improvements. Please ensure that you follow the coding standards and add tests for new functionality.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

