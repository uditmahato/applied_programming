
CustomerName=input("Enter the name of the customer: ")
CustomerAddress=input("Enter the address of the customer: ")
CustomerUnit=int(input("Enter the unit of the customer: "))

DiscountAmount= 0
CustomerTotalBill=0

if CustomerUnit<=20:
    CustomerTotalBill=CustomerUnit*4
elif CustomerUnit<=50:
    CustomerTotalBill=20*4+ (CustomerUnit-20)*7.3
elif CustomerUnit<=150:
    CustomerTotalBill=20*4+30*7.3+(CustomerUnit-20-50)*8.6
    DiscountAmount=DiscountAmount+(CustomerUnit-20-50)*0.05

elif CustomerUnit<=250:
    CustomerTotalBill=20*4+30*7.3+80*8.6+(CustomerUnit-20-30-80)*9.5
    DiscountAmount=DiscountAmount+(CustomerUnit-20-30-80)*0.1
else:
    CustomerTotalBill=0*4+30*7.3+80*8.6+100*9.5+(CustomerUnit-20-30-80-100)*11.0
    DiscountAmount=DiscountAmount+(CustomerUnit-20-30-80-100)*0.15

CustomerTotalBill=CustomerTotalBill-DiscountAmount
print("*******************************************")
print("""Sunway Electricity Bill""")
print("""Maitidevi Kathmandu Nepal""")
print("________________________________")

print("Name of the customer: ",CustomerName,"        ","Address: ",CustomerAddress)
print("Total Consumed unit: ",CustomerUnit)
print("Total Bill: ",CustomerTotalBill)
print("Discount Amount: ",DiscountAmount)

print("Costumer Name " ,CustomerName," has consumed ",CustomerUnit,
" units of electricity and his billing amount is ",CustomerTotalBill ," after getting discount of ",DiscountAmount)