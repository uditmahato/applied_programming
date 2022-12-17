def read(filename):
    f=open(filename,'r')
    for i in f:
        print(i)
        # if i[0]=='a':
        #     print("Yes there is a sentence starting with a in the following line ")
        # else:
        #     print("No there is no sentence starting with a")
            
read("uditBill.txt")   