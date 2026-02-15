LOCAL_DEPARTMENTS = "departments"
LOCAL_TEAMS = "teams"
LOCAL_EMPLOYEES = "employees"
LOCAL_NAMES = "name"
LOCAL_SALARY = "salary"



def get_average_salary_by_department(company: dict) -> dict[str, float]:
    keys = [departments[LOCAL_NAMES] for departments in company[LOCAL_DEPARTMENTS]]
    averages = []

    for department in keys:

        given_department = [
            employees
            for departmentt in company[LOCAL_DEPARTMENTS]
            if departmentt[LOCAL_NAMES] == department
            for employees in departmentt[LOCAL_TEAMS]

        ]

        salary_list = [
            employee[LOCAL_SALARY]
            for teams in given_department
            for employee in teams[LOCAL_EMPLOYEES]
        ]
        if salary_list:
                calculate_average = sum(salary_list) / len(salary_list)
                averages.append(calculate_average)
        else:
                averages.append(0)

    average_salary_department = {key: value for key, value in zip(keys, averages)}

    return average_salary_department


