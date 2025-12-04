**Expense & Budget Tracking Application**

A Python-based web application. This tool allows users to track daily expenses, categorize spending, and set monthly budgets with an automated alert system.

**Table of Contents:**

    1.Tech Stack
    2.Prerequisites
    3.How to Run (Docker)
    4.How to Run (Manual)
    5.Test Scenarios
    6.Project Structure

**Tech Stack:**

    Language: Python 3.9
    Framework: Flask (Web Backend)
    Database: SQLite (Relational DB)
    ORM: SQLAlchemy (Data Abstraction)
    Containerization: Docker
    Frontend: HTML5, CSS3, Jinja2 Templates


**Prerequisites:**

    To run this application, you need either:
        Docker Desktop installed and running (Recommended).
        Python 3.x installed locally.


**How to Run (Using Docker) Recommended**

    Easiest way to run the application as it handles all dependencies automatically.

    1.  Open your terminal in the project directory.

    2.  Build the Docker Image: (bash)
        docker build -t expense-tracker .
    
    3.  Run the Container: (bash)
        docker run -p 5000:5000 expense-tracker

    4.  Access the Application:
        Open your web browser and go to: http://localhost:5000


**How to Run (Manually)**

    If you want to run manually, follow these steps:

    1.  Install Dependencies: (bash)
        pip install -r requirements.txt
    
    2.  Start the Application: (bash)
        python app.py
    
    3.  Access the Application:
        Navigate to http://localhost:5000 in your browser.



**Test Steps (Validation)**

    **Test Case 1: Create a Category & Budget**

    1.  Navigate to "Add New Category" section on the dashboard.
    2.  Input Name: Food
    3.  Input Budget Limit: 2000
    4.  Click "Set Budget".
    5.  Validation: Verify that Food appears in the "Financial Summary" table at the bottom with a Limit of $2000 and Balance of $2000.

    **Test Case 2: Log an Expense (Normal)**

    1.  Navigate to "Log Daily Expense" section.
    2.  Select Category: Food
    3.  Input Cost: 500
    4.  Input Description: Lunch
    5.  Click "Save Expense".
    6.  Validation:
        A green "Success" message appears.
        The Summary Table updates: Spent becomes $500, Balance becomes $1500.
        Status shows "On Track".

    **Test Case 3: Log an Expense (Trigger Alert)**
    1.  Log another expense for Food.
    2.  Input Cost: 1600 (Note: This exceeds the remaining balance of $1500).
    3.  Click "Save Expense".
    4.  Validation:
        A Red Alert Banner appears at the top: "Alert: You have exceeded the limit on Food!".
        The Summary Table Status changes to "OVER BUDGET!" in red text.

**Project Structure**

    |- app.py               # Application Logic
    |- models.py            # Schema
    |- Dockerfile           # Docker configuration
    |- requirements.txt     # Dependencies
    |- README.md            # Documentation & Setup Guide
    |- templates/
        |-- index.html      # UI



    
