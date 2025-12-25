s = "welcome to the jungle"

x = len(s)-1
arr=""
substr=""
while x>=-1:
    print(s[x])
    if s[x]==" " or x==-1:
        substr =substr[::-1]
        arr+= substr + " "
        substr=""
        x-=1
    else:
        substr+=s[x]
        x-=1
    
print(arr)


