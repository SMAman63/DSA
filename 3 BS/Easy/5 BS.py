arr  = [3,4,4,7,8,10]
x= 8
def ceil(arr,x):
    ans = -1
    low =0
    high = len(arr)-1

    while(low <= high ):
        mid= (low+high)//2
        if arr[mid] >= x:
            ans=mid
            high = mid - 1
        else :
            low = mid + 1

    return ans

def floor(arr,x):
    ans = -1
    low =0
    high = len(arr)-1

    while(low <= high ):
        mid= (low+high)//2
        if arr[mid] <= x:
            ans=mid
            low = mid + 1
        else :
            high = mid - 1

    return ans

def find(arr,x):
    f = floor(arr,x)
    c = ceil(arr,x)

    return f,c
fl,ce = find(arr,x)
print("floor",arr[fl])
print("floor index",fl)
print("ceil",arr[ce])
print("ceil index",ce)

