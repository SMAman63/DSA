arr = [1,2,3,4,5,6,7,8,9]
# arr = [9]
k=3
print("original",arr)
type="l"

# while(k>0):
#     # right
#     if type=="r":
#         temp=arr[0]
#         i=0
#         while(i<len(arr)-1):
#             arr[i]=arr[i+1]
#             i+=1
#         arr[-1]=temp

#         print(arr)
#         k-=1
#     # left
#     if type == "l":
#         temp=arr[-1]
#         i=len(arr)-1
#         while(0<i):
#             arr[i]=arr[i-1]
#             i-=1
#         arr[0]=temp

#         print(arr)
#         k-=1
        

### Reverse Algo

# For Rotating Elements to right
# Step 1: Reverse the last k elements of the array

# Step 2: Reverse the first n-k elements of the array.

# Step 3: Reverse the whole array.

# For Rotating Elements to left
# Step 1: Reverse the first k elements of the array

# Step 2: Reverse the last n-k elements of the array.

# Step 3: Reverse the whole array.




#  rotate right
def reverse(arr,i,j):
    while(i<=j):
        arr[j],arr[i]=arr[i],arr[j]
        i+=1
        j-=1


def rotate(arr,n,k):
    reverse(arr,0,n-k-1)
    reverse(arr,n-k,n-1)
    reverse(arr,0,n-1)

rotate(arr,len(arr),k)
print(arr)
