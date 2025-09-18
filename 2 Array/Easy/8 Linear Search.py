arr=[2,4,5,6,7,9,50,61,73,23,56,43,9]

findnum=577
x=-1
for i in range(len(arr)):
    if arr[i]==findnum:
       x=i
if x==-1:
    print("num not found",x)
else :
    print("num index",x)