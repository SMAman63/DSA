# arr = [1,2,3,4,5,6,7,8,9]
arr = [9]

temp=arr[0]
i=0
while(i<len(arr)-1):
    arr[i]=arr[i+1]
    i+=1
arr[-1]=temp

print(arr)