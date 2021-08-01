# Question: A company decides to give bonus to all its employees on Diwali. A 5% bonus on salary is given to the male workers 
# and 10% bonus on salary to female workers. Write a program to enter the salary of employee and sex of the employee.
# If salary of the employee is less than Rs. 10,000/- then the employee gets an extra 2% bonus on salary. 
# Calculate the bonus that has to be given to the employee and display the Salary.

print("Name= Nayan Ukande")
print("Roll No= 54")
print("Section= C")

a = input('Enter your name here: ')
b = int(input('your salary here: '))
c = input('your gender here (M/F) : ')
if b < 10000 and c == 'M':
    print(str(a) + ' your salary with bonus is ' + str(b*7/100+b))
elif b < 10000 and c == 'F':
    print(str(a) + ' your salary with bonus is ' + str(b*12/100+b))

if b >= 10000 and c == 'M':
    print(str(a) + ' your salary with  bonus is '+ str(b*5/100+b))

elif b >= 10000 and c=='F':
        print(str(a) + ' your salary with  bonus is '+ str(b*10/100+b))




