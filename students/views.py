from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound, HttpRequest, HttpResponse
import re


# Each student is stored as a dictionary containing the student's details.
students: list[dict[str, int | str]] = [
    {
        "id": 1,
        "name": "Rahul",
        "email": "rahul@gmail.com",
        "phone": "9876543210",
        "course": "Python"
    },
    {
        "id": 2,
        "name": "Priya",
        "email": "priya@gmail.com",
        "phone": "9876543211",
        "course": "Django"
    },
    {
        "id": 3,
        "name": "Amit",
        "email": "amit@gmail.com",
        "phone": "9876543212",
        "course": "Java"
    }
]


def validate_student(
    name: str,
    email: str,
    phone: str,
    course: str
) -> dict[str, str]:

    errors: dict[str, str] = {}

    if not re.fullmatch(r"[A-Za-z ]{2,50}", name):
        errors["name"] = (
            "Name must contain only letters and spaces."
        )

    if not re.fullmatch(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}",
        email
    ):
        errors["email"] = "Enter a valid email address."

    if not re.fullmatch(r"\\d{10}", phone):
        errors["phone"] = (
            "Phone number must contain exactly 10 digits."
        )

    if not re.fullmatch(r"[A-Za-z ]{2,50}", course):
        errors["course"] = (
            "Course must contain only letters and spaces."
        )

    return errors


def student_list(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "students/student_list.html",
        {"students": students}
    )


def add_student(request: HttpRequest) -> HttpResponse:

    if request.method == "POST":

        name: str = request.POST.get("name", "").strip()
        email: str = request.POST.get("email", "").strip()
        phone: str = request.POST.get("phone", "").strip()
        course: str = request.POST.get("course", "").strip()

        errors: dict[str, str] = validate_student(name, email, phone, course)

        if errors:
            return render(
                request,
                "students/student_form.html",
                {
                    "errors": errors,
                    "student": request.POST,
                    "title": "Add Student"
                }
            )

        new_id: int = max(
            [int(student["id"]) for student in students],
            default=0
        ) + 1

        new_student: dict[str, int | str] = {
            "id": new_id,
            "name": name,
            "email": email,
            "phone": phone,
            "course": course
        }
        students.append(new_student)

        return redirect("student_list")

    return render(
        request,
        "students/student_form.html",
        {
            "title": "Add Student"
        }
    )


def edit_student(request: HttpRequest, id: int) -> HttpResponse:

    student: dict[str, int | str] | None = next(
        (
            student for student in students
            if student["id"] == id
        ),
        None
    )

    if not student:
        return HttpResponseNotFound("Student not found")

    if request.method == "POST":

        name: str = request.POST.get("name", "").strip()
        email: str = request.POST.get("email", "").strip()
        phone: str = request.POST.get("phone", "").strip()
        course: str = request.POST.get("course", "").strip()

        errors: dict[str, str] = validate_student(
            name, email, phone, course
        )

        if errors:
            return render(
                request,
                "students/student_form.html",
                {
                    "errors": errors,
                    "student": {
                        "id": id,
                        "name": name,
                        "email": email,
                        "phone": phone,
                        "course": course
                    },
                    "title": "Edit Student"
                }
            )

        student["name"] = name
        student["email"] = email
        student["phone"] = phone
        student["course"] = course

        return redirect("student_list")

    return render(
        request,
        "students/student_form.html",
        {
            "student": student,
            "title": "Edit Student"
        }
    )


def delete_student(request: HttpRequest, id: int) -> HttpResponse:

    student: dict[str, int | str] | None = next(
        (
            student for student in students
            if student["id"] == id
        ),
        None
    )

    if not student:
        return HttpResponseNotFound("Student not found")

    if request.method == "POST":
        students.remove(student)
        return redirect("student_list")

    return render(
        request,
        "students/student_confirm_delete.html",
        {"student": student}
    )
