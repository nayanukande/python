# Exp. 8:- Write a program to demonstrate the File Handling Mechanism in Python with below mentioned guidelines.
# To copy contents of one file to other. While copying
# a) All full stops are to be replaced with commas
# b) Lower case are to be replaced with upper case
# c) Upper case are to be replaced with lower case.
# Note: create a file named as input.txt and write some contents in it and save it.

print("Name = Nayan Ukande")
print("Roll No / Sec = 54/C-3 ")

txt_file_1 = open("input.txt", 'r')
txt_file_2 = open("output.txt", 'w')

for poem in txt_file_1 :
    poem = poem.replace(".",",")
    poem = poem.swapcase()

    txt_file_2.write(poem)