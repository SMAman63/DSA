
def merge(low,mid,high,arr):
    temp=[]
    left=low
    right=mid+1

    while(left<=mid and right<=high):
        if arr[left]<arr[right]:
            temp.append(arr[left])
            left+=1
        else: 
            temp.append(arr[right])
            right+=1
    while (left<=mid):
        temp.append(arr[left])
        left+=1
    while (right<=high):
        temp.append(arr[right])
        right+=1
    
    for i in range(len(temp)):
        arr[low+i]=temp[i]
        

def ms(arr,low,high):
    if low>=high:
        return;
    mid=(low+high)//2

    ms(arr,low,mid)
    ms(arr,mid+1,high)

    merge(low,mid,high,arr)

def mergeSort(arr,n):
    ms(arr,0,n-1)

arr=[3,6,8,9,4,2,1,7]
n=len(arr)
mergeSort(arr,n)
print(arr)
