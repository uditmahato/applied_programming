import datetime
# Description: This program is used to calculate the discount and net amount of the customer

#creating empty list to store values
namel=[]
addressl=[]
emaill=[]
itempricel=[]
itemnamel=[]
itemqtyl=[]
totall=[]
netTotall=[]
discl=[]



#variable for displaying information
heading="""
                     Sunway College BhatBhateni 
                        Maitidevi,Kathmandu 
                         Phone: 01-4444444"""
heading2="\n\t\t\tCustomer Billing System\n"
heading3="=======================================================================\n"
heading5="_______________________________________________________________________\n"
date=datetime.date.today()
#function for displaying the information
def initialDisplay(heading,heading2,heading3,date,heading5):
    print("")
    print(heading3)
    print("{:>30}".format(heading))
    print("{:>30}".format(heading2))
    print("")
    print("{:>60}Billing Date:{:}".format("",date))
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
            itemname=input(f"Enter the name of item [{j+1}]: ")
            itemprice=int(input(f"Enter the price of item [{j+1}]: "))
            itemqty=int(input(f"Enter the quantity of item [{j+1}]: "))
            print("\n")
            totalPrice=totalPrice+itemprice*itemqty
            totall.append(totalPrice)
            itempricel.append(itemprice)
            itemqtyl.append(itemqty)
            itemnamel.append(itemname)
            calculation(totall)
        print("")
    #for condion to either print and create bill or only print or only create bill
    print("=======================================================")
    Action=int(input("Enter 1 to print the bill: \nEnter 2 to Create the bill in text file: \nEnter 3 to both print and create bill : "))
    if Action==1:
        displayInformation(namel,addressl,emaill,itemnamel,itempricel,itemqtyl,totall,discl,netTotall,heading,heading2,heading3,date,heading5)
    elif Action==2:
        writeInformation(namel,addressl,emaill,itemnamel,itempricel,itemqtyl,totall,discl,netTotall,heading,heading2,heading3,date,heading5)
    elif Action==3:
        displayInformation(namel,addressl,emaill,itemnamel,itempricel,itemqtyl,totall,discl,netTotall,heading,heading2,heading3,date,heading5)
        writeInformation(namel,addressl,emaill,itemnamel,itempricel,itemqtyl,totall,discl,netTotall,heading,heading2,heading3,date,heading5)
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
def writeInformation(namel,addressl,emaill,itemnamel,itempricel,itemqtyl,totall,discl,netTotall,heading,heading2,heading3,date,heading5):
    for j in range(len(namel)):
        fileName=namel[j]+"Bill.txt"
        f=open(fileName,"w")
        for i in range(1):
            f.write(heading3)
            f.write(heading)
            f.write(heading2)
            f.write("")
            f.write("{:>60}Billing date:{:} \n".format("",date))
            f.write("")
            f.write(f"Customer Name: {namel[j]}\n")
            f.write(f"Customer Address: {addressl[j]}\n")
            f.write(f"Customer Email: {emaill[j]}\n")
            f.write(f"\t{heading5}")
            f.write("\n")
            f.write(f"Item Nam\tItem Price\tItem Quantity\tTotal Price\n\n")
            for k in range(len(itemnamel)):
                f.write(f"{itemnamel[k]}\t\t{itempricel[k]}\t\t\t{itemqtyl[k]}\t\t\t{totall[k]}\n")
            f.write(heading5)
            f.write(f"\t\t\t\t\t\tTotal Price: {totall[j]}\n")
            f.write(f"\t\t\t\t\t\tDiscount: {discl[j]}\n")
            f.write(f"\t\t\t\t\t\tNet Amount: {netTotall[j]}\n")
            print("\n\n")
            f.write("\t\t\tThank you for purchasing from us\n\n")
            f.write(heading3)
        f.close()

#function for displaying the information
def displayInformation(namel,addressl,emaill,itemnamel,itempricel,itemqtyl,totall,discl,netTotall,heading,heading2,heading3,date,heading5):
    for i in range(len(namel)):
        initialDisplay(heading,heading2,heading3,date,heading5)
        print(f"Customer Name: {namel[i]}")
        print(f"Customer Address: {addressl[i]}")
        print(f"Customer Email: {emaill[i]}")
        print(heading5)
        print(f"Item Nam\tItem Price\tItem Quantity\tTotal Price\n")
        for j in range(len(itemqtyl)):
            print(f"{itemnamel[j]}\t\t{itempricel[j]}\t\t{itemqtyl[j]}\t\t{totall[j]}")
        print(heading5)
        print(f"\t\t\t\tTotal Price: {totall[i]}")
        print(f"\t\t\t\tDiscount: {discl[i]}")
        print(f"\t\t\t\tNet Amount: {netTotall[i]}")
        print("\n")
        print("\t\tThank you for purchasing from us\n")
        print(heading3)

#function call
initialDisplay(heading,heading2,heading3,date,heading5)
initialInformation()