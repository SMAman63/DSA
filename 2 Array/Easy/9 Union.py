arr1=[1,2,3,4,13]
arr2=[4,5,11,12,13,14]

i=0
j=0
temp=[]

while (i<len(arr1) and j<len(arr2)):
    if arr1[i]<=arr2[j]:
        if len(temp)==0 or temp[-1]!=arr1[i]:
            temp.append(arr1[i])
        i+=1
    else:
        if len(temp)==0 or temp[-1]!=arr2[j]:
            temp.append(arr2[j])
        j+=1

while j<len(arr2):
    if temp[-1]!=arr2[j]:
        temp.append(arr2[j])
    j+=1

while i<len(arr1):
    if temp[-1]!=arr1[i]:
        temp.append(arr1[i])
    i+=1

print(temp)