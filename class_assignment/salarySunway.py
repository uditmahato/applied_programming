heading=("""
               Sunway College Account Department
                    Maitidevi ,Kathmandu
                      Welcome to
              Salary & Tax Calculate System(STCS)""")

def DisplayStaticInfo(heading):
    print(heading)

#creating list
staff_name=[]
staff_address=[]
staff_pan=[]
staff_status=[]
fy=[]
yearlyincome=[]
taxl=[]
slabl=[]
#defining function for collection staf information
def StaffInfo():
    StaffNo=int(input("Total no of Staff : "))
    for i in range(StaffNo):
        print(f"Enter for the {i+1} :")
        staff_name.append(input(f"\tEnter Staff Name [{i+1}]:"))
        staff_address.append(input(f"\tEnter Address [{i+1}]:"))
        staff_pan.append(input(f"\tEnter Pan No [{i+1}]:"))
        staff_status.append((input(f"\tEnter 'Y' for Married and 'N' for Unmarried Status [{i+1}]:")).upper())
        fy.append(input(f"\tEnter FY [{i+1}]:"))
        monthlyincome=int(input(f"\tEnter Staff per month income [Rs.][{i+1}]:"))
        yearlyincome.append(monthlyincome*12)
        print("\n")
#function to calculate tax
def Calculate_Tax_Of_Staff(staff_status,yearlyincome):
    def Calculate_Tax_Of_Staff_Married(yearlyincome):
        for i in range(len(yearlyincome)):
            tax=0
            if yearlyincome[i]<=400000:
                slabl.append("1%")
                tax=tax+yearlyincome[i]*0.01
            elif yearlyincome[i]<=500000:
                slabl.append("10%")
                tax=tax+(yearlyincome[i]-400000)*0.1
            elif yearlyincome[i]<=700000:
                slabl.append("20%")
                tax=tax+400000*0.01+100000*0.1+(yearlyincome[i]-500000)*0.2
            elif yearlyincome[i]<=1300000:
                slabl.append("30%")
                tax=tax+400000*0.01+100000*0.1+200000*0.2+(yearlyincome[i]-700000)*0.3
            else:
                slabl.append("36%")
                tax=tax+400000*0.01+100000*0.1+200000*0.2+600000*0.3+(yearlyincome[i]-1300000)*0.36
            taxl.append(tax)
           
    def Calculate_Tax_Of_Staff_Unmarried(yearlyincome):
        for i in (range(len(yearlyincome))):
            tax=0
            if yearlyincome[i]<=450000:
                slabl.append("1%")
                tax=tax+yearlyincome[i]*0.01
            elif yearlyincome[i]<=550000:
                slabl.append("10%")
                tax=tax+(yearlyincome[i]-450000)*0.1
            elif yearlyincome[i]<=750000:
                slabl.append("20%")
                tax=tax+450000*0.01+100000*0.1+(yearlyincome[i]-550000)*0.2
            elif yearlyincome[i]<=1300000:
                slabl.append("30%")
                tax=tax+450000*0.01+100000*0.1+200000*0.2+(yearlyincome[i]-700000)*0.3
            else:
                slabl.append("36%")
                tax=tax+450000*0.01+100000*0.1+200000*0.2+550000*0.3+(yearlyincome[i]-1300000)*0.36
            taxl.append(tax)

    for i in range(len(staff_status)):
        if staff_status[i]=='Y':
            Calculate_Tax_Of_Staff_Married(yearlyincome)
        else:
            Calculate_Tax_Of_Staff_Unmarried(yearlyincome)

def Display_Staff_Info(staff_name,staff_address,staff_pan,staff_status,slabl,taxl):
    for i in range(len(staff_name)):
        print(f"{heading}\n")
        print(f"Staff Name : {staff_name[i]}\t\t\t\tAddress:{staff_address[i]}")
        print(f"PAN No.: {staff_pan[i]}\t\tFY:{fy[i]}\t\tMarried Status:{staff_status[i]}\n")
        print(f"Staff {staff_name[i]} with PAN {staff_pan[i]} fall under {slabl[i]} Tax Slab.")
        print(f"{staff_name[i]} ({staff_pan[i]}) to pay tax to government is [Rs.]={taxl[i]}\n\n\n")

        #to write in file and txt file 
        f=open(f"bill/{staff_name[i]}.txt",'w')
        f.write(f"{heading}\n")
        f.write(f"Staff Name :{staff_name[i]}\t\t\t\tAddress:{staff_address[i]}\n")
        f.write(f"PAN No.: {staff_pan[i]}\t\tFY:{fy[i]}\t\tMarried Status:{staff_status[i]}\n\n")
        f.write(f"Staff {staff_name[i]} with PAN {staff_pan[i]} fall under {slabl[i]} Tax Slab.\n")
        f.write(f"{staff_name[i]} ({staff_pan[i]}) to pay tax to government is [Rs.]={taxl[i]}\n\n")
        f.close()

# main function to call all other function
def main():
    DisplayStaticInfo(heading)
    StaffInfo()
    Calculate_Tax_Of_Staff(staff_status,yearlyincome)
    Display_Staff_Info(staff_name,staff_address,staff_pan,staff_status,slabl,taxl)

main()
            