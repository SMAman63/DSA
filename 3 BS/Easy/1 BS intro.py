# Binary Search in using iterative way 

# target=6    
# arr = [3, 4, 6, 7, 9, 12, 16, 17]
# high = len(arr)-1
# low=0
# ans=-1
# while (low<=high):
#     mid=(high+low)//2
#     if arr[mid]==target:
#         ans=mid
#         break
#     elif arr[mid]<target:
#         low=mid+1
#     else:
#         high=mid-1
# print(ans)   
    

###########
#recursion


target=6    
arr = [3, 4, 6, 7, 9, 12, 16, 17]
high = len(arr)-1
low=0

def bs(arr,low,high,target):
    if low>high:
        return -1
    mid = (low + high)//2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return bs(arr,mid+1,high,target)
    return bs(arr,low,mid-1,target)


ans=bs(arr,low,high,target)
print(ans)