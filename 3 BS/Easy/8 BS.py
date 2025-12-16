arr = [4, 5, 6, 7, 0, 1, 2]
x = 2

def search(arr,x):
    low = 0
    high = len(arr) -1

    while (low<=high):
        mid = (low + high)//2 

        if arr[mid] == x:
            return mid
        
        if arr[low] < arr[mid]:
            if arr[low] <= x < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1

        else:
            if arr[mid] < x <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    
    return -1

print(search(arr,x))