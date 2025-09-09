arr=[2,6,8,8,4,5,0,0,12,6,55,88]

lar=arr[0]
slar=arr[0]

for i in range(len(arr)):
    if arr[i]>lar:
        lar=arr[i]
        slar=lar
    
print(lar)
