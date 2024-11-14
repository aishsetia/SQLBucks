# Bank Of E - A Modernized Class 12th CBSE CS Project

This is a modernized version of the class 12th CBSE Computer Science project, coded in Python. It now uses SQLAlchemy ORM for database interactions and Alembic for database migrations, implementing better security and schema management practices.

## Prerequisites

- Python 3.8+
- MySQL Server

## Installation

1. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2. **Set Up Environment Variables**:
    - Create a `.env` file with your database credentials:
      ```
      DB_HOST=localhost
      DB_USER=root
      DB_PASSWORD=`YOUR_PASSWORD`
      DB_NAME=sqlbucks
      ```

3. **Run Database Migrations**:
    ```bash
    alembic upgrade head
    ```

4. **Run the Application**:
    ```bash
    python app.py
    ```

## Usage

Follow the on-screen prompts to interact with the banking system.