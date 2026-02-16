GLOBAL_DEPARTMENTS = "departments"
GLOBAL_TEAMS = "teams"
GLOBAL_EMPLOYEES = "employees"
GLOBAL_NAMES = "name"
GLOBAL_SALARY = "salary"


def get_average_salary_by_department(company: dict) -> dict[str, float]:
    keys = [departments[GLOBAL_NAMES] for departments in company[GLOBAL_DEPARTMENTS]]
    averages = []

    for department in keys:

        given_department = [
            employees
            for departmentt in company[GLOBAL_DEPARTMENTS]
            if departmentt[GLOBAL_NAMES] == department
            for employees in departmentt[GLOBAL_TEAMS]
        ]

        salary_list = [
            employee[GLOBAL_SALARY]
            for teams in given_department
            for employee in teams[GLOBAL_EMPLOYEES]
        ]
        if salary_list:
            averages.append(sum(salary_list) / len(salary_list))
        else:
            averages.append(0)

    average_salary_department = {key: value for key, value in zip(keys, averages)}

    return average_salary_department


