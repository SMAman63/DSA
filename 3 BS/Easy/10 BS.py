arr = [4,5,6,0,1,2,3]
# def search_min(arr):
#     low, high = 0, len(arr)-1
#     mid = (low+high)//2
#     min = arr[mid]

#     while low < high:
#         mid = (low + high)//2
#         print("low",low,'high',high )
#         print(min)

#         if arr[low] < arr[mid]:
#             if arr[low]<min:
#                 min = arr[low]
#                 low=mid+1
#         else:
#             if arr[mid]<min:
#                 min = arr[mid]
#                 high = mid-1

        
#     return min

def search_min(arr):
    low, high = 0, len(arr) - 1

    while low < high:
        mid = (low + high) // 2
        print("low", low, 'high', high)

        if arr[mid] > arr[high]:
            low = mid + 1
        else:
            high = mid
    return arr[low]

print(search_min(arr))