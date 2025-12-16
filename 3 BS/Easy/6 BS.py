arr = [3, 4, 13, 13, 13, 20, 40]
x= 13
low =0
high = len(arr) - 1
ans = -1
while (low <= high):
    mid=(low+high)//2

    if arr[mid] == x:
        ans=mid
        low = mid+1
    else:
        high = mid -1

print(ans)