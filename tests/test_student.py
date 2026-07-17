from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to Student Management API"
    }


def test_create_student():

    student = {
        "id": 1,
        "name": "Kaushal",
        "age": 23,
        "course": "MCA"
    }

    response = client.post("/students", json=student)

    assert response.status_code == 200
    assert response.json()["message"] == "Student added successfully"


def test_get_students():

    response = client.get("/students")

    assert response.status_code == 200
    assert isinstance(response.json(), list)