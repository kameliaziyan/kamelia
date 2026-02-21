import pytest
from typing import Any

from solution.all_employee_names import get_all_employee_names
from solution.employees_department import get_employees_by_department
from solution.high_earners import get_high_earners
from solution.average_salary_by_department import get_average_salary_by_department


@pytest.fixture
def company() -> dict[str, Any]:
    return {
        "departments": [
            {
                "name": "Engineering",
                "teams": [
                    {
                        "employees": [
                            {"name": "Alice", "salary": 100000},
                            {"name": "Bob", "salary": 80000},
                        ]
                    },
                    {
                        "employees": [
                            {"name": "Charlie", "salary": 120000},
                        ]
                    },
                ],
            },
            {
                "name": "HR",
                "teams": [
                    {
                        "employees": [
                            {"name": "Dana", "salary": 60000},
                            {"name": "Eli", "salary": 65000},
                        ]
                    }
                ],
            },
        ]
    }


def test_get_all_employee_names(company: dict[str, Any]) -> None:
    result = get_all_employee_names(company)
    assert sorted(result) == sorted(["Alice", "Bob", "Charlie", "Dana", "Eli"])


@pytest.mark.parametrize(
    "given, expected_result",
    [
        ("Engineering", ["Alice", "Bob", "Charlie"]),
        ("HR", ["Dana", "Eli"]),
        ("Other", []),
    ],
)
def test_get_employees_by_department(
    company: dict[str, Any],
    given: str,
    expected_result: list[str],
) -> None:
    result = get_employees_by_department(company, given)
    assert sorted(result) == sorted(expected_result)


@pytest.mark.parametrize(
    "given, expected_result",
    [
        (50000, {"Engineering": ["Alice", "Bob", "Charlie"], "HR": ["Dana", "Eli"]}),
        (95000, {"Engineering": ["Alice", "Charlie"], "HR": []}),
        (200000, {"Engineering": [], "HR": []}),
    ],
)
def test_get_high_earners(
    company: dict[str, Any],
    given: int,
    expected_result: dict[str, list[str]],
) -> None:
    result = get_high_earners(company, given)

    for result in expected_result:
        assert sorted(result[result]) == sorted(expected_result[result])


def test_get_average_salary_by_department(
    company: dict[str, Any],
) -> None:
    result = get_average_salary_by_department(company)

    assert result["Engineering"] == 100000
    assert result["HR"] == 62500
