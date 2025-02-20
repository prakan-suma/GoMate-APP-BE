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
git clone https://github.com/prakan-suma/GoMate-APP-BE.git
cd GoMate-APP-BE
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

Example for MySQL:
```python
DATABASE_URL = "mysql+pymysql://username:password@localhost/gomate_db"
```

### 5. Run the Application

Run the FastAPI application with Uvicorn:

```bash
uvicorn main:app --reload
```

This will start the application at `http://127.0.0.1:8000`.

