# Search Single Element in a sorted array
# 1

# Problem Statement: Given an array of N integers. Every number in the array except one appears twice. Find the single number in the array.

# Examples
# Input : arr[] = {1,1,2,2,3,3,4,5,5,6,6}
# Output: 4
# Explanation: Only the number 4 appears once in the array.

# Input: arr[] = {1,1,3,5,5}
# Output : 3
# Explanation: Only the number 3 appears once in the array.

arr = [1,1,2,2,3,3,4,5,5,6,6]
# arr = [1,1,3,5,5]
# arr = [3,5,5]

low, high = 0, len(arr) - 1
n=0
def isEven(n):
    if n%2==0:
        return True
    return False

while low<=high:
    mid= (low+high)//2
    n=arr[mid]
    if arr[mid]!=arr[mid+1] and arr[mid]!=arr[mid-1]:
        n=arr[mid]
        break
    print(mid)
    if isEven(mid-low+1):
        print("mid",arr[mid],"mid+1",arr[mid+1],"mid-1",arr[mid-1])
        if arr[mid]==arr[mid-1]:
            low=mid+1
            print(low)
        else:
            print("in")
            high=mid-1
            print(high)
    else:
        print("mid",arr[mid],"mid+1",arr[mid+1],"mid-1",arr[mid-1])
        if arr[mid]==arr[mid+1]:
            low=mid+1
            print(low)        
        else:
            high = mid-1
            print(high)

print(n)