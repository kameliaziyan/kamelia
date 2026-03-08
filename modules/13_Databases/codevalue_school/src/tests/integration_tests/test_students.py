import pytest
from httpx import AsyncClient


async def test_health_check(ac: AsyncClient) -> None:
    response = await ac.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}


async def test_get_all_students_returns_list(ac: AsyncClient) -> None:
    response = await ac.get("/students/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 3


async def test_create_student(ac: AsyncClient) -> None:
    payload = {
        "first_name": "Eve",
        "last_name": "Mizrahi",
        "email": "eve.mizrahi@school.com",
        "birth_date": "2001-03-20",
    }
    response = await ac.post("/students/", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "eve.mizrahi@school.com"
    assert data["first_name"] == "Eve"
    assert "student_id" in data


async def test_get_student_by_id(ac: AsyncClient) -> None:
    all_response = await ac.get("/students/")
    students = all_response.json()
    student_id = students[0]["student_id"]

    response = await ac.get(f"/students/{student_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["student_id"] == student_id


async def test_get_student_not_found(ac: AsyncClient) -> None:
    response = await ac.get("/students/99999")
    assert response.status_code == 404


async def test_update_student(ac: AsyncClient) -> None:
    all_response = await ac.get("/students/")
    students = all_response.json()
    student_id = students[0]["student_id"]

    payload = {"first_name": "Alicia"}
    response = await ac.put(f"/students/{student_id}", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["first_name"] == "Alicia"


async def test_delete_student(ac: AsyncClient) -> None:
    payload = {
        "first_name": "Temp",
        "last_name": "Student",
        "email": "temp.student@school.com",
    }
    create_response = await ac.post("/students/", json=payload)
    student_id = create_response.json()["student_id"]

    response = await ac.delete(f"/students/{student_id}")
    assert response.status_code == 204

    get_response = await ac.get(f"/students/{student_id}")
    assert get_response.status_code == 404


async def test_delete_student_not_found(ac: AsyncClient) -> None:
    response = await ac.delete("/students/99999")
    assert response.status_code == 404
