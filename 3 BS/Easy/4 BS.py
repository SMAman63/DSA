arr  = [1,2,4,7]
x= 2

ans=len(arr)
low =0
high = len(arr)-1
while low <= high:
    mid = (low + high)//2
    
    if arr[mid] > x :
        ans = mid 
        high =mid - 1
    else:
        low = mid+1

print(ans)