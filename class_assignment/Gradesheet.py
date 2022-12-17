InitialDisplay="""
            Sunway International Business School
                Maitidevi Kathmandu Nepal"""
#create empty list 
namel=[]
addressl=[]
programmel=[]
facultyl=[]
intakel=[]
percentagel=[]
Finalgradel=[]

subjectmarks=[]

def studentdetails():
    print(InitialDisplay)
    n=int(input("Enter the number of students: "))
    for i in range(n):
        namel.append(input(f"Enter the name of the student [{i+1}]: "))
        addressl.append(input(f"Enter the address of the student [{i+1}]: "))
        programmel.append(input(f"Enter the programme of the student [{i+1}]: "))
        facultyl.append(input(f"Enter the faculty of the student [{i+1}]: "))
        intakel.append(input(f"Enter the intake of the student [{i+1}]: "))
        subjectmarks.append([])
        for j in range(5):
            subjectmarks[i].append([input(f"Enter name of course[{j+1}] : "),int(input(f"Enter the marks of course[{j+1}] : "))])

def gradecalculation(subjectmarks):
    for i in range(len(subjectmarks)):
        total=0
        for j in range(5):
            total=total+subjectmarks[i][j][1]
            percentage=(total/500)*100
        percentagel.append(percentage)
        if percentage>=90:
            Finalgradel.append("A+")
        elif percentage>=80:
            Finalgradel.append("A")
        elif percentage>=70:
            Finalgradel.append("B+")
        elif percentage>=60:
            Finalgradel.append("B")
        elif percentage>=50:
            Finalgradel.append("B-")
        elif percentage>=40:
            Finalgradel.append("C+")
        elif percentage>=30:
            Finalgradel.append("C")
        else:
            Finalgradel.append("F")

def displayInformation(namel,addressl,programmel,facultyl,intakel,subjectmarks,percentagel,Finalgradel,InitialDisplay):
    for i in range(len(namel)):
        print("\n")
        print(InitialDisplay)
        print("\n\n")
        print(f"Name of the student: {namel[i]}\t\t Address: {addressl[i]}")
        print(f"Programme of the student: {programmel[i]}\t\t Faculty: {facultyl[i]}")
        print(f"Intake of the student: {intakel[i]}\n\n")
        print("\t\t\tGrade Sheet\n")
        print(f"Course Name\t\t\t\tMarks\n")
        for j in range(5):
            print(f"{subjectmarks[i][j][0]}\t\t\t{subjectmarks[i][j][1]}")
        print("\n")
        print("Final Grade: ",Finalgradel[i])
        print("Percentage: ",percentagel[i])

def main():
    studentdetails()
    gradecalculation(subjectmarks)
    displayInformation(namel,addressl,programmel,facultyl,intakel,subjectmarks,percentagel,Finalgradel,InitialDisplay)

main()



