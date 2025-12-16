arr = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6]

x = 10


def search(arr,x):
    low = 0 
    high = len(arr)-1

    while (low<=high):
        mid = (low+high)//2

        if arr[mid] == x:
            return True
        
        if arr[low] == arr[mid] == arr[high]:
            low+=1
            high-=1
            continue
        
        if arr[low] < arr[mid]:
            if arr[low] <= x <arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid]< x <= arr[high]:
                low=mid+1
            else :
                high = mid -1
        
    return False

print(search(arr,x))