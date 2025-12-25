
s = "5347"
x=0
largest_odd=0
last_ind=0
for i in range (len(s)-1, -1,-1):
    if int(s[i])%2!=0:
        print("llll",last_ind)
        last_ind=i
        break
first_ind=0
while x<=len(s):
    if s[x]==0:
        first_ind+=1
    else:
        break
    x+=1
print("first",first_ind)
print("last",last_ind)
print(s[first_ind:last_ind+1])