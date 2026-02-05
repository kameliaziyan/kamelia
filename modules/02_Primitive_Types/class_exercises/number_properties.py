## Additional Challen

import sys

num = input ("enter an integer number : ")

convertNum = int(num)

print("Number :", convertNum )
typeNum = type(convertNum)
print("Type: ", typeNum )

print("Size in bytes:", sys.getsizeof(convertNum))
print("Number Squared:", convertNum ** 2)
print("As float:", float(convertNum))
print("As string:", str(convertNum))
print("Is positive:", convertNum > 0)




