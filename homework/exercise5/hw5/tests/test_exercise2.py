from solution.exercise2 import Employee, FullTimeEmployee, Manager


def test_employee_compensation() -> None:
    david = Employee("E101", "David Cohen", 32.5)
    assert david.calculate_compensation() == 32.5 * 160


def test_fulltime_compensation() -> None:
    maya = FullTimeEmployee("E102", "Maya Levi", 84000, "Marketing")
    assert maya.calculate_compensation() == 84000 / 12


def test_manager_compensation() -> None:
    noam = Manager("E103", "Noam Adler", 132000, "Finance", 6, 0.12)
    expected = (132000 / 12) * 1.12
    assert noam.calculate_compensation() == expected


def test_total_payroll() -> None:
    emp1 = Employee("E201", "Lior Katz", 28.0)
    emp2 = FullTimeEmployee("E202", "Shira Gold", 72000, "Sales")
    emp3 = Manager("E203", "Omer Rubin", 110000, "Operations", 4, 0.08)

    employees = [emp1, emp2, emp3]
    total = sum(emp.calculate_compensation() for emp in employees)

    expected_total = 28.0 * 160 + 72000 / 12 + (110000 / 12) * 1.08

    assert total == expected_total


def test_information_contains() -> None:
    yael = Manager("E301", "Yael Mor", 140000, "R&D", 10, 0.2)

    info = yael.get_info()

    assert "Yael Mor" in info
    assert "R&D" in info
    assert "Team Size" in info
    assert "Bonus" in info
