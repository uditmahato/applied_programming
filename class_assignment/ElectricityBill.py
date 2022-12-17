
Heading="""
              Sunway Electricity Bill
                Maitidevi, Kathmandu
"""
customerName=[]
customerName=[]
customerAddress=[]
customerUnit=[]
Discount=[]
TotalBill=[]

def customerInformation():
    n=int(input("Enter the number of customers: "))
    for i in range(n):
        customerName.append(input(f"Enter the name of customer [{i+1}]: "))
        customerAddress.append(input(f"Enter the address of customer [{i+1}]: "))
        customerUnit.append(int(input(f"Enter the unit of customer [{i+1}]: ")))

def calculation(customerUnit):
    for i in range(len(customerUnit)):
        DiscountAmount= 0
        CustomerTotalBill=0
        if customerUnit[i]<=20:
            CustomerTotalBill=customerUnit[i]*4
        elif customerUnit[i]<=50:
            CustomerTotalBill=20*4+ (customerUnit[i]-20)*7.3
        elif customerUnit[i]<=150:
            CustomerTotalBill=20*4+30*7.3+(customerUnit[i]-20-50)*8.6
            DiscountAmount=DiscountAmount+(customerUnit[i]-20-50)*0.05

        elif customerUnit[i]<=250:
            CustomerTotalBill=20*4+30*7.3+80*8.6+(customerUnit[i]-20-30-80)*9.5
            DiscountAmount=DiscountAmount+(customerUnit[i]-20-30-80)*0.1
        else:
            CustomerTotalBill=0*4+30*7.3+80*8.6+100*9.5+(customerUnit[i]-20-30-80-100)*11.0
            DiscountAmount=DiscountAmount+(customerUnit[i]-20-30-80-100)*0.15
        Discount.append(DiscountAmount)
        CustomerTotalBill=CustomerTotalBill-DiscountAmount
        TotalBill.append(CustomerTotalBill)

def displayInformation(Heading,customerName,customerAddress,customerUnit,TotalBill,Discount):
    for i in range(len(customerName)):
        print("************************************************")
        print(Heading)
        print("_____________________________________________________________________\n")
        print(f"Customer Name: {customerName[i]}\t\tCustomer Address: {customerAddress[i]}")
        print(f"CUstomer Unit:{customerUnit[i]}\n")
        print(f"Total Bill:{TotalBill[i]}")
        print(f"Discount Amount: {Discount[i]}\n\n")
        print("Costumer" ,customerName[i]," has consumed ",customerUnit[i],
        " units of electricity and his billing amount is ",TotalBill[i] ,
        " after getting discount of ",Discount[i])
        print("*"*60)

customerInformation()
calculation(customerUnit)
displayInformation(Heading,customerName,customerAddress,customerUnit,TotalBill,Discount)


