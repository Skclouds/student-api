from fastapi import APIRouter, HTTPException
from app.models import Student

router = APIRouter()

# Temporary in-memory storage
students = []

# Home API
@router.get("/")
def home():
    return {"message": "Welcome to Student Management API"}

# Create Student
@router.post("/students")
def create_student(student: Student):
    students.append(student)
    return {
        "message": "Student added successfully",
        "student": student
    }

# Get All Students
@router.get("/students")
def get_students():
    return students

# Get Student by ID
@router.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student.id == student_id:
            return student

    raise HTTPException(status_code=404, detail="Student not found")

# Update Student
@router.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):

    for index, student in enumerate(students):
        if student.id == student_id:
            students[index] = updated_student
            return {
                "message": "Student updated successfully",
                "student": updated_student
            }

    raise HTTPException(status_code=404, detail="Student not found")

# Delete Student
@router.delete("/students/{student_id}")
def delete_student(student_id: int):

    for index, student in enumerate(students):
        if student.id == student_id:
            deleted = students.pop(index)
            return {
                "message": "Student deleted successfully",
                "student": deleted
            }

    raise HTTPException(status_code=404, detail="Student not found")