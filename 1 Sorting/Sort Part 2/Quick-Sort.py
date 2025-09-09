arr = [4,1,7,9,3]


def partition(arr,low,high):
    i=low
    j=high

    pivot=arr[low]
    while(i<j):
        
        while (arr[i]<=pivot and i<=high-1):
            i+=1

        while (arr[j]>pivot and j>=low+1):
            j-=1

        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    
    arr[j],arr[low]=arr[low],arr[j]

    return j


def qs(arr,low, high):
    if low<high:
        pindex=partition(arr,low,high)

        qs(arr,low,pindex-1)

        qs(arr,pindex+1,high)


qs(arr,0,len(arr)-1)

print(arr)