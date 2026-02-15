LOCAL_DEPARTMENTS = "departments"
LOCAL_TEAMS = "teams"
LOCAL_EMPLOYEES = "employees"
LOCAL_NAMES = "name"
LOCAL_SALARY = "salary"

def get_employees_by_department(company: dict, department: str) -> list[str]:
        teams = [
                 team
                 for dept in company[LOCAL_DEPARTMENTS]
                 if dept[LOCAL_NAMES] == department
                 for team in dept[LOCAL_TEAMS]
                ]

        result = [
        employee[LOCAL_NAMES] for team in teams for employee in team[LOCAL_EMPLOYEES]
                         ]
        return result
    