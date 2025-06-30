# SQLBucks 

This project was made to explore Python and MySQL using SQLAlchemy and Alembic. The project is a simple banking system with basic functionalities.

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

4. **(Optional) Populate Database**:
    ```bash
    python src/populate_db.py
    ```

6. **Run the Application**:
    ```bash
    python src/app.py
    ```

## Usage

Follow the on-screen prompts to interact with the banking system.