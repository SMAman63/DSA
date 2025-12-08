
arr=[3,5,8,15,19]
high = len(arr)-1
low = 0
target = 9
lower_bound=0
def bs(arr, low, high):
    print(low,high)
    if low>high:
        print("lw",high)
        return high 
    mid=(low+high)//2
    print(mid)
    if arr[mid]==target:
        print(low,high)
        lower_bound = mid
        return mid
    if target<arr[mid]:
        print(low,high)
        return bs(arr,low,mid-1)
    if target>arr[mid]:
        print(low,high)
        return bs(arr,mid+1,high)
    
x=bs(arr,low,high)

print(x)