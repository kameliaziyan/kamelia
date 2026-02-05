## Exercise 3:

a = input ("enter the first number : ")
a = int(a)
b = input ("enter the second number : ")
b = int(b)
c = input ("enter the third number : ")
c = int (c)

print("Is a equal to c?", a == c)
print("Is a less than b?", a < b)
print("Is b greater than or equal to a?", b >= a)
print("Is a not equal to b?", a != b)
print("Are both conditions true (a < b AND b > c)?", a < b and b > c)
print("Is at least one condition true (a > b OR a == c)?", a > b or a == c)
print("Is it NOT true that a equals b?", not (a == b))


word1 = input ("enter the first word : ")
word2 = input ("enter the second word : ")

print("Are the strings equal?", word1 == word2)
print("Are the strings equal (lowercase)?", word1.lower() == word2.lower())
print("Length of word1:", len(word1))




