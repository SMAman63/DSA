
count = 0
def pri(n):
    if count>n:
        return
    pri(n-1)
    print(n)
    


n=int(input("enter no of prodcuts"))
pri(n)