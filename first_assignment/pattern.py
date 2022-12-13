"""
Udit Kumar Mahato
Applied Programming Lab
IUKL ID: 0042003900006
"""
#take input from user
n=int(input("Enter the number of Rows:"))
#loop for printing the first half of the pattern
for i in range(n+1):
    for j in range(i+1):
        print("*",end=" ")
    print()
#loop for printing the second half of the pattern
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print()