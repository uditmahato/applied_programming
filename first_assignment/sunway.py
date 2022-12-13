"""
Udit Kumar Mahato
Applied Programming
IUKL ID: 0042003900006
"""

def count_chars(str):
    print("")
    print('''WELCOME TO SUNWAY CHARACTER CHECK SYSTEM 
            MAITIDEVI, KATHMANDU''')
    print("")
    #counter of the characters
    uppercase_counter=0
    lowercase_counter=0 
    number_counter=0
    specialchar_counter =0
    #creating options for the user
    print('Enter the 1 for count uppercase character \nEnter the 2 for countlowercase character \nEnter the 3 for count number character \nEnter the 4 for count special character')
    input_number=int(input("Enter the number:"))
    if input_number==1:
        for i in str:
            if i.isupper():
                uppercase_counter+=1
        print("The number of uppercase character is:",uppercase_counter)
    elif input_number==2:
        for i in str:
            if i.islower():
                lowercase_counter+=1
        print("The number of lowercase character is:",lowercase_counter)
    elif input_number==3:
        for i in str:
            if i.isdigit():
                number_counter+=1
        print("The number of number character is:",number_counter)
    elif input_number==4:
        for i in str:
            if i.isalnum():
                specialchar_counter+=1
        print("The number of special character is:",specialchar_counter)
    elif input_number==5:
        print("Thank you for the visit")
    else:
        print("Invalid input")

#calling the function to take user input   
count_chars(input("Enter a string: "))