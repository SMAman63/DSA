# arr=[2,6,8,4,5,0,12,6,55]
arr=[2,4,5,7,8,9,13,5,46,77,90]

sorted=True
for i in range(len(arr)-1):
    if arr[i]>arr[i+1]:
        sorted=False

print("sorted",sorted)