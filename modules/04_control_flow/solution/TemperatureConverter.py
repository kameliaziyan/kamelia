def convert_temperature(value: float, from_unit: str, to_unit: str) -> float :
    #######################

    if from_unit not in ("C" , "F" , "K") or to_unit not in ("C" , "F" , "K") :
        raise ValueError ("Invalid unit. Use 'C' , 'F' , OR 'K' .")
    
    if from_unit == "K" and value < 0 :
        raise ValueError ("kelvin cannot be negative. ")
    
    if from_unit == "C" and value < -273.15 :
        raise ValueError ("Temperature below absolute zero .")
    




    if from_unit == to_unit :
        print(value)
        return value
    
    if from_unit == "C" and to_unit =="F" :
        print( value * 9 / 5 + 32)
        return value * 9 / 5 + 32
    if from_unit == "C" and to_unit =="K" :
        print (value + 273.15)
        return value + 273.15
    if from_unit == "F" and to_unit =="C" :
        print(( value - 32 ) * 5 / 9)
        return ( value - 32 ) * 5 / 9
    if from_unit == "F" and to_unit =="K" :
        print (( value - 32 ) * 5 / 9 + 273.15)
        return ( value - 32 ) * 5 / 9 + 273.15
    if from_unit == "K" and to_unit =="C" :
        print(value - 273.15)
        return value - 273.15
    if from_unit == "K" and to_unit =="F" :
        print(( value - 273.15 ) * 9 / 5 + 32)
        return ( value - 273.15 ) * 9 / 5 + 32
    
    

##**Conversion Formulas:**
##- Celsius to Fahrenheit: `F = C * 9/5 + 32`
##- Fahrenheit to Celsius: `C = (F - 32) * 5/9`
##- Celsius to Kelvin: `K = C + 273.15`
##- Kelvin to Celsius: `C = K - 273.15

convert_temperature(0, "C", "F")  # Returns 32.0
convert_temperature(100, "C", "K")  # Returns 373.15
convert_temperature(32, "F", "C")  # Returns 0.0
convert_temperature(0, "C", "C")  # Returns 0.0



###rite at least 3 unit tests covering different conversion scenarios and validation cases.==============
