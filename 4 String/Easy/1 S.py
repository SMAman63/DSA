s = "()(()())(())"
f=0
l=""
for i in range(len(s)):
    print(s[i])
    if s[i]=='(':
        if f>0:
            l+=s[i]
        f+=1    
    elif s[i]==')':
        f-=1
        if f>0:
            l+=s[i]
print(l)