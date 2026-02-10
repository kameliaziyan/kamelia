from typing import Dict, List, Optional

############ לשאול על ערך החזרת הפונקציה 
def calculate_statistics(**options: List[float]) -> dict :
    
    result = {}

    for name, values in options.items():
        if not values:
            result[name] = {
                "sum": None,
                "average": None,
                "min": None,
                "max": None,
            }
        else:
                result[name] = {
                "sum": sum(values),
                "average": sum(values) / len(values),
                "min": min(values),
                "max": max(values)
                
            }
    
            
    print (result)

    return result

calculate_statistics(
    temperatures=[22.5, 24.0, 23.5, 25.0],
    humidity=[60, 65, 62, 68]
)


# Output:
# {
#     'temperatures': {'sum': 95.0, 'average': 23.75, 'min': 22.5, 'max': 25.0},
#     'humidity': {'sum': 255, 'average': 63.75, 'min': 60, 'max': 68}
# }