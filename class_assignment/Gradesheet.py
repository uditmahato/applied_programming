InitialDisplay="""Sunway International Business School"""
#student details
name=input("Enter the name of the student: ")
address=input("Enter the address of the student: ")
programme=input("Enter the programme of the student: ")
faculty=input("Enter the faculty of the student: ")
intake=input("Enter the intake of the student: ")

#subject details and marks

subject1,subject2,subject3,subject4,subject5=input("Enter the name of the subjects: ").split()
# marks1,marks2,marks3,marks4,marks5=int,input().split()

marks2=int(input("Enter the marks of the subject2: "))
marks1=int(input("Enter the marks of the subject1: "))
marks3=int(input("Enter the marks of the subject3: "))
marks4=int(input("Enter the marks of the subject4: "))
marks5=int(input("Enter the marks of the subject5: "))


#total marks


total=marks1+marks2+marks3+marks4+marks5

#percentage

percentage=(total/500)*100

#grade classification

if percentage>=90:
    grade="A+"
elif percentage>=80:
    grade="A"
elif percentage>=70:
    grade="B+"
elif percentage>=60:
    grade="B"
elif percentage>=50:
    grade="B-"
elif percentage>=40:
    grade="C+"
elif percentage>=30:
    grade="D"
else:
    grade="F"
print("*******************************************")
print(InitialDisplay)
print(" Maitidevi Kathmandu Nepal ")

print("Name of the student: ",name,"        ","Address: ",address)
print("Faculty of the student: ",faculty,"      ","Program: ",programme)
print("Intake of the student: ",intake)
print("")
print("Course Name","       ","Marks")
print(subject1,"          ",marks1)
print(subject2 ,"         ",marks2)
print(subject3,"          ",marks3)
print(subject4,"          ",marks4)
print(subject5,"          ",marks5)

print("")
print("Final Grade: ",grade)




