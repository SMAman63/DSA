

arr = [5,3,3,6,2,1,11,23]
n = len(arr)

def rec_insertion(arr,i,n):
    if i==n:
        return
    j = i
    while (j>0 and arr[j-1]>arr[j]):
        arr[j-1],arr[j]=arr[j],arr[j-1]
        j-=1
    
    rec_insertion(arr,i+1,n)

print(arr)
rec_insertion(arr,0,n)
print(arr)
