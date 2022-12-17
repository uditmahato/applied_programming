#read data from a file and count the number, character,lowercase,uppercase,space,tab,lines
def read(filename):
    f=open(filename,'r')
    count=0
    count1=0
    count2=0
    count3=0
    count4=0
    count5=0
    count6=0
    count7=0
    for i in f:
        count+=1
        for j in i:
            count1+=1
            if j.islower():
                count2+=1
            elif j.isupper():
                count3+=1
            elif j.isspace():
                count4+=1
            elif j=='\t':
                count5+=1
            elif j=='\n':
                count6+=1
            elif j.isdigit():
                count7+=1    
    print(f"Number of lines in the file are {count}")
    print(f"Number of characters in the file are {count1}")
    print(f"Number of lowercase characters in the file are {count2}")
    print(f"Number of uppercase characters in the file are {count3}")
    print(f"Number of spaces in the file are {count4}")
    print(f"Number of tabs in the file are {count5}")

read("uditBill.txt")
