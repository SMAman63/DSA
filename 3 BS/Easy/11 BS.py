# arr = [4,5,6,7,0,1,2,3]
arr = [3,4,5,1,2]

def mina(arr):
    low, high = 0, len(arr)-1
    while low < high:
        mid = (low + high)//2

        if arr[mid] <= arr[high]:
            high = mid

        else:
            low = mid+1

    return low

print(mina(arr))