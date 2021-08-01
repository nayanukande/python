# Question: Write a python program that demonstrates the use of dictionary to 
# display doctor profile information.

print("Nayan Ukande")
print("Roll No/Section: 54/C")

doctordetails={}
lists=["Name", "DOB", "Specialists", "Hospital Name", "Contact Number", "Address"]

for i in range(len(lists)):
    print(lists[i])
    k=lists[i]
    v=input("Enter:")
    doctordetails[k]=v

print(doctordetails)
