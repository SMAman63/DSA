x=[2,3,4,1,7,6,9,5,5]

while(True):
    done=True
    for i in range(len(x)-1):
        if x[i]>x[i+1]:
            done=False
            x[i],x[i+1]=x[i+1],x[i]
            print(x)
            # temp=x[i+1]
            # x[i+1]=x[i]
            # x[i]=temp
    if done==True:
        break

print(x)
