arr = [1,1,2,2,2,3,3]
temp=[]
x=float("-inf")
for i in arr:
    if x != i:
        x=i
        temp.append(x)

print(len(temp))