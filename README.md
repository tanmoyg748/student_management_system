# Student Management System

A simple Student Management System built with **Python** and **Django**.

This project allows users to manage student details through a web browser. It is a beginner-friendly Django project for learning the basics of web development.

## Features

- View the list of students
- Add a new student
- Edit student details
- Delete a student
- Validate student information:
  - Name should contain letters and spaces.
  - Email should be in a valid format.
  - Phone number should contain exactly 10 digits.
  - Course should contain letters and spaces.

## Technologies Used

- Python
- Django
- HTML

## Project Structure

```text
student_management_system/
│
├── manage.py
│
├── student_management/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── students/
    ├── migrations/
    ├── templates/
    │   └── students/
    │       ├── student_list.html
    │       ├── student_form.html
    │       └── student_confirm_delete.html
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── urls.py
    ├── views.py
    └── tests.py
```

## Installation and Setup

Follow these steps to run the project on your computer.

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the Project Folder

```bash
cd student_management_system
```

### 3. Create a Virtual Environment

```bash
python -m venv myenv
```

### 4. Activate the Virtual Environment

For Windows:

```bash
myenv\Scripts\activate
```

### 5. Install Django

```bash
pip install django
```

### 6. Apply Migrations

```bash
python manage.py migrate
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

### 8. Open the Project in Your Browser

Open this URL in your browser:

```text
http://127.0.0.1:8000/
```

## How It Works

1. Open the home page to see the student list.
2. Click **Add Student** to add a new student.
3. Click **Edit** to update a student's details.
4. Click **Delete** to remove a student.

## Important Note

Currently, student information is stored in a Python list inside `students/views.py`. It is not permanently saved in the database. Therefore, newly added or updated student information will be lost when the server is restarted.

## Author

Tanmoy Ghosh

---

