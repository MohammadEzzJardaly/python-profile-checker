name = input("Enter your full name: ")
age = int(input("Enter your age: "))
gpa = float(input("Enter your GPA (0.0 - 5.0): "))
field = input("Enter your field of interest: ")
graduated = input("Have you graduated")

print("Name:", name)
print("Age:", age)
print("GPA:", gpa)
print("Field of Interest:", field)
print("Graduated:", "Yes" if graduated == "yes" else "No")


print("\n")

if age < 25 and gpa >= 3.5 and graduated == "yes":
    print("You are eligible for Scholarship")
elif age < 30 and gpa >= 2.5:
    print("You are eligible for Internship")
else:
    print("Apply again later")

