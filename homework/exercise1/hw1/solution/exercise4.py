def TypeConversion (binary_number : str ) -> int :
    int_number = int(binary_number, 2)
    return int_number



binary_number = "1101"
result = TypeConversion(binary_number)
print(result)