# Student Marks Analyzer

# Description:
# This program takes student marks as input, calculates the total marks, percentage, and assigns a grade based on the percentage.

m1=int(input("Enter the marks of Subject 1 : "))
m2=int(input("Enter the marks of Subject 2 : "))
m3=int(input("Enter the marks of Subject 3 : "))
m4=int(input("Enter the marks of Subject 4 : "))
m5=int(input("Enter the marks of Subject 5 : "))
print("\n")
print("Student Marks Analysis")
totalMarks=m1+m2+m3+m4+m5
print(f"Total Marks : {totalMarks}")
percentage=(totalMarks/500)*100
print(f"Percentage : {percentage}")
if(90<=percentage<=100):
    print("Grade A")
elif(80<=percentage<90):
    print("Grade B")
elif(70<=percentage<80):
    print("Grade C")
elif(60<=percentage<70):
    print("Grade D")
elif(50<=percentage<60):
    print("Grade E")
else:
    print("Fail")


