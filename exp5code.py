#Question: Write a Python function to calculate result of students 
#by accepting marks of all subjects by using variables arguments.

print("Name= Nayan Ukande")
print("Roll No= 54")
print("Section= C")

def result(roll_no, name, *args):
    print("Roll No", roll_no)
    print("Enter your name", name)
    z=1
    for marks in args:
        z += marks
    z=z/5
    print(z,"%")
roll_no=int(input("Enter your roll number: "))
name=input("Enter your name: ")
sub1=int(input('Enter the marks of subject1: '))
sub2=int(input('Enter the marks of subject2: '))
sub3=int(input('Enter the marks of subject3: '))
sub4=int(input('Enter the marks of subject4: '))
sub5=int(input('Enter the marks of subject5: '))

result(roll_no, name, sub1,sub2,sub3,sub4,sub5)