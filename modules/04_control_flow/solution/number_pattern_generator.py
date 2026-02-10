def generate_pyramid(height: int) -> str:

    if height < 1:
        raise ValueError("Height must be at least 1.")
    if height > 9:
        raise ValueError("Height cannot exceed 9.")

    matrix = []

    # יצירת מטריצה מלאה באפסים
    for i in range(height):
        row = []
        for j in range(height * 2 - 1):
            row.append(0)
        matrix.append(row)

    middle = height - 1
    for i in range(height):
        for j in range(height * 2 - 1):
            value = i + 1 - abs(j - middle)
            if value > 0:
                matrix[i][j] = value

    result = ""

    for row in matrix:
        line = ""
        for num in row:
            if num != 0:
                line = line + str(num)
            else:
                line = line + " "
        result = result + line + "\n"

    print (result)
    return result


generate_pyramid(4)
generate_pyramid(2)
generate_pyramid(7)


