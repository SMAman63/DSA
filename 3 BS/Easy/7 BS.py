arr = [3, 4, 13, 13, 13, 20, 40]
x= 1


def last_occurance(arr,x):
    low =0
    high = len(arr) - 1
    ans = -1

    while (low<=high):
        mid= (low+high)//2

        if arr[mid] <= x:
            ans=mid
            low = mid+1
        else:
            high = mid -1

    return ans

def first_occurance(arr,x):
    low =0
    high = len(arr) - 1
    ans = -1

    while (low<=high):
        mid= (low+high)//2

        if arr[mid] >= x:
            ans=mid
            high = mid -1
        else:
            low = mid+1

    return ans
    

first = first_occurance(arr,x)
last = last_occurance(arr,x)
print("first_occurance",first)
print("last_occurance",last)

print("count",last - first + 1)