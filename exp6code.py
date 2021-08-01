# Question: Write a program that creates a list of 10 random integers. 
# Then create two Lists: - Odd List and Even List that has all odd and even values in the list.

import random

name=input("Enter your name: ")
roll_no=input("Enter your roll number: ")
section=input("Enter your section: ")

numbers=[]
for i in range(0, 10):
    rn = random.randint(1, 40)
    numbers.append(rn)

el=[]
ol=[]

for i in range(1, 10):
    if numbers[i] % 2 == 0:
        el.append(numbers[i])
    else:
        ol.append(numbers[i])

print("The program is performed by: ", name)
print("Roll No/Section: ", roll_no,"-", section)
print("Generated random list is: ", numbers)     
print("The Even numbers list is: ", el)
print("The Odd numbers list is: ", ol)
