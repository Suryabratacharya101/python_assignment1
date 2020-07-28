# assignment 1
# Task 1
lst = []
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        lst.append(i)

print(lst)

# task 2
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print('The reverse of your name is ' + last_name[::-1] + "\t" + first_name[::-1])

# task 3
diameter = input("Enter the diameter of the sphere: ")
volume = 4.0/3.0*3.14159265359*(float(diameter)/2)**3
print("the Volume of the sphere is: " + str(volume))