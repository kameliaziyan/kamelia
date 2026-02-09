def generate_pyramid(height: int) -> str :

    if height < 1:
        raise ValueError("Height must be at least 1.")
    if height > 9:
        raise ValueError("Height cannot exceed 9.")


    ##matrix = [[0]*(height + height - 1 )]* height
    matrix = [[0 for _ in range(height + height - 1)] for _ in range(height)]

    middle = height - 1
    for i in range (height) :
        for j in range (height + height - 1 ) :
                        
            value = i + 1 - abs(j - middle)
            if value > 0:
                matrix[i][j] = value

            ##matrix[i][j] = 1

    ##or row in matrix:
    ##    print(row)


    ##for row in matrix:
    ##   print("".join(str(num) for num in row))
        
    for row in matrix:
        print("".join(str(num) if num != 0 else " " for num in row)) ## רק לקחתי את צורת ההדפסה הזו מצאט כי שכחתי את הסינטאקס 


    return ("".join(str(num) if num != 0 else " " for num in row))

generate_pyramid(4)
generate_pyramid(2)
generate_pyramid(7)


