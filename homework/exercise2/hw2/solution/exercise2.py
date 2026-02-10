  #- "add 2 t0 5" 
  #- "subtract 2 from 5"
  #- "multiply 2 by 5"
  #- "divide 10 by 5"

def add(line : list[str] ) -> str:
    if line[2] == "to" :
         
        a = int(line[1])
        b = int(line[3])

        result = a + b
        return (f"The answer is {result}")
    else:
        return("invalid operation")
    

         


def subtract(line : list[str] ) -> str :
    if line[2] == "from" :
         
        a = int(line[1])
        b = int(line[3])

        result = b - a
        return (f"The answer is {result}")
    else:
        return("invalid operation")

def multiply(line : list[str] ) -> str :
    if line[2] == "by" :
         
        a = int(line[1])
        b = int(line[3])

        result = a * b
        return (f"The answer is {result}")
    else:
        return("invalid operation")

def divide(line : list[str] ) -> str :
    if line[2] == "by" :
         
        a = int(line[1])
        b = int(line[3])
        if b == 0 :
            print("invalid operation")
            return


        result = a / b
        return (f"The answer is {result}")
    else:
        return("invalid operation")

def Calculator( ) -> None:

    while True:
        data = input("enters a valid operation ")
        if not data :
             print("invalid operation")
             continue
        

        if data.lower() == 'exit':
                break
        
        words = data.split()

        if len(words) == 1:
            if words[0] == "help":
                print(
            "Available commands:\n"
            "add 2 to 5\n"
            "subtract 2 from 5\n"
            "multiply 2 by 5\n"
            "divide 10 by 5\n"
        )
                continue
            else:
                print("invalid operation")
                continue




        if len(words) not in (1, 4):
            print("invalid operation")
            continue


        try:
            a = int(words[1])
            b = int(words[3])
        except ValueError:
            print("invalid operation")
            continue


        if words[0] == "add":
             print (add(words))
             continue
        
        if words[0] == "subtract":
             print (subtract(words))
             continue
        
        if words[0] == "divide":
             print (divide(words))
             continue
        
        if words[0] == "multiply":
             print (multiply(words))
             continue
        

        else :
            print( "invalid operation")
            continue

             

    return

#multiply 2 by 5
print(Calculator())
