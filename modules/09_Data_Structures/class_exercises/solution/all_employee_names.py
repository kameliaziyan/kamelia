LOCAL_DEPARTMENTS = "departments"
LOCAL_TEAMS = "teams"
LOCAL_EMPLOYEES = "employees"
LOCAL_NAMES = "name"
LOCAL_SALARY = "salary"


def get_all_employee_names(company: dict) -> list[str]:
    # matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # flattened = [num for row in matrix for num in row]
    teams = [
        team
        for department in company[LOCAL_DEPARTMENTS]
        for team in department[LOCAL_TEAMS]
    ]
    result = [
        employee[LOCAL_NAMES] for team in teams for employee in team[LOCAL_EMPLOYEES]
    ]
    return result
