

arr = [5,3,6,2,1]
n=len(arr)

def bubble(arr,n):
    if n==1:
        return
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
    bubble(arr,n-1)
    
print(arr)
bubble(arr,n)
print(arr)    