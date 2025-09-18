def single(arr):
    temp={}
    for i in arr:
        if i not in temp:
            temp[i]=1
            print(temp)
        else:
            temp[i]+=1
        print(temp)
    for j in temp:
        if temp[j]==1:
            print(j)

def main():
    arr=[1,1,4,6,6]
    single(arr)


if __name__=='__main__':
    main()


