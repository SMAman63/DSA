arr = [1,2,4,5]
count=1
missing=0
for i in range(len(arr)):
    if arr[i]!=count:
        missing=count
        break
    count+=1

print(missing)

# approach 2
n=len(arr)+1
sum1 = (n*(n+1))//2
sum2 = sum(arr)

print(sum1-sum2)