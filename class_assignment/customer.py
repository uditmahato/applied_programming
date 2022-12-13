import time
# Description: This program is used to calculate the discount and net amount of the customer
# Function to display heading
namel=[]
addressl=[]
emaill=[]
itempricel=[]
itemqtyl=[]
totall=[]
netTotall=[]
discl=[]
#variable for displaying information
heading="Sunway College BhatBhateni \nMaitidevi,Kathmandu \nPhone: 01-4444444"
heading2="Customer Billing System"
heading3="===================================="
d="Date: ", time.strftime("%d/%m/%Y")
date=str(d)

#function for displaying the information
def initialDisplay(heading,heading2,heading3,date):
    print(heading3)
    print(heading)
    print(heading2)
    print(heading3)
    print(date)
    print(heading3)
    
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
    #forbiling purpose
    print("=======================================================")
    Action=int(input("Enter 1 to print the bill: \nEnter 2 to Create the bill in text file: \nEnter 3 to both print and create bill : "))
    if Action==1:
        displayInformation(namel,addressl,emaill,totall,discl,netTotall)
    elif Action==2:
        writeInformation(namel,addressl,emaill,totall,discl,netTotall,heading,heading2,heading3,date)
    elif Action==3:
        displayInformation(namel,addressl,emaill,totall,discl,netTotall)
        writeInformation(namel,addressl,emaill,totall,discl,netTotall,heading,heading2,heading3,date)
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
def writeInformation(namel,addressl,emaill,totall,discl,netTotall,heading,heading2,heading3,date):
    for j in range(len(namel)):
        fileName=namel[j]+".txt"
        f=open(fileName,"w")
        for i in range(len(namel)):
            f.write("====================================")
            f.write(heading)
            f.write(heading2)
            f.write(heading3)
            f.write(date)
            f.write(heading3)
            f.write(f"Customer Name: {namel[i]}")
            f.write(f"Customer Address: {addressl[i]}")
            f.write(f"Customer Email: {emaill[i]}")
            f.write(f"Total Price: {totall[i]}")
            f.write(f"Discount: {discl[i]}")
            f.write(f"Net Amount: {netTotall[i]}")
            f.write("====================================")
        f.close()

def displayInformation(namel,addressl,emaill,totall,discl,netTotall):
    for i in range(len(discl)):
        print("====================================")
        initialDisplay(heading,heading2,heading3,date)
        print(f"Customer Name: {namel[i]}")
        print(f"Customer Address: {addressl[i]}")
        print(f"Customer Email: {emaill[i]}")
        print(f"Total Price: {totall[i]}")
        print(f"Discount: {discl[i]}")
        print(f"Net Amount: {netTotall[i]}")
        print("====================================")

#funrion call
initialDisplay(heading,heading2,heading3,date)
initialInformation()
