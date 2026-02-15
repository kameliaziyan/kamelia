LOCAL_DEPARTMENTS = "departments"
LOCAL_TEAMS = "teams"
LOCAL_EMPLOYEES = "employees"
LOCAL_NAMES = "name"
LOCAL_SALARY = "salary"


def get_high_earners(company: dict, threshold: int) -> dict[str, list[str]]:
    keys = [departments[LOCAL_NAMES] for departments in company[LOCAL_DEPARTMENTS]]
    values = []

    for department in keys:
        split = [
            teams[LOCAL_EMPLOYEES]
            for departmentt in company[LOCAL_DEPARTMENTS]
            if departmentt[LOCAL_NAMES] == department
            for teams in departmentt[LOCAL_TEAMS]

        ]
        names = [
            employee[LOCAL_NAMES]
            for employees in split
            for employee in employees
            if employee[LOCAL_SALARY] > threshold
                    ]


       
        values.append(names)

    high_earners = {key: value for key, value in zip(keys, values)}

    return high_earners