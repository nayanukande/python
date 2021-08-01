# Write a python program that accepts a string from user and perform following string operations.
# 1. Calculate length of string
# 2. String reversal
# 3. Equality check of two strings
# 4. Check palindrome

x=input("Enter any string: ")
y=input("Enter any string: ")
print("The lenth of string = %f" %len(x))
print("The reverse of Nayan is: ")
print(x[::-1])
if(x==y):
    print("Strings are equal")
else:
    print("Strings are not equal")
if(x==y[::-1]):  
      print("The letter is a palindrome")  
else:  
      print("The letter is not a palindrome")