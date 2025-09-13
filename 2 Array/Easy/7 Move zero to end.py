# remaining
arr = input("enter nos.")
arr=list(map(int,arr.split(",")))
print(arr)


def moveback(n,a):
    j=-1
    for i in range(n):
        if a[i]==0:
            j=i
            break

    if j==-1:
        return a
    for i in range(j+1,n):
        if a[i] != 0:
            a[i],a[j]=a[j],a[i]
            j+=1
        
    return a


n=len(arr)
x = moveback(n,arr)
print(x)