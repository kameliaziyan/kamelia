from __future__ import annotations

MONTHLY_WORK_HOURS = 160
MONTHS_IN_YEAR = 12
ZERO_FLOAT = float(0)
PERCENT_MULTIPLIER = 100


class Employee:
    def __init__(
        self,
        employee_id: str,
        full_name: str,
        hourly_rate: float,
    ) -> None:
        self.employee_id = employee_id
        self.full_name = full_name
        self.hourly_rate = hourly_rate

    def calculate_compensation(self) -> float:
        return self.hourly_rate * MONTHLY_WORK_HOURS

    def get_info(self) -> str:
        return (
            f"Employee {self.employee_id}: {self.full_name}, "
            f"Hourly Rate: ${self.hourly_rate:.2f}/hr"
        )


class FullTimeEmployee(Employee):

    def __init__(
        self,
        employee_id: str,
        full_name: str,
        annual_salary: float,
        department_name: str,
    ) -> None:
        super().__init__(
            employee_id,
            full_name,
            hourly_rate=ZERO_FLOAT,
        )
        self.annual_salary = annual_salary
        self.department_name = department_name

    def calculate_compensation(self) -> float:
        return self.annual_salary / MONTHS_IN_YEAR

    def get_info(self) -> str:
        return (
            f"Full-Time Employee {self.employee_id}: "
            f"{self.full_name}, "
            f"Department: {self.department_name}, "
            f"Salary: ${self.annual_salary:,.2f}/year"
        )


class Manager(FullTimeEmployee):
    def __init__(
        self,
        employee_id: str,
        full_name: str,
        annual_salary: float,
        department_name: str,
        team_size: int,
        bonus_percentage: float,
    ) -> None:
        super().__init__(
            employee_id,
            full_name,
            annual_salary,
            department_name,
        )
        self.team_size = team_size
        self.bonus_percentage = bonus_percentage

    def calculate_compensation(self) -> float:
        base_salary = super().calculate_compensation()
        bonus_multiplier = 1 + self.bonus_percentage
        return base_salary * bonus_multiplier

    def get_info(self) -> str:
        bonus_percent = self.bonus_percentage * PERCENT_MULTIPLIER

        return (
            f"Manager {self.employee_id}: "
            f"{self.full_name}, "
            f"Department: {self.department_name}, "
            f"Salary: ${self.annual_salary:,.2f}/year, "
            f"Team Size: {self.team_size}, "
            f"Bonus: {bonus_percent:.0f}%"
        )
