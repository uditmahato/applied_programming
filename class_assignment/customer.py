from datetime import datetime as time
# Description: This program is used to calculate the discount and net amount of the customer

#creating empty list to store values
namel=[]
addressl=[]
emaill=[]
itempricel=[]
itemqtyl=[]
totall=[]
netTotall=[]
discl=[]

#variable for displaying information
heading="""Sunway College BhatBhateni 
Maitidevi,Kathmandu 
Phone: 01-4444444"""
heading2="\nCustomer Billing System\n"
heading3="=================================================================\n"
heading5="__________________________________________________________________\n"
d=time.now()
date=d.strftime("%d/%m/%Y %H:%M:%S")

#function for displaying the information
def initialDisplay(heading,heading2,heading3,date,heading5):
    print("")
    print(heading3)
    print("{:>30}".format(heading))
    print("{:>30}".format(heading2))
    print("")
    print("{:>30}Purchase d/t:{:}".format("",date))
    print("")
    
#fuction for input and information
def initialInformation():
    n=int(input("Enter the number of customers: "))
    #first for loop for different customers
    for i in range(n):
        #input for details
        namel.append(input(f"Enter the name of customer [{i+1}]: "))
        addressl.append(input(f"Enter the address of customer [{i+1}]: "))
        emaill.append(input(f"Enter the email of customer [{i+1}]: "))
        itemno=int(input(f"Enter the number of items of customer : "))
        for j in range(itemno):
            totalPrice=0
            itemprice=int(input(f"Enter the price of item [{j+1}]: "))
            itemqty=int(input(f"Enter the quantity of item [{j+1}]: "))
            totalPrice=totalPrice+itemprice*itemqty
            totall.append(totalPrice)
            calculation(totall)
        print("")
    #for condion to either print and create bill or only print or only create bill
    print("=======================================================")
    Action=int(input("Enter 1 to print the bill: \nEnter 2 to Create the bill in text file: \nEnter 3 to both print and create bill : "))
    if Action==1:
        displayInformation(namel,addressl,emaill,totall,discl,netTotall,heading,heading2,heading3,date,heading5)
    elif Action==2:
        writeInformation(namel,addressl,emaill,totall,discl,netTotall,heading,heading2,heading3,date,heading5)
    elif Action==3:
        displayInformation(namel,addressl,emaill,totall,discl,netTotall,heading,heading2,heading3,date,heading5)
        writeInformation(namel,addressl,emaill,totall,discl,netTotall,heading,heading2,heading3,date,heading5)
    else:
        print("Invalid Input")

#function for calculation of discount and Net amount
def calculation(totall):
    for i in range(len(totall)):
        totalPrice=totall[i]
    #discount calculation   
        discount=0
        if totalPrice<=5000:
            discount = totalPrice*0.05
        elif totalPrice<=7000:
            discount=(5000*0.05)+(totalPrice-5000)*0.08
        elif totalPrice<=10000:
            discount=(5000*0.05)+(2000*0.08)+(totalPrice-7000)*0.10
        else:
            discount=(5000*0.05)+(2000*0.08)+(3000*0.10)+(totalPrice-10000)*0.15
        # net amount after discount
        netAmount=totalPrice-discount
        netTotall.append(netAmount)
        discl.append(discount)
        return netAmount,discount

#function for writing the information in text file
def writeInformation(namel,addressl,emaill,totall,discl,netTotall,heading,heading2,heading3,date,heading5):
    for j in range(len(namel)):
        fileName=namel[j]+".txt"
        f=open(fileName,"w")
        for i in range(1):
            f.write(heading3)
            f.write(heading)
            f.write(heading2)
            f.write("")
            f.write("{:>30}Purchase d/t:{:} \n".format("",date))
            f.write("")
            f.write(f"Customer Name: {namel[j]}\n")
            f.write(f"Customer Address: {addressl[j]}\n")
            f.write(f"Customer Email: {emaill[j]}\n")
            f.write(heading5)
            f.write("")
            f.write(f"Total Price: {totall[j]}\n")
            f.write(f"Discount: {discl[j]}\n")
            f.write(f"Net Amount: {netTotall[j]}\n")
            print("")
            f.write("Thank you for purchasing from us")
            f.write(heading3)
        f.close()

#function for displaying the information
def displayInformation(namel,addressl,emaill,totall,discl,netTotall,heading,heading2,heading3,date,heading5):
    for i in range(len(namel)):
        initialDisplay(heading,heading2,heading3,date,heading5)
        print(f"Customer Name: {namel[i]}")
        print(f"Customer Address: {addressl[i]}")
        print(f"Customer Email: {emaill[i]}")
        print(heading5)
        print("")
        print(f"Total Price: {totall[i]}")
        print(f"Discount: {discl[i]}")
        print(f"Net Amount: {netTotall[i]}")
        print("")
        print("Thank you for purchasing from us")
        print(heading3)

#function call
initialDisplay(heading,heading2,heading3,date,heading5)
initialInformation()