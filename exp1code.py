# question: To accept the object of mass in kg and velocity in meter per second
# and display it momentum. Momentum is calculated as E=MC^2 when M is mass and 
# C is Velocity.
print("Name = Nayan Ukande\n Roll No = 54\n Section = C3\n")

mass=int(input("Enter the mass of the object:"))
vel=float(input("Enter the velocity of the Object:"))
momentum= mass * vel
energy= mass*vel*vel
print("the momentum of object is = %f kilogram meter per second" %momentum)
print("The energy of the object = %f joules" %energy)
print("hey guys we added this new line")