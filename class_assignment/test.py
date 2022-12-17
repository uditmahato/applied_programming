#continue statement
# name=["m","b","c","d","e"]
# for i in name:
#     print(i)
#     if i=="c":
#         continue

list=[]
sublist=[]
n=int(input("enter the number of students: "))
for i in range(n):
    list.append([])
    for j in range(2):
        list[i].append([input("enter subject name: "),int(input("enter subject mark: "))])



print(list)