#create a file and provide a the name as README.txt
# try:
#     f=open("/home/udit/Desktop/fifth_sem/applied programming/applied_programming/class_assignment/README.txt","r")
#     for each in f:
#         print(each)
# finally:
#     f.close()

with open("/home/udit/Desktop/fifth_sem/applied programming/applied_programming/class_assignment/README.txt","w") as f:
    f.write("Hello World \n")
    f.write("Hello Sunway College \n")